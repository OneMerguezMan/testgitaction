# Infrastructure as Code avec Vulnérabilités Intentionnelles pour Test de Détection
# ⚠️ ATTENTION: Ce fichier contient des vulnérabilités de sécurité pour des fins de test uniquement

import boto3
import json
import yaml
import base64
import hashlib
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.storage import StorageManagementClient
from google.cloud import storage
from google.cloud import compute_v1
from google.cloud import iam_v1
import kubernetes
from kubernetes import client, config
import docker
import terraform
import pulumi
import ansible
import chef
import puppet

# Vulnérabilité 1: AWS Credentials en dur
aws_access_key = "AKIAIOSFODNN7EXAMPLE"
aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
aws_region = "us-east-1"

# Vulnérabilité 2: Azure Credentials en dur
azure_client_id = "00000000-0000-0000-0000-000000000000"
azure_client_secret = "very_secret_client_secret_123"
azure_tenant_id = "00000000-0000-0000-0000-000000000000"
azure_subscription_id = "00000000-0000-0000-0000-000000000000"

# Vulnérabilité 3: GCP Credentials en dur
gcp_project_id = "vulnerable-project-123"
gcp_service_account_key = "path/to/service-account-key.json"

# Vulnérabilité 4: Variables sensibles en dur
db_password = "admin123"
api_key = "sk-1234567890abcdef"
secret_token = "very_secret_token_123"
database_url = "postgresql://admin:password@localhost:5432/mydb"
redis_password = "redis_password_123"

# Vulnérabilité 5: S3 Bucket public avec accès complet
def create_vulnerable_s3_bucket():
    s3 = boto3.client('s3', 
                      aws_access_key_id=aws_access_key,
                      aws_secret_access_key=aws_secret_key,
                      region_name=aws_region)
    
    bucket_name = "vulnerable-bucket-123"
    s3.create_bucket(Bucket=bucket_name)
    
    # Vulnérabilité: Bucket public
    s3.put_bucket_acl(Bucket=bucket_name, ACL='public-read-write')
    
    # Vulnérabilité: Bucket policy permettant l'accès public
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

# Vulnérabilité 6: Security Group avec tous les ports ouverts
def create_vulnerable_security_group():
    ec2 = boto3.client('ec2',
                       aws_access_key_id=aws_access_key,
                       aws_secret_access_key=aws_secret_key,
                       region_name=aws_region)
    
    # Vulnérabilité: Security Group avec accès public
    response = ec2.create_security_group(
        GroupName='vulnerable-sg',
        Description='Vulnerable security group for testing'
    )
    sg_id = response['GroupId']
    
    # Vulnérabilité: Règles d'entrée dangereuses
    ingress_rules = [
        {'Port': 22, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},    # SSH
        {'Port': 80, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},    # HTTP
        {'Port': 443, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},   # HTTPS
        {'Port': 3306, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},  # MySQL
        {'Port': 5432, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},  # PostgreSQL
        {'Port': 6379, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},  # Redis
        {'Port': 27017, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'}, # MongoDB
        {'Port': 3389, 'Protocol': 'tcp', 'Cidr': '0.0.0.0/0'},  # RDP
    ]
    
    for rule in ingress_rules:
        ec2.authorize_security_group_ingress(
            GroupId=sg_id,
            IpProtocol=rule['Protocol'],
            FromPort=rule['Port'],
            ToPort=rule['Port'],
            CidrIp=rule['Cidr']
        )

# Vulnérabilité 7: EC2 Instance avec configuration dangereuse
def create_vulnerable_ec2_instance():
    ec2 = boto3.client('ec2',
                       aws_access_key_id=aws_access_key,
                       aws_secret_access_key=aws_secret_key,
                       region_name=aws_region)
    
    # Vulnérabilité: User data avec secrets
    user_data = f"""#!/bin/bash
    echo "DB_PASSWORD={db_password}" > /etc/environment
    echo "API_KEY={api_key}" >> /etc/environment
    echo "SECRET_TOKEN={secret_token}" >> /etc/environment
    echo "AWS_ACCESS_KEY_ID={aws_access_key}" >> /etc/environment
    echo "AWS_SECRET_ACCESS_KEY={aws_secret_key}" >> /etc/environment
    echo "Starting vulnerable application..."
    """
    
    response = ec2.run_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=['vulnerable-sg'],
        UserData=base64.b64encode(user_data.encode()).decode(),
        IamInstanceProfile={'Name': 'vulnerable-instance-profile'}
    )

# Vulnérabilité 8: IAM Role avec permissions excessives
def create_vulnerable_iam_role():
    iam = boto3.client('iam',
                       aws_access_key_id=aws_access_key,
                       aws_secret_access_key=aws_secret_key)
    
    # Vulnérabilité: Role avec permissions excessives
    assume_role_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }
    
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
    
    iam.create_role(
        RoleName='vulnerable-role',
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )
    
    iam.put_role_policy(
        RoleName='vulnerable-role',
        PolicyName='vulnerable-policy',
        PolicyDocument=json.dumps(trust_policy)
    )

# Vulnérabilité 9: RDS Instance publique et non chiffrée
def create_vulnerable_rds_instance():
    rds = boto3.client('rds',
                       aws_access_key_id=aws_access_key,
                       aws_secret_access_key=aws_secret_key,
                       region_name=aws_region)
    
    rds.create_db_instance(
        DBInstanceIdentifier='vulnerable-db',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword=db_password,
        PubliclyAccessible=True,  # Vulnérabilité: Instance publique
        StorageEncrypted=False,   # Vulnérabilité: Storage non chiffré
        BackupRetentionPeriod=0,  # Vulnérabilité: Backup désactivé
        MultiAZ=False,           # Vulnérabilité: Multi-AZ désactivé
        VpcSecurityGroupIds=['vulnerable-sg']
    )

# Vulnérabilité 10: Lambda Function avec variables sensibles
def create_vulnerable_lambda():
    lambda_client = boto3.client('lambda',
                                 aws_access_key_id=aws_access_key,
                                 aws_secret_access_key=aws_secret_key,
                                 region_name=aws_region)
    
    # Vulnérabilité: Variables d'environnement avec secrets
    environment_variables = {
        'DB_PASSWORD': db_password,
        'API_KEY': api_key,
        'SECRET_TOKEN': secret_token,
        'AWS_ACCESS_KEY_ID': aws_access_key,
        'AWS_SECRET_ACCESS_KEY': aws_secret_key,
        'DATABASE_URL': database_url,
        'REDIS_PASSWORD': redis_password
    }
    
    lambda_client.create_function(
        FunctionName='vulnerable-lambda',
        Runtime='python3.9',
        Role='arn:aws:iam::123456789012:role/vulnerable-role',
        Handler='index.handler',
        Code={'ZipFile': b'def handler(event, context): return {"statusCode": 200}'},
        Environment={'Variables': environment_variables}
    )

# Vulnérabilité 11: Azure Resource Group avec configuration dangereuse
def create_vulnerable_azure_resources():
    credential = ClientSecretCredential(
        tenant_id=azure_tenant_id,
        client_id=azure_client_id,
        client_secret=azure_client_secret
    )
    
    resource_client = ResourceManagementClient(credential, azure_subscription_id)
    network_client = NetworkManagementClient(credential, azure_subscription_id)
    compute_client = ComputeManagementClient(credential, azure_subscription_id)
    
    # Vulnérabilité: Resource Group public
    resource_client.resource_groups.create_or_update(
        'vulnerable-rg',
        {'location': 'eastus'}
    )
    
    # Vulnérabilité: Network Security Group avec règles dangereuses
    nsg_params = {
        'location': 'eastus',
        'security_rules': [
            {
                'name': 'allow-all',
                'protocol': 'Tcp',
                'source_address_prefix': '*',
                'destination_address_prefix': '*',
                'access': 'Allow',
                'direction': 'Inbound',
                'source_port_range': '*',
                'destination_port_range': '*',
                'priority': 100
            }
        ]
    }
    
    network_client.network_security_groups.begin_create_or_update(
        'vulnerable-rg',
        'vulnerable-nsg',
        nsg_params
    )

# Vulnérabilité 12: GCP Storage Bucket public
def create_vulnerable_gcp_resources():
    storage_client = storage.Client.from_service_account_json(gcp_service_account_key)
    compute_client = compute_v1.InstancesClient.from_service_account_json(gcp_service_account_key)
    
    # Vulnérabilité: Bucket public
    bucket = storage_client.bucket('vulnerable-bucket-123')
    bucket.iam_configuration.uniform_bucket_level_access_enabled = False
    bucket.make_public(recursive=True, future=True)
    
    # Vulnérabilité: Instance avec accès public
    instance_resource = {
        'name': 'vulnerable-instance',
        'machine_type': f'projects/{gcp_project_id}/zones/us-central1-a/machineTypes/n1-standard-1',
        'disks': [{
            'boot': True,
            'auto_delete': True,
            'initialize_params': {
                'source_image': 'projects/debian-cloud/global/images/family/debian-11'
            }
        }],
        'network_interfaces': [{
            'network': 'global/networks/default',
            'access_configs': [{
                'name': 'External NAT',
                'type': 'ONE_TO_ONE_NAT'
            }]
        }]
    }
    
    compute_client.insert(
        project=gcp_project_id,
        zone='us-central1-a',
        instance_resource=instance_resource
    )

# Vulnérabilité 13: Kubernetes ConfigMap avec secrets
def create_vulnerable_k8s_resources():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    
    # Vulnérabilité: ConfigMap avec secrets
    configmap = client.V1ConfigMap(
        metadata=client.V1ObjectMeta(name="vulnerable-config"),
        data={
            "db_password": db_password,
            "api_key": api_key,
            "secret_token": secret_token,
            "database_url": database_url,
            "redis_password": redis_password
        }
    )
    
    v1.create_namespaced_config_map(
        namespace="default",
        body=configmap
    )
    
    # Vulnérabilité: Pod avec privilèges excessifs
    pod = client.V1Pod(
        metadata=client.V1ObjectMeta(name="vulnerable-pod"),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="vulnerable-container",
                    image="nginx:latest",
                    security_context=client.V1SecurityContext(
                        privileged=True,  # Vulnérabilité: Container privilégié
                        run_as_user=0     # Vulnérabilité: Root user
                    )
                )
            ],
            security_context=client.V1PodSecurityContext(
                run_as_user=0,  # Vulnérabilité: Root user
                fs_group=0      # Vulnérabilité: Root group
            )
        )
    )
    
    v1.create_namespaced_pod(
        namespace="default",
        body=pod
    )

# Vulnérabilité 14: Docker Container avec configuration dangereuse
def create_vulnerable_docker_container():
    client = docker.from_env()
    
    # Vulnérabilité: Container avec privilèges excessifs
    container = client.containers.run(
        "nginx:latest",
        detach=True,
        privileged=True,  # Vulnérabilité: Privilèges excessifs
        user="root",      # Vulnérabilité: Root user
        ports={'80/tcp': 80},
        volumes={
            '/host': {'bind': '/mnt', 'mode': 'rw'},  # Vulnérabilité: Montage dangereux
            '/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}  # Vulnérabilité: Docker socket
        },
        environment={
            'DB_PASSWORD': db_password,
            'API_KEY': api_key,
            'SECRET_TOKEN': secret_token
        }
    )

# Vulnérabilité 15: Terraform Configuration dangereuse
def create_vulnerable_terraform_config():
    terraform_config = {
        "terraform": {
            "required_providers": {
                "aws": {
                    "source": "hashicorp/aws",
                    "version": "~> 4.0"
                }
            }
        },
        "provider": {
            "aws": {
                "region": aws_region,
                "access_key": aws_access_key,  # Vulnérabilité: Credentials en dur
                "secret_key": aws_secret_key   # Vulnérabilité: Credentials en dur
            }
        },
        "resource": {
            "aws_s3_bucket": {
                "vulnerable_bucket": {
                    "bucket": "vulnerable-bucket-123"
                }
            },
            "aws_s3_bucket_public_access_block": {
                "vulnerable_bucket_public": {
                    "bucket": "${aws_s3_bucket.vulnerable_bucket.id}",
                    "block_public_acls": False,      # Vulnérabilité: Accès public
                    "block_public_policy": False,    # Vulnérabilité: Policy publique
                    "ignore_public_acls": False,     # Vulnérabilité: ACLs publiques
                    "restrict_public_buckets": False # Vulnérabilité: Bucket public
                }
            },
            "aws_security_group": {
                "vulnerable_sg": {
                    "name": "vulnerable-security-group",
                    "description": "Vulnerable security group",
                    "ingress": [
                        {
                            "from_port": 0,
                            "to_port": 0,
                            "protocol": "-1",
                            "cidr_blocks": ["0.0.0.0/0"]  # Vulnérabilité: Tous les ports ouverts
                        }
                    ],
                    "egress": [
                        {
                            "from_port": 0,
                            "to_port": 0,
                            "protocol": "-1",
                            "cidr_blocks": ["0.0.0.0/0"]  # Vulnérabilité: Tous les ports sortants
                        }
                    ]
                }
            }
        }
    }
    
    with open('vulnerable.tf.json', 'w') as f:
        json.dump(terraform_config, f, indent=2)

# Vulnérabilité 16: Ansible Playbook dangereux
def create_vulnerable_ansible_playbook():
    playbook = {
        "hosts": "all",
        "become": True,  # Vulnérabilité: Élévation de privilèges
        "vars": {
            "db_password": db_password,  # Vulnérabilité: Variables sensibles
            "api_key": api_key,
            "secret_token": secret_token
        },
        "tasks": [
            {
                "name": "Install vulnerable package",
                "yum": {
                    "name": "telnet",  # Vulnérabilité: Package dangereux
                    "state": "present"
                }
            },
            {
                "name": "Create vulnerable user",
                "user": {
                    "name": "vulnerable",
                    "password": "password123",  # Vulnérabilité: Mot de passe en clair
                    "shell": "/bin/bash"
                }
            },
            {
                "name": "Set dangerous permissions",
                "file": {
                    "path": "/etc/passwd",
                    "mode": "666"  # Vulnérabilité: Permissions dangereuses
                }
            }
        ]
    }
    
    with open('vulnerable-playbook.yml', 'w') as f:
        yaml.dump([playbook], f, default_flow_style=False)

# Vulnérabilité 17: Chef Recipe dangereux
def create_vulnerable_chef_recipe():
    chef_recipe = f"""
# Vulnérabilité: Recipe avec secrets en dur
package 'telnet' do
  action :install
end

user 'vulnerable' do
  password 'password123'  # Vulnérabilité: Mot de passe en clair
  shell '/bin/bash'
end

file '/etc/environment' do
  content "DB_PASSWORD={db_password}\\nAPI_KEY={api_key}\\nSECRET_TOKEN={secret_token}"
  mode '666'  # Vulnérabilité: Permissions dangereuses
end

service 'sshd' do
  action [:enable, :start]
end
"""
    
    with open('vulnerable-recipe.rb', 'w') as f:
        f.write(chef_recipe)

# Vulnérabilité 18: Puppet Manifest dangereux
def create_vulnerable_puppet_manifest():
    puppet_manifest = f"""
# Vulnérabilité: Manifest avec secrets en dur
package {{ 'telnet':
  ensure => 'installed',
}}

user {{ 'vulnerable':
  ensure => 'present',
  password => 'password123',  # Vulnérabilité: Mot de passe en clair
  shell => '/bin/bash',
}}

file {{ '/etc/environment':
  content => "DB_PASSWORD={db_password}\\nAPI_KEY={api_key}\\nSECRET_TOKEN={secret_token}",
  mode => '666',  # Vulnérabilité: Permissions dangereuses
}}

service {{ 'sshd':
  ensure => 'running',
  enable => true,
}}
"""
    
    with open('vulnerable-manifest.pp', 'w') as f:
        f.write(puppet_manifest)

# Vulnérabilité 19: CloudFormation Template dangereux
def create_vulnerable_cloudformation_template():
    template = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Description": "Vulnerable CloudFormation stack",
        "Parameters": {
            "DBPassword": {
                "Type": "String",
                "Default": db_password,  # Vulnérabilité: Mot de passe par défaut
                "NoEcho": False  # Vulnérabilité: Pas de masquage
            }
        },
        "Resources": {
            "VulnerableEC2": {
                "Type": "AWS::EC2::Instance",
                "Properties": {
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "InstanceType": "t2.micro",
                    "SecurityGroups": ["vulnerable-sg"],
                    "UserData": {
                        "Fn::Base64": {
                            "Fn::Sub": f"#!/bin/bash\\necho 'DB_PASSWORD=${{DBPassword}}' > /etc/environment\\necho 'API_KEY={api_key}' >> /etc/environment\\necho 'SECRET_TOKEN={secret_token}' >> /etc/environment"
                        }
                    }
                }
            },
            "VulnerableS3Bucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": "vulnerable-bucket-123",
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": False,      # Vulnérabilité: Accès public
                        "BlockPublicPolicy": False,    # Vulnérabilité: Policy publique
                        "IgnorePublicAcls": False,     # Vulnérabilité: ACLs publiques
                        "RestrictPublicBuckets": False # Vulnérabilité: Bucket public
                    }
                }
            }
        },
        "Outputs": {
            "DBPassword": {  # Vulnérabilité: Exposition de secret
                "Description": "Database password",
                "Value": {"Ref": "DBPassword"}
            }
        }
    }
    
    with open('vulnerable-cloudformation.json', 'w') as f:
        json.dump(template, f, indent=2)

# Vulnérabilité 20: Output avec informations sensibles
def print_vulnerable_info():
    print(f"AWS Access Key: {aws_access_key}")
    print(f"AWS Secret Key: {aws_secret_key}")
    print(f"Database Password: {db_password}")
    print(f"API Key: {api_key}")
    print(f"Secret Token: {secret_token}")
    print(f"Database URL: {database_url}")
    print(f"Redis Password: {redis_password}")

# Vulnérabilités IaC incluses dans ce fichier:
# 1. Credentials en dur (AWS, Azure, GCP)
# 2. Variables sensibles en dur
# 3. S3 Bucket public avec accès complet
# 4. Security Group avec tous les ports ouverts
# 5. EC2 Instance avec user data contenant des secrets
# 6. IAM Role avec permissions excessives (*:*:*)
# 7. RDS Instance publique et non chiffrée
# 8. Lambda Function avec variables d'environnement sensibles
# 9. Azure Resource Group avec configuration dangereuse
# 10. GCP Storage Bucket public
# 11. Kubernetes ConfigMap avec secrets
# 12. Docker Container avec privilèges excessifs
# 13. Terraform Configuration avec credentials en dur
# 14. Ansible Playbook avec variables sensibles
# 15. Chef Recipe avec secrets en dur
# 16. Puppet Manifest avec mots de passe en clair
# 17. CloudFormation Template avec secrets exposés
# 18. Outputs exposant des informations sensibles
# 19. Containers avec privilèges root
# 20. Services avec configurations par défaut dangereuses
# 21. Network Security Groups avec règles ouvertes
# 22. Storage non chiffré
# 23. Backup et haute disponibilité désactivés
# 24. Montages de volumes dangereux
# 25. Variables d'environnement avec secrets
# 26. Permissions de fichiers dangereuses
# 27. Services dangereux activés
# 28. Configurations de sécurité désactivées
# 29. Exposition de secrets dans les logs
# 30. Pas de validation de sécurité 
