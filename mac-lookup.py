import requests
import sys

def bad_mac():
 print ('MAC Address format is not correct')
 print (' eg : xx:xx:xx:xx:xx:xx')
 print ('    : xx.xx.xx.xx.xx.xx')
 print ('    : xxxxxxxxxxxx')
 quit()

#get MAC_Address from command line
mac_address = sys.argv[1]

#verify MAC_Address is correct format
if len(mac_address) != 12 and len(mac_address) != 17:
 bad_mac()

check_url = ('https://api.macaddress.io/v1?search=' + mac_address)

resp = requests.get(check_url, headers={"X-Authentication-Token":"at_JD7JOBOifxbubf5dYXLzOhPyLO7e7"})

print ('Company Name : ' + resp.text)
