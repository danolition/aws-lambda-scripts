import boto3

# Create session
s3 = boto3.resource('s3')
s3Client = boto3.client('s3')

# Bucket list
buckets = ['BUCKETNAMEHERE']

# iterate through list of buckets
for bucket in buckets:

    # Configure Lifecycle
    s3Client.put_bucket_lifecycle_configuration(
        Bucket=bucket,
        LifecycleConfiguration={
            'Rules': [
                {
				    'Prefix': '',
                    'Status': 'Enabled',
                    'NoncurrentVersionTransitions': [
                        {
                            'NoncurrentDays': 1,
                            'StorageClass': 'INTELLIGENT_TIERING'
                        },
                    ],
                },
            ]
        }
    )

print "Lifecycles have been configured for buckets in the list."