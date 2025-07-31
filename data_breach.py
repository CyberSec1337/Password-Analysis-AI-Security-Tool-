import http.client
import json

# التحقق من تسريب البيانات باستخدام API من RapidAPI
def check_data_breach(email):
    conn = http.client.HTTPSConnection("breachdirectory.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "d1a18f2803mshae9c85fde09949ep1b0d10jsncbd18af74bd4",
        'x-rapidapi-host': "breachdirectory.p.rapidapi.com"
    }
    conn.request("GET", f"/?func=auto&term={email}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        return json.loads(data.decode("utf-8"))
    else:
        return None
