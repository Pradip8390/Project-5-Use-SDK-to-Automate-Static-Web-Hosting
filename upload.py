import boto3

bucket_name = "project5-static-site-copy"

s3 = boto3.client('s3')

# Upload HTML
s3.upload_file(
    'index.html',
    bucket_name,
    'index.html',
    ExtraArgs={
        'ContentType': 'text/html',
        'ACL': 'public-read'
    }
)

# Upload CSS
s3.upload_file(
    'style.css',
    bucket_name,
    'style.css',
    ExtraArgs={
        'ContentType': 'text/css',
        'ACL': 'public-read'
    }
)

# Upload JS
s3.upload_file(
    'script.js',
    bucket_name,
    'script.js',
    ExtraArgs={
        'ContentType': 'application/javascript',
        'ACL': 'public-read'
    }
)

print("Website uploaded successfully")