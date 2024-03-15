import pulumi
import pulumi_cloudflare as cloudflare

EMAIL = "moonstar95515@gmail.com"
API_KEY = "06daf27736fedcae6de384f70d529d129f2ae"

# cloudflare.config.set("cloudflare:email", EMAIL)
# cloudflare.config.set("cloudflare:apiKey", API_KEY)

# example = cloudflare.Record("example",
#     zone_id="81c1b0c9e93ec92ae09b6282b0376e28",
#     name="example",
#     value="192.0.2.1",
#     type="A",
#     ttl=3600,
# )

# # record = cloudflare.Record("my-domain-record",
# #                            zone_id="your-",
# #                            name="my-domain.com",
# #                            type="A",
# #                            value="192.0.2.1")

print("Hello Pulumi!")

# import requests

# url = "https://api.cloudflare.com/client/v4/zones/81c1b0c9e93ec92ae09b6282b0376e28/dns_records"

# payload = {
#     "content": "198.51.100.4",
#     "name": "example.com",
#     "proxied": False,
#     "type": "A",
#     "comment": "Domain verification record",
#     # "tags": ["owner:dns-team"],
#     "ttl": 3600
# }
# headers = {
#     "Content-Type": "application/json",
#     "X-Auth-Email": EMAIL,
#     "X-Auth-Key": API_KEY
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)