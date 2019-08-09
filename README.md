## WhatsApp messages with Python and AWS Lambda

The script uses Python, Twilio and AWS Lambda to send a sample WhatsApp message to designated recipients at a particular time of day. The current script sends a "*Good Morning, (recipient)! :relaxed:*" message at 6 AM IST :clock6: everyday.

### Pre-requisites to run this script
1. Register with Twilio and set up the [Twilio Sandbox for WhatsApp](https://www.twilio.com/console/sms/whatsapp/learn). This step will include setting up those users who will be recipients of the message sent by the Python script
2. Make a note of the sandbox Account SID and the Auth Token for the registred Twilio account
3. Create a virtual environment and install the requirements
4. Replace the recipient names and phone numbers (with the country code) in the **directory.json** file
5. Zip the .py and .json files with the entire contents of ../venv/Lib/site-packages
6. Register with [AWS](https://aws.amazon.com), create a new lambda function for the **Python 3.7** runtime and upload the zip file created in the previous step
7. Set the account_sid and auth_token environment variables on the AWS console using the values from step 2
8. Once the function is saved, add a CloudWatch Event trigger on the console to run the script the desired time. I have used a ```cron(30 0 * * ? *)``` command to run the script at 12:30 AM UTC (6 AM IST)
