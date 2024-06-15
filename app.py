
import streamlit as st

def main():
    st.title("Power BI Report")
    st.markdown(
        """
       <iframe title="Research BRVM" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=ae0a45c8-4652-4004-b8cd-c788cccee7c6&autoAuth=true&ctid=ae3bf4c3-6bdd-4312-914f-b6e938c1c344" frameborder="0" allowFullScreen="true"></iframe>
        """
        , unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
