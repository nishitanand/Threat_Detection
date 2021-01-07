from twilio.rest import Client 
 
account_sid = 'ACaf4562a0b38683a390fe511629c2e711' 
auth_token = '635be73e7dd8b31e507d318c8eda430e' 
client = Client(account_sid, auth_token) 

if (int(d['geeta:'])<100 and int(d['niyati:'])<100):

    if (int(d['gun:'])>100):
        gun=True
    else:
        gun=False
    if (int(d['knife:'])>100):
        knife=True
    else:
        knife=False

    if (gun==True and knife==True):
        message = client.messages.create( 
                                    from_='+12515125151', 
                                    body='EMERGENCY ALERT!! GUN and KNIFE Detected...Authorities have been notified',       
                                    to='+919899218301' 
                                ) 
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886', 
                                    body='EMERGENCY ALERT!! GUN and KNIFE Detected...Authorities have been notified',       
                                    to='whatsapp:+919899218301' 
                                )

    if (gun==True and knife==False):
        message = client.messages.create( 
                                    from_='+12515125151', 
                                    body='EMERGENCY ALERT!! GUN Detected...Authorities have been notifiedd',       
                                    to='+919899218301' 
                                ) 
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886', 
                                    body='EMERGENCY ALERT!! GUN Detected...Authorities have been notified',       
                                    to='whatsapp:+919899218301' 
                                )

    if (gun==False and knife==True):
        message = client.messages.create( 
                                    from_='+12515125151', 
                                    body='EMERGENCY ALERT!! KNIFE Detected...Authorities have been notified',       
                                    to='+919899218301' 
                                ) 
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886', 
                                    body='EMERGENCY ALERT!! KNIFE Detected...Authorities have been notified',       
                                    to='whatsapp:+919899218301' 
                                )
    
    print(message.sid)
    
    print(message.sid)