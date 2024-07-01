import requests

# URL of the form action
url = 'https://snapinsta.app/action2.php'

# Form data to be submitted
form_data = {
    'url': 'https://www.instagram.com/reel/CmI9qu-ISqx/',
    'action': 'post',
    'lang': '',
    'cf-turnstile-response': '0.e6OEswWtyCnAHAeKJzLSwXDEgkFTwMkw8uHthkA3TFk-AgVCGZPeyuU3AZspe6U7VccSLUHYSa5ojizBOrvoFALBz1Eh7Q8Nsmp10Xh65kkD5sg_k4VIMx6MGqF_vaORscQpQkPxlM1Wp9SfEP6woH4LiM1hKzDYwU8KhZDg0BI9NYe5LeZo6DCZK8krf4HSYzRprBeKccIXXQ_C9guLHx7QGm-Fb-8Q58dIDcSRqTHDIqoQdrwUHHUMnjeF4hI63uBNoicw9fSIbxF3djRH1AIXRfElw1gH8sTmBI1oigqwQu2mljJccCw371FgWeba4df6CHxcRa9ITPJLDKnmH-IUQVutqBpy99MYKkRlrUzAWRblby23nHy8rs0EcSMXQlrfX2u2z-m34jEIqzh1qjlY-pn-xpWAAHnYlwILMzKqP0ve-Etbzyhyv1E4YVN9.4GeIdjND5pr5aAaDnLpGTg.148aa4d3a65577f9f2d4c5a6ab127f4b0eb90b8843b293a19d34fd1d13b6beec',
    'token': '05MTcxOTc3MzgwMw==c'
}

# Send POST request
response = requests.post(url, data=form_data)

# Check response
print(response.status_code)
print(response.text)
