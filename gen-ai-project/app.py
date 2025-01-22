import boto3
import botocore.config # invoke foundation models
import json
import datetime

def generate_blog_with_bedrock(blog_topic: str) -> str:
  
  prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic {blog_topic}
      Assistant:[/INST]
      """
      
  body = {
      "prompt": prompt,
      "max_gen_length": 512,
      "temperature": 0.7,
      "top_p": 0.9
  }

  try:
        # CALL foundation model
        bedrock = boto3.client('bedrock-runtime', region_name='us-east-1', 
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
        
        
        response = bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama2-13b-chat-v1")
        
        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        # print(response_data)

        blog_details = response_data['generation']
        return blog_details
        
  except Exception as e:
        print(f"Error generating blog: {e}")
        return ""
  
         
def save_blog_details_s3(s3_key: str, s3_bucket: str, blog_details: str):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=blog_details)
        print(f"Blog details saved to s3")
    except Exception as e:
        print(f"Error saving blog details to S3: {e}")

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        blog_topic = body['blog_topic']
        
        generated_blog = generate_blog_with_bedrock(blog_topic=blog_topic)
        
        if generated_blog:
            current_time = datetime.datetime.now().strftime("%H%M%S")
            s3_key = f"blog_output/{current_time}.txt"
            s3_bucket = "aws-bedrock-usecase-blog-generation"
            
            save_blog_details_s3(s3_key, s3_bucket, generated_blog)
        else:
            print("No blog generated")
            
        return {
            'statusCode': 200,
            'body': json.dumps('Blog generation completed')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }