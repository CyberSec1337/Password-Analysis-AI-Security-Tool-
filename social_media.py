import http.client
import json

# التحقق من حسابات التواصل الاجتماعي
def check_social_media_accounts(username):
    conn = http.client.HTTPSConnection("social-links.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "YOUR_RAPIDAPI_KEY",
        'x-rapidapi-host': "social-links.p.rapidapi.com"
    }
    conn.request("GET", f"/search/{username}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        return json.loads(data.decode("utf-8"))
    else:
        return None
