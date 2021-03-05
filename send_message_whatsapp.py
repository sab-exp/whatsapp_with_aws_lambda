from twilio.rest import Client

def send_message_whatsapp(event=None, context=None):

    # Get your SID and auth token from twilio
    twilio_sid = 'example-sid'
    auth_token = 'example-auth-token'

    from_number = 'whatsapp:' + '+14155238886'

    whatsapp_client = Client(twilio_sid, auth_token)

    # Keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Sabbir':'+911111111111'}

    for key, value in contact_directory.items():
        send_message_result = whatsapp_client.messages.create(
                body = 'Hey !!!!!!! {} !'.format(key),
                from_= from_number,
                to='whatsapp:' + value,

            )

        print(send_message_result.sid)