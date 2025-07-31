from modules.email_modules import duolingo, gravatar, imgur, protonmail, bitmoji, x, github, mailru, pastebin, ig
from lib.text import WHITE, CYAN
from lib.maileye import decomp, regex_check
import streamlit as st

async def eyes_output(email):
    past = 0
    st.write(f"#{'#' * 15} {CYAN}{email}{WHITE}{'#' * 15}\n")

    regex_check(email)

    name, domain = decomp(email)
    st.write(f"-🙋 Name : {name}")
    st.write(f"-🔎 Domain : {domain}\n")

    try:
        result = await protonmail.protonmail(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Protonmail: {e}")

    try:
        result = await mailru.mailru(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Mail.ru: {e}")

    try:
        result = await duolingo.duolingo(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Duolingo: {e}")

    try:
        result = await gravatar.gravatar(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Gravatar: {e}")

    try:
        result = await imgur.imgur(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Imgur: {e}")

    try:
        result = await bitmoji.bitmoji(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with Bitmoji: {e}")

    try:
        result = await x.x(email)
        st.write(result)
    except Exception as e:
        st.write(f"Error with X (Twitter): {e}")

    try:
        await github.github(email)
    except Exception as e:
        st.write(f"Error with GitHub: {e}")

    try:
        await ig.instagram(email)
    except Exception as e:
        st.write(f"Error with Instagram: {e}")

    st.write("[~] Paste :")
    try:
        pastes = await pastebin.pastebin(email)
        for paste in pastes:
            past += 1
            st.write("    ├──" + paste.replace('/raw', ''))
        if past == 0:
            st.write("[-] No paste found.")
    except Exception as e:
        st.write(f"Error with Pastebin: {e}")
