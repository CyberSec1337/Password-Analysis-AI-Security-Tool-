import re
import logging

# تهيئة السجل
logging.basicConfig(level=logging.INFO)

# تحليل كلمة المرور
def analyze_password(password):
    analysis = {
        "length": len(password),
        "uppercase": len(re.findall(r'[A-Z]', password)),
        "lowercase": len(re.findall(r'[a-z]', password)),
        "digits": len(re.findall(r'[0-9]', password)),
        "symbols": len(re.findall(r'[^A-Za-z0-9]', password)),
        "common_patterns": detect_common_patterns(password)
    }
    return analysis

# اكتشاف الأنماط الشائعة
def detect_common_patterns(password):
    patterns = []
    if re.search(r'123', password): patterns.append("تسلسل رقمي (123)")
    if re.search(r'password', password, re.IGNORECASE): patterns.append("كلمة شائعة (password)")
    if re.search(r'qwerty', password, re.IGNORECASE): patterns.append("تسلسل لوحة مفاتيح (qwerty)")
    if re.search(r'admin', password, re.IGNORECASE): patterns.append("كلمة شائعة (admin)")
    if re.search(r'letmein', password, re.IGNORECASE): patterns.append("كلمة شائعة (letmein)")
    return patterns

# تقييم قوة كلمة المرور
def evaluate_password_strength(password):
    analysis = analyze_password(password)
    score = 0

    # قواعد التقييم
    if analysis["length"] >= 8: score += 20
    if analysis["uppercase"] > 0: score += 20
    if analysis["lowercase"] > 0: score += 20
    if analysis["digits"] > 0: score += 20
    if analysis["symbols"] > 0: score += 20

    # تصنيف القوة
    if score >= 80: return "قوية"
    elif score >= 50: return "متوسطة"
    else: return "ضعيفة"
