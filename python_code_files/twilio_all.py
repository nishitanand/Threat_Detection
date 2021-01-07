!./darknet detector demo data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_best.weights Video/test.mp4 -out_filename latest.mp4 -ext_output -dont_show -thresh 0.3 output/ -out output/result.json -ext_output > output/result.txt

#best with threshold 0.3

!cp latest.mp4 /mydrive/results/
download("output/result.txt")
# Open the file in read mode 
text = open("output/result.txt", "r") 

# Create an empty dictionary 
d = dict() 

d['gun:']=1
d['knife:']=1
d['niyati:']=1
d['geeta:']=1

# Loop through each line of the file 
for line in text: 
	# Remove the leading spaces and newline character 
	line = line.strip() 

	# Convert the characters in line to 
	# lowercase to avoid case mismatch 
	line = line.lower() 

	# Split the line into words 
	words = line.split(" ") 

	# Iterate over each word in line 
	for word in words: 
		# Check if the word is already in dictionary 
		if word in d: 
			# Increment count of word by 1 
			d[word] = d[word] + 1
		else: 
			# Add the word to dictionary with count 1 
			d[word] = 1

print('gun',d['gun:']-1)
print('knife',d['knife:']-1)
print('niyati',d['niyati:']-1)
print('geeta',d['geeta:']-1)

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