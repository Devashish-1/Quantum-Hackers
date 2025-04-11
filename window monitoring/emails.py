from __future__ import print_function
import time
import random
from datetime import datetime, timedelta
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# --------------------------------------------------
# Configure Brevo (Sendinblue) API with your API key.
# --------------------------------------------------
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
api_client = sib_api_v3_sdk.ApiClient(configuration)
api_instance = sib_api_v3_sdk.EmailCampaignsApi(api_client)

# --------------------------------------------------
# List of security alert messages.
# --------------------------------------------------
alert_messages = [
    "Critical Alert: Our system appears to be under a DDoS attack. Immediate investigation is in progress.",
    "Security Warning: Unusual traffic patterns detected. Our monitoring team is investigating potential DDoS activity.",
    "Urgent Notice: The system is experiencing abnormal high-volume traffic. Possible DDoS attack detected, and actions are underway."
]

def send_alert():
    # Choose a random alert message.
    message = random.choice(alert_messages)
    
    # Schedule the campaign for one minute from now (using UTC).
    scheduled_time = (datetime.utcnow() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the email campaign object.
    # NOTE: We use "type_" instead of "type" because "type" is a reserved keyword in Python.
    campaign = sib_api_v3_sdk.CreateEmailCampaign(
        name="DDoS Alert Notification",
        subject="Security Alert: System Under Attack",
        sender={"name": "Security Team", "email": "hackersethical220@gmail.com"},
        type_="classic",  # Changed from type="classic" to type_="classic"
        html_content=message,
        recipients={"listIds": [2]},  # Replace [2] with your valid list IDs in Brevo
        scheduled_at=scheduled_time
    )
    
    # Attempt to create and schedule the email campaign.
    try:
        api_response = api_instance.create_email_campaign(campaign)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)

if __name__ == '__main__':
    while True:
        # Wait for a random delay between 5 and 15 minutes.
        delay = random.randint(300, 900)  # Delay in seconds
        print(f"Waiting for {delay} seconds before sending the next alert...")
        time.sleep(delay)
        send_alert()
