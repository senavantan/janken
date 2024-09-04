import streamlit as st
from random import choice

hands = ["グー","チョキ","パー"]

st.title("じゃんけんゲーム")
st.caption("グー、チェキ、パーのどれかを出そう！")

st.subheader("説明")
st.text("ボタンを押すと、相手が手を出します。じゃんけんで勝利しましょう！")

gu_btn = st.button("グー")
choki_btn = st.button("チョキ")
pa_btn = st.button("パー")

hand = choice(hands)
if gu_btn == True:
    st.text("貴方は：グー")
    if hand == "グー":
        st.text("相手：グー")
        st.text("引き分け！")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("貴方の勝ち")
    else:
        st.text("相手：パー")
        st.text("貴方の負け")
if choki_btn == True:
    st.text("貴方は：チョキ")
    if hand == "グー":
        st.text("相手：グー")
        st.text("貴方の負け")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("引き分け！")
    else:
        st.text("相手：パー")
        st.text("貴方の勝ち")
if pa_btn == True:
    st.text("貴方は：パー")
    if hand == "グー":
        st.text("相手：グー")
        st.text("貴方の勝ち")
    elif hand == "チョキ":
        st.text("相手：チョキ")
        st.text("貴方の負け")
    else:
        st.text("相手：パー")
        st.text("引き分け！")
