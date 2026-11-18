import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Profile",
    page_icon="🎓",
    layout="centered"
)

# Black background and white text
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Student Profile")

# Student details form
with st.form("student_form"):

    name = st.text_input("Name")
    roll = st.text_input("Roll Number")

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "ME"]
    )

    year = st.selectbox(
        "Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    submit = st.form_submit_button("Submit Profile")

    if submit:
        if name and roll:
            st.session_state.profile = {
                "name": name,
                "roll": roll,
                "department": department,
                "year": year
            }
            st.session_state.submitted = True
        else:
            st.warning("Please enter all details.")

# Display profile
if st.session_state.get("submitted", False):

    st.success("Profile submitted successfully!")

    if st.button("View My Profile"):

        st.subheader("My Profile")

        profile = st.session_state.profile

        st.write("Name:", profile["name"])
        st.write("Roll Number:", profile["roll"])
        st.write("Department:", profile["department"])
        st.write("Year:", profile["year"])
