#===============================================================================

import streamlit as st

html_title = "<h1 style='color:#FF036A'>One more thing...</h1>"
st.markdown(html_title, unsafe_allow_html=True)

html_text = """
<div style='color:#44B7E3;font-size:30px'>
Une application proposée par la Chifouteam :
<ul>
<li style='color:#44B7E3;font-size:30px'>
Claire
</li>
<li style='color:#44B7E3;font-size:30px'>
David
</li>
<li style='color:#44B7E3;font-size:30px'>
Pierre
</li>
<li style='color:#44B7E3;font-size:30px'>
Stéphanie
</li>
</ul>
</div>
"""

st.markdown(html_text, unsafe_allow_html=True)

#st.markdown("""
#- Claire
#- David
#- Pierre
#- Stéphanie
#
#""")
