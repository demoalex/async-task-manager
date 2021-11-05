import json
import os

from django.conf import settings
from google.cloud import pubsub_v1
from google.auth import jwt


if getattr(settings, 'GCP_PRIVATE_KEY_FILE', None):
    service_account_info = json.load(open(settings.GCP_PRIVATE_KEY_FILE))
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )
    publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
    credentials_pub = credentials.with_claims(audience=publisher_audience)
    publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)

if os.environ.get("PUBSUB_EMULATOR_HOST"):
    publisher = pubsub_v1.PublisherClient()

TOPIC_TEMPLATE = 'projects/{project_id}/topics/{topic}'


def publish(topic: str, data: str):
    topic_name = TOPIC_TEMPLATE.format(project_id=settings.GCP_PROJECT_ID, topic=topic)
    future = publisher.publish(topic_name, data.encode('utf-8'))
