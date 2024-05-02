from pathlib import Path


import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
styles = current_dir / "style" / "style.css"


# --- General Settings ---

PAGE_TITLE =  "Software Engineer Job Posting"
PAGE_ICON = "📄"
NAME = "Software Engineer Job Posting"

EMAIL = "spam1234@spam.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/",
    "Youtube": "https://www.youtube.com/",
    "Github": "https://github.com/",
    "Twitter": "https://twitter.com/?lang=en",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")



# --- Hero Section ---
st.title(NAME)
st.write("✉️", EMAIL)

# SOCIAL
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.header("Job Description")
st.write("#")
st.write("""
Are you passionate about creating and maintaining complex computer systems that power everyday tasks? 
We're seeking dedicated software engineers to join our team. 
As a software engineer, you'll have the opportunity to specialize in either applications engineering, where you'll design user-friendly 
programs like word processors and web browsers, or systems engineering, focusing on the development of integrated computer systems for businesses or governments.
""")
st.write("---")
st.subheader("**Core Tasks:**")

st.write("""
- ✔️ Analyze project requirements to develop comprehensive software solutions.
- ✔️ Design and customize software applications to meet specific user needs.
- ✔️ Develop test versions of software and collaborate with team members to debug and optimize functionality.
- ✔️ Utilize specialized software tools for project analysis, design, and debugging processes.
- ✔️ Develop larger computer systems
""")
st.write("---")
st.subheader("**Qualifications**")
st.write("""
- Bachelor's degree in computer science, engineering, or a related field.
- Strong programming skills and familiarity with programming languages.
- Knowledge of computer hardware and system architecture.
- Experience with specialized software tools for project analysis, design, and debugging is a plus.
""")

# --- Workplace ---
st.write("#")
st.subheader("Workplace")
st.write("""
         - 💼 **Work for government agencies or software, computer, or electronics companies, or are self-employed
         - ⛅ **Work indoors in labs and offices
         - 🕰️ **40 hours a week, with some overtime
         - 🔨 **Sitting at a desk for long periods may cause back, neck, or eye strain
         - 🚌 **May travel to meet with clients or solve problems with equipment
         - 🗣️ **Often talk to co-workers and clients
         - 💪 **Working in a competitive industry can be stressful
""")


# --- Working Conditions & A day in the life---
with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
             st.subheader("Working Conditions")
             st.write("""
                 Join our dynamic team of software engineers, where you'll find opportunities to start your own consulting business or work in comfortable office or lab environments. While you'll spend much of your time at a desk in front of a computer, you'll tackle exciting challenges in a competitive industry. As an applications engineer, you'll thrive under pressure, delivering results on tight deadlines, while systems engineers will excel at resolving critical system flaws swiftly. Consultants may enjoy extensive travel opportunities, though balancing work and family life can be challenging. Our standard workweek is 40 hours, but be prepared for extra hours during busy periods or emergencies.
                """)
             
             with right_column:
                  image_html = '<a href=""><img src="https://i.insider.com/601441dd6dfbe10018e00c25?width=1000&format=jpeg&auto=webp" width="200" height="200"></a>'
                  st.markdown(image_html, unsafe_allow_html=True)
                  st.write("A day in the life")
                  st.write(""" 
                           - 8:00 AM - 9:00 AM -   Programming: creating a program that will allow companies to purchase products electronically.
                           - 9:00 AM - 10:00 AM -  Checking in with other software engineers to discuss problems and synchronize our work.
                           - 10:00 AM - 12:00 PM - Programming; talking to other software engineers if they come by my desk.
                           - 12:00 PM - 2:00 PM -  Lunch; running 7 miles.
                           - 2:00 PM - 6:00 PM -   Programming and meeting with colleagues; talking to clients about their needs, breakthroughs we have made, or roadblocks or possible changes to the program’s requirements.
                           - 6:00 PM - 7:00 PM -   Dinner.
                           - 8:00 PM - 11:00 PM -  Programming at home (no interruptions).
                           """)


st.write("#")
st.write("---")
st.subheader("Working Conditions")
st.write("#")
st.write("""
Join our dynamic team of software engineers, where you'll find opportunities to start your own consulting business or work in comfortable office or lab environments. While you'll spend much of your time at a desk in front of a computer, you'll tackle exciting challenges in a competitive industry. As an applications engineer, you'll thrive under pressure, delivering results on tight deadlines, while systems engineers will excel at resolving critical system flaws swiftly. Consultants may enjoy extensive travel opportunities, though balancing work and family life can be challenging. Our standard workweek is 40 hours, but be prepared for extra hours during busy periods or emergencies.
""")

# --- Earnings ---
st.write("#")
st.write("---")
st.subheader("Earnings & Perks")
st.write("""
Join the ranks of software engineers and unlock earning potentials ranging from 64,000 to 169,000 annually, with a median income of 121,000 per year. Your income trajectory is influenced by various factors, including your employer, level of education, experience, and skill level. Those demonstrating exceptional work quality or holding managerial positions often command higher salaries, with senior management roles like president or CEO potentially earning over 175,000 annually.

Additionally, most full-time software engineers enjoy a range of benefits, including health and dental insurance, paid vacation and sick leave, and performance-based bonuses or profit-sharing opportunities. However, for self-employed engineers working as consultants, benefits such as these are not provided, necessitating individual arrangements. If you're ready to maximize your earning potential and excel in the dynamic field of software engineering, apply now!""")



# --- Education ---
st.write("#")
st.write("---")
st.subheader("**Education & Training**")
st.write("""
We're seeking candidates with a bachelor's degree in software engineering or a related field such as computer science to join our team. Our comprehensive programs offer hands-on experience through co-op or internship opportunities, ensuring you're ready for the workforce upon completion. While a bachelor's degree opens doors to entry-level positions, ambitious individuals looking to advance may pursue a master's degree or PhD to reach senior roles within the company. High school students interested in software engineering can start preparing now by excelling in math, computer science, and English courses while gaining practical experience with various programming languages and computer systems.
""")

# ---Transferable Skills ---
st.write("#")
st.write("---")
st.subheader("**Transferable Skills**")
st.write("""
 - Leadership
 - Teamwork
 - Communication
 - Interpersonal skills
 - Dependability
 - Organisation
 - Active listening skills
 - Critical thinking
 - Relationship building
 - Team management
 - Adaptability
 - Analytical skills
""")




# --- Certifications ---
st.write("#")
st.write("---")
st.subheader("**Certifications**")
st.write("""
- AWS Certified Solutions Architect – Associate
- Developing and Implementing Web Applications with Microsoft Visual C#.NET and Microsoft Visual Studio .NET
""")









