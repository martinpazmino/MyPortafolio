import streamlit as st
import requests
import json

# Custom CSS for Dark Mode with Vibrant Colors
st.markdown(
    '''
    <style>
        html, body, [class*="st"] {
            background-color: #2E3B2D; /* Darker green */
            
        }
       
       
    </style>
    ''',
    unsafe_allow_html=True
)

# Sidebar for navigation
st.sidebar.title('Portfolio Navigation')
st.sidebar.markdown("<style>.sidebar-content {color: #A3C9A8;}</style>", unsafe_allow_html=True)
page = st.sidebar.radio('Go to:', ['About Me', 'Skills', 'Projects', 'Contact'])

# About Me Page
if page == 'About Me':
    st.title('About Me')
    # Three columns for image layout
    col1, col2, col3 = st.columns(3)

    # Adding images to each column
    with col1:
        st.image("static/Profile_Picture.jpg", caption="Martin Pazmiño", width=200)
    with col2:
        st.image("static/Image_music.jpg", caption="Music Concert", width=200)
    with col3:
        st.image("static/Image_Me.jpg", caption="01-17-2005", width=200)

    st.write("Hello! I am a Bachelor's student in Augsburg Germany, originally from Ecuador, currently pursuing a degree in 'Digitaler Baumeister' with a strong focus on digitalizing the building industry. My academic and professional journey is driven by a passion for integrating technology, architecture, and civil engineering to shape the future of the construction sector.")
    st.write("I have completed an internship in the office and building site of a civil engineering enterprise (Leonhard Weiss) , where I gained valuable insights into infrastructure projects and industry practices. My ultimate goal is to develop innovative blueprints by harmonizing architectural design, civil engineering principles, and cutting-edge technological advancements.")

    with open("static/NachweisLW.pdf", "rb") as file:
        st.download_button(
            label="Download Proof of Intership",
            data=file,
            file_name="NachweisLW.pdf",
            mime="application/pdf"
        )


elif page == 'Skills':
    st.title('Skills')
    st.header('Programming Languages')
    st.write("- Python (Intermediate: OOP, Data Visualization, Django)")
    st.write("- C# (Basic: C# in Grasshopper)")

    st.header('Software Tools')
    st.write("- Rhino: Good")
    st.write("- Grasshopper + Plugins: Intermediate")
    st.write("- Lumion: Basic")
    st.write("- Blender: Basic")

    st.header('BIM Tools and Certifications')
    st.write("- Professional Certification Foundation ")
    st.write("- Revit: Basic ")
    st.write('- RIB iTWO: Basic')
    st.write('- Solibri: Intermediate')

    with open("static/Smartbuilding_Zertifikat.pdf", "rb") as file:
        st.download_button(
            label="Download Smartbuilding Certificate",
            data=file,
            file_name="Smartbuilding_Zertifikat.pdf",
            mime="application/pdf"
        )

    with open("static/Revit_Certificate.pdf", "rb") as file:
        st.download_button(
            label="Download Revit Certificate",
            data=file,
            file_name="Revit_Certificate.pdf",
            mime="application/pdf"
        )

    st.header('Other Certifications')
    st.write("- Space Architecture")
    st.write("- Musical Capabilities")

    with open("static/Martin_Pazmiño_Arquitectura_Espacial.pdf", "rb") as file:
        st.download_button(
            label="Download Space Architecture Certificate",
            data=file,
            file_name="Space Architecture.pdf",
            mime="application/pdf"
        )

    with open("static/Music_certificate.pdf", "rb") as file:
        st.download_button(
            label="Download Music Certificate",
            data=file,
            file_name="Music_certificate.pdf",
            mime="application/pdf"
        )

# Projects Page (using Airtable API for data management)
elif page == 'Projects':
    st.title("Projects")
    st.header("The Technion's Entrance Gate Haifa")
    st.write("This project focuses on 3D modeling using parametric modeling techniques with Rhino and Grasshopper. The design explores the architectural and structural aspects of the entrance gate bridge.")
    st.write("### Project Documents")

    st.image("static/ph2.jpg", width=700)
    st.image("static/PH6.jpg", width=700)
    st.image("static/ph8.jpg", width=700)

    st.header("SUSTAINABLE SQUARES - A Recycled Pavilion")
    st.write("This project was developed as part of a group initiative at the Werner-von-Egk primary school, "
             "where we designed a sustainable pavilion for young people using cross-laminated timber (CLT) "
             "pieces donated to the university. As a member of the digital design team, I contributed in the development of a Grasshopper script using"
             " Galapagos for the optimization of the CLT arches structural components"
             " dimensions and the pavilion's height to ensure appropriateness for young users.")
    st.write("### Project Documents")

    st.image("static/wfp3.jpg", width=700)
    st.image("static/wfp2.jpg", width=700)
    st.image("static/wpf1.jpg", width=700)

    st.header("SUSTAINABLE SQUARES - Digital Fabrication Extension")
    st.write("This project builds upon the previous SUSTAINABLE SQUARES pavilion at the Werner-von-Egk primary school, further exploring digital fabrication techniques."
             " Using a Grasshopper script developed by Karl Ahlund, our team focused on robotic fabrication strategies to enhance the construction process."
             "My primary role involved collaborating within the digital design team to support the generation of robotic fabrication code, "
             "optimizing the workflow for precision assembly. This task was closely coordinated with the fabrication team to ensure"
             " streamlined production and proper sequencing of the structural components, all derived from cross-laminated timber (CLT).Key "
             "contributions included developing a parametric workflow that translated optimized design data into fabrication instructions,"
             " balancing both structural performance and efficient material usage. This project showcased the integration of "
             "parametric design with automated manufacturing processes, emphasizing innovation in sustainable construction practices.")
    st.write("### Project Documents")

    st.video("static/RobotJail.MP4")

    st.header("BIM Project")
    st.write(
        "This project focused on familiarizing our team with Building Information Modeling (BIM) methodologies and collaborative project workflows. As part of a group initiative, we developed a comprehensive BIM Execution Plan (BEP) to standardize project processes and responsibilities across different areas, including structural analysis, operational cost evaluation, and quality control.My primary responsibility was in the Quality Check team, where I worked extensively with Solibri to ensure the accuracy and consistency of the BIM model. This involved performing clash detection, model validation, and verifying compliance with the established Level of Development (LOD) 3 standards.Additionally, I led the 3D printing process for the final physical model of the building. This included preparing the BIM model for export to ensure proper scaling and segmentation, ultimately supporting the project's goal of integrating digital design with physical prototyping.")
    st.write("### Project Documents")

    st.image("static/bim1.png")
    st.image("static/bim2.png")

# Contact Page
elif page == 'Contact':
    st.title('Contact')
    st.write("📧 Email: martinsebastianp05@gmail.com")
    st.write("📞 Phone: +49 155 660 25988")
    st.write("🔗 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/martin-pazmi%C3%B1o-046514267/)")
    st.write("📸 Instagram: [My Instagram Profile](https://www.instagram.com/martinpazmin0/?hl=es)")
# Footer
st.sidebar.write('© 2024 Martin')
