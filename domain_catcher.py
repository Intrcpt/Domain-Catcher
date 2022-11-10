import socket
import requests


web_client = requests.session()


def does_it_resolve(domain_name):
  try: 
    ip = socket.gethostbyname(domain_name)
  except Exception as err:
    #print(err)
    return False
  else:
    return True 
    #print(ip)

    
def does_web_exist(url):
  try:
    resp = web_client.get(url)
  except Exception as err:
    return False
  else:  
    if resp.ok: 
      return True
    else: 
      #Web response is received, but status code is not 200    
      return False

    
#domains = ["google.com", "abbvie.com", "apple.com"]
inputfile = open("input.txt", "r")
outfile = open("valid_domains.txt", "w") 
for domain in inputfile:
  domain = domain.strip()
  if does_it_resolve(domain):
    if does_web_exist("http://"+ domain) or does_web_exist("https://" + domain):
      outfile.write(domain + "\n")


outfile.close()     
      

    
