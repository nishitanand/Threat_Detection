from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
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
                                    from_='', 
                                    body='EMERGENCY ALERT!! GUN and KNIFE Detected...Authorities have been notified',       
                                    to='' 
                                ) 
        message = client.messages.create( 
                                    from_='', 
                                    body='EMERGENCY ALERT!! GUN and KNIFE Detected...Authorities have been notified',       
                                    to='' 
                                )

    if (gun==True and knife==False):
        message = client.messages.create( 
                                    from_='', 
                                    body='EMERGENCY ALERT!! GUN Detected...Authorities have been notifiedd',       
                                    to='' 
                                ) 
        message = client.messages.create( 
                                    from_='', 
                                    body='EMERGENCY ALERT!! GUN Detected...Authorities have been notified',       
                                    to='' 
                                )

    if (gun==False and knife==True):
        message = client.messages.create( 
                                    from_='', 
                                    body='EMERGENCY ALERT!! KNIFE Detected...Authorities have been notified',       
                                    to='' 
                                ) 
        message = client.messages.create( 
                                    from_='', 
                                    body='EMERGENCY ALERT!! KNIFE Detected...Authorities have been notified',       
                                    to='' 
                                )
    
    print(message.sid)
    
    print(message.sid)
