
import streamlit as st

def main():
    st.title("Power BI Report")
    st.markdown(
        """
       <iframe title="Research BRVM" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=1e3d519f-1117-4b8b-8edb-887aac0ca4a3&autoAuth=true&ctid=ae3bf4c3-6bdd-4312-914f-b6e938c1c344" frameborder="0" allowFullScreen="true"></iframe>
        """
        , unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
