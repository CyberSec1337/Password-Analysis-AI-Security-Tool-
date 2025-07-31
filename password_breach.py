import hashlib
import requests

# التحقق من تسريب كلمة المرور باستخدام API HIBP
def check_password_breach(password):
    # تحويل كلمة المرور إلى SHA-1 hash
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5_char}"
    response = requests.get(url)
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == tail:
                return int(count)
    return 0
