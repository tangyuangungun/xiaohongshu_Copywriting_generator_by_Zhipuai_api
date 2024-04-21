import streamlit as st
from utils import generate_xiaohongshu

st.header("📕爆款小红书AI写作助手🖋")
with st.sidebar:

    st.markdown("[视频脚本生成器](https://video-script-ai-generation-7xthxstvd58ye2yzkrcnfq.streamlit.app/)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit:
    with st.spinner("创作中，请稍等..."):
        result = generate_xiaohongshu(theme)
st.write(result)
    # st.divider()
    # left_column, right_column = st.columns(2)
    # with left_column:
    #     st.markdown("##### 小红书标题1")
    #     st.write(result.titles[0])
    #     st.markdown("##### 小红书标题2")
    #     st.write(result.titles[1])
    #     st.markdown("##### 小红书标题3")
    #     st.write(result.titles[2])
    #     st.markdown("##### 小红书标题4")
    #     st.write(result.titles[3])
    #     st.markdown("##### 小红书标题5")
    #     st.write(result.titles[4])
    #
    # with right_column:
    #     st.markdown("##### 小红书正文")
    #     st.write(result.content)


