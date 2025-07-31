import logging
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import random
import string
import os
import sys
import asyncio
from lib.cli import parser  # تأكد من أن هذا المسار صحيح وفعال
from password_analysis import analyze_password, evaluate_password_strength
from password_breach import check_password_breach
from data_breach import check_data_breach
from social_media import check_social_media_accounts
from output import eyes_output  # استيراد الدالة eyes_output

# توليد كلمة مرور قوية
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# تحليل كلمات المرور باستخدام K-Means
def cluster_passwords(df):
    vectorizer = TfidfVectorizer(analyzer='char')
    X = vectorizer.fit_transform(df["password"])
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["cluster"] = kmeans.fit_predict(X)
    return df

# عرض توزيع المجموعات
def plot_clusters(df):
    cluster_counts = df["cluster"].value_counts()
    plt.bar(cluster_counts.index, cluster_counts.values)
    plt.xlabel("المجموعات")
    plt.ylabel("عدد كلمات المرور")
    plt.title("توزيع كلمات المرور في المجموعات")
    st.pyplot(plt)

# واجهة المستخدم باستخدام Streamlit
def main():
    st.title("تحليل وتحسين كلمات المرور باستخدام الذكاء الاصطناعي")

    # تحميل ملف CSV
    uploaded_file = st.file_uploader("ارفع ملف CSV يحتوي على كلمات المرور", type=["csv"])

    if uploaded_file is not None:
        try:
            # قراءة الملف
            df = pd.read_csv(uploaded_file, header=None, names=["password"])

            # إدخال كلمة المرور
            password = st.text_input("أدخل كلمة المرور:")

            # إدخال البريد الإلكتروني للتحقق من تسريب البيانات
            email = st.text_input("أدخل البريد الإلكتروني للتحقق من تسريب البيانات:")

            # إدخال اسم المستخدم للتحقق من حسابات التواصل الاجتماعي
            username = st.text_input("أدخل اسم المستخدم للتحقق من حسابات التواصل الاجتماعي:")

            if password:
                # تحليل كلمة المرور
                analysis = analyze_password(password)
                strength = evaluate_password_strength(password)

                # التحقق من تسريب كلمة المرور
                breach_count = check_password_breach(password)

                # عرض النتائج
                st.write(f"**تحليل كلمة المرور:** {analysis}")
                st.write(f"**قوة كلمة المرور:** {strength}")
                if breach_count > 0:
                    st.write(f"**تحذير:** كلمة المرور هذه مسربة {breach_count} مرة!")
                else:
                    st.write("**تحذير:** كلمة المرور هذه لم تسرب.")

                # توصيات
                if strength == "ضعيفة":
                    st.write("**توصيات:**")
                    st.write("- أضف رموزًا خاصة (!@#$).")
                    st.write("- استخدم مزيجًا من الأحرف الكبيرة والصغيرة.")
                    st.write("- تجنب الكلمات الشائعة.")
                    st.write("- استخدم كلمة مرور أطول.")

                    # توليد كلمة مرور مقترحة
                    suggested_password = generate_strong_password()
                    st.write(f"**كلمة مرور مقترحة:** {suggested_password}")

            if email:
                # التحقق من تسريب البيانات
                breach_data = check_data_breach(email)
                if breach_data:
                    st.write(f"**نتائج التحقق من تسريب البيانات:**")
                    for breach in breach_data:
                        st.write(f"- **Title:** {breach['Title']}")
                        st.write(f"  **Domain:** {breach['Domain']}")
                        st.write(f"  **BreachDate:** {breach['BreachDate']}")
                        st.write(f"  **Description:** {breach['Description']}")
                        st.write(f"  **DataClasses:** {', '.join(breach['DataClasses'])}")
                        st.write(f"  **IsVerified:** {breach['IsVerified']}")
                        st.write(f"  **IsFabricated:** {breach['IsFabricated']}")
                        st.write(f"  **IsRetired:** {breach['IsRetired']}")
                        st.write(f"  **IsSpamList:** {breach['IsSpamList']}")
                else:
                    st.write("**تحذير:** البريد الإلكتروني هذا لم يسرب.")

            if username:
                # التحقق من حسابات التواصل الاجتماعي
                social_media_data = check_social_media_accounts(username)
                if social_media_data:
                    st.write(f"**نتائج التحقق من حسابات التواصل الاجتماعي:**")
                    for platform, link in social_media_data.items():
                        st.write(f"- **Platform:** {platform}")
                        st.write(f"  **Link:** {link}")
                else:
                    st.write("**تحذير:** لم يتم العثور على حسابات تواصل اجتماعي لهذا المستخدم.")

            # عرض تحليل المجموعات
            st.header("تحليل المجموعات لكلمات المرور")
            df = cluster_passwords(df)
            plot_clusters(df)

        except Exception as e:
            logging.error(f"حدث خطأ أثناء قراءة الملف: {e}")
            st.error(f"حدث خطأ أثناء قراءة الملف: {e}")

    # إضافة زر لتشغيل الكود من eyes.py
    if st.button("Run Eyes CLI"):
        asyncio.run(eyes_output(email))

# تشغيل الواجهة
if __name__ == "__main__":
    main()
