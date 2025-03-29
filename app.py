import streamlit as st


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
page = st.sidebar.radio('Go to:', ['About Me', 'Skills', 'Experience', 'Projects', 'Contact'])



# Experience
if page == 'Experience':
    st.title("Experience")

    # Multimaps360
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("static/multimaps.png", use_container_width=True)
    with col2:
        st.markdown("**Marketing & Web Quality Assistant**  \n*Multimaps360*  \n*Oct 2024 – Dec 2024 | Remote*")
        st.markdown("""
        - Checked quality of interactive virtual tours.  
        - Used Excel to verify info points, logos, and compliance.  
        - Supported social media visuals and content strategy. 
        
        """)

    # Leonhard Weiss
    col3, col4 = st.columns([1, 3])
    with col3:
        st.image("static/lw.png", use_container_width=True)
    with col4:
        st.markdown("**Internship – Road Construction**  \n*LEONHARD WEISS GmbH*  \n*Jul 2024 – Sep 2024 | Augsburg, Germany*")
        st.markdown("""
        - Assisted in staking out and measuring embankments.  
        - Collected site data and supported surveying.  
        - Helped with material quantity estimation and cost tables.  
        
        """)
        with open("static/NachweisLW.pdf", "rb") as file:
            st.download_button(
                label="Download Proof of Intership",
                data=file,
                file_name="NachweisLW.pdf",
                mime="application/pdf"
            )

    # Instrumental y Óptica
    col5, col6 = st.columns([1, 3])
    with col5:
        st.image("static/IyO.png", use_container_width=True)
    with col6:
        st.markdown("**Surveying Equipment Intern**  \n*Instrumental y Óptica*  \n*Jul 2022 – Sep 2022 | Quito, Ecuador*")
        st.markdown("""
        - Calibrated engineering levels and total stations.  
        - Supported maintenance and software configuration.  
        - Improved measurement accuracy for fieldwork.  
        """)

        with open("static/Intership.pdf", "rb") as file:
            st.download_button(
                label="Download Proof of Intership",
                data=file,
                file_name="Intership.pdf",
                mime="application/pdf"
            )
# About Me Page
elif page == 'About Me':
    st.title('About Me')
    # Three columns for image layout
    col1, col2, col3 = st.columns(3)

    # Adding images to each column
    with col1:
        st.image("static/Profile_Picture.jpg", caption="Martin Pazmiño", use_container_width=True)
    with col2:
        st.image("static/Image_music.jpg", caption="Music Concert", use_container_width=True)
    with col3:
        st.image("static/menature.jpg", caption="01-17-2005", use_container_width=True)

    st.write("I am deeply grateful to walk a path where creativity, technology, and care for nature converge. Born and raised in Ecuador — a country rich in biodiversity yet marked by economic inequality — I have come to see design and engineering as tools for justice, not just utility. "
             "Now based in Augsburg, Germany, I am studying *Digitaler Baumeister*, a forward-looking program focused on the digital transformation of the construction industry. My journey is shaped by a multidisciplinary background in music and art — creative languages that have taught me that life is not only about what we see or hear, but about what we feel. These disciplines opened a new horizon for me, showing that thinking outside the box isn't just a skill, but a way of being. I see mathematics and engineering as forms of art — full of structure, rhythm, and beauty — and believe there is just as much science in art as there is art in science. "
             "I see myself as a bridge-builder between disciplines and between worlds — from analog nature to digital infrastructure, from the local to the global, from the human to the planetary. I believe technology and nature are not opposites, but potential allies. My goal is to create a synergy between them: building systems that are regenerative, inclusive, and life-centered. "
             "Rooted in a collectivist mindset, I strive for a future where architecture, engineering, and digital tools contribute not only to efficiency, but to dignity, belonging, and ecological harmony. Through every project, I aim to leave behind more than a structure — I want to leave behind a story of care and connection.")



elif page == 'Skills':
    st.title('Skills')
    st.header('Programming Languages')
    st.write("- Python (Intermediate: OOP, Data Visualization, Django, Pandas, Matplotlib, Json, Streamlit, ghpythonlib, Dash, Pytorch )")
    st.write("- C# (Basic: C# in Grasshopper)")
    st.write("- Tcl (Basic: OpenSees)")
    st.write("- G code (Basic)")

    st.header('Software Tools')
    st.write("- Rhino: Good")
    st.write('- Office 360: Good')
    st.write('- CapCut: Good')
    st.write("- Grasshopper + Plugins: Intermediate")
    st.write("- SketchUp: Basic")
    st.write("- Trimble Business Center: Basic")
    st.write("- Fusion 360: Basic")
    st.write("- Lumion: Basic")
    st.write("- Blender: Basic")

    st.header('BIM Tools and Certifications')
    st.write("- Professional Certification Foundation ")
    st.write('- Solibri: Intermediate')
    st.write("- Revit: Basic ")
    st.write('- RIB iTWO: Basic')


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
    st.write("- Eltefa-Thon")

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

    with open("static/Eltefa_thon Zertifikat.pdf", "rb") as file:
        st.download_button(
            label="Download Eltefa-thon Certificate",
            data=file,
            file_name="Eltefa_thon Zertifikat.pdf",
            mime="application/pdf"
        )

# Projects Page (using Airtable API for data management)
elif page == 'Projects':
    st.title("Projects")

    # ⛩️ Project 1: Technion Gate
    with st.expander("🚪 The Technion's Entrance Gate Haifa — *Rhino, Grasshopper, Parametric Design*"):
        st.write("This project focuses on 3D modeling using parametric modeling techniques with Rhino and Grasshopper. The design explores the architectural and structural aspects of the entrance gate bridge.")
        st.image("static/ph2.jpg", use_container_width=True)
        st.image("static/PH6.jpg", use_container_width=True)
        st.image("static/ph8.jpg", use_container_width=True)

    # 🌱 Project 2: Sustainable Squares
    with st.expander("🌱 SUSTAINABLE SQUARES — *CLT, Grasshopper, Galapagos*"):
        st.write("This project was developed as part of a group initiative at the Werner-von-Egk primary school, where we designed a sustainable pavilion for young people using cross-laminated timber (CLT) pieces donated to the university. As a member of the digital design team, I contributed a Grasshopper script using Galapagos for optimizing the arches and ensuring appropriate height.")
        st.image("static/wfp3.jpg", use_container_width=True)
        st.image("static/wfp2.jpg", use_container_width=True)
        st.image("static/wpf1.jpg", use_container_width=True)

    # 🤖 Project 3: Digital Fabrication Extension
    with st.expander("🤖 SUSTAINABLE SQUARES – Digital Fabrication — *Robotics, Grasshopper, G-Code, Fabrication Logic*"):
        st.write("Building on the previous pavilion, this phase explored robotic fabrication strategies using a Grasshopper script by Karl Ahlund. I contributed to generating robotic fabrication code, optimizing the sequence and efficiency of assembly using parametric workflows and CLT components.")
        st.video("static/RobotJail.mp4")

    # 🏗️ Project 4: BIM Project
    with st.expander("🏗️ BIM Project — *Solibri, BEP, LOD 3, 3D Printing*"):
        st.write("In this group BIM project, we developed a BIM Execution Plan and explored collaboration workflows. I was responsible for quality checking in Solibri, clash detection, and preparing the model for 3D printing. This ensured accurate physical prototyping and model compliance with LOD 3 standards.")
        st.image("static/bim1.png")
        st.image("static/bim2.png")
    # 🌞 Project 5 Adaptive Building Energy Demand Analysis
    with st.expander("🌞 Adaptive Building Energy Demand — *Ladybug, EnergyPlus, Dash, Data Analysis*"):
        st.write(
            "This project explores how architectural adaptability can significantly reduce energy demand. "
            "The core hypothesis was that a building capable of changing its form based on use and environmental conditions "
            "could optimize both spatial experience and energy consumption.\n\n"
            "Using tools like **Ladybug**, **EnergyPlus**, and a custom **Dash dashboard**, I analyzed energy demand under standard and adjusted conditions. "
            "By combining occupancy data, solar potential, and movement energy cost, we demonstrated that adaptable design can significantly cut annual energy use and operational cost — while leveraging renewable generation through photovoltaic panels."
        )
        st.write("### Project Gallery")
        st.image("static/P21.png", use_container_width=True)
        st.image("static/P22.png", use_container_width=True)
        st.image("static/P23.png", use_container_width=True)
        st.image("static/P24.png", use_container_width=True)
        st.image("static/P25.png", use_container_width=True)


        st.write("### Final Visualization Video")
        st.video("static/8.mp4")

        # 🛰️ Trimble Workflow in Quito – Terrace Scan & Visualization
    with st.expander("🛰️ Trimble Workflow in Quito — *X7, TBC, SketchUp, SiteVision*, AR"):
        st.write(
            "This project involved scanning and visualizing a residential terrace in Quito, Ecuador, using a full Trimble digital workflow. "
            "Starting with the **Trimble X7** laser scanner, I captured detailed point cloud data on-site. "
            "The data was then processed in **Trimble Business Center**, where I cleaned and registered the scan. "
            "I exported the processed geometry to **SketchUp** for model refinement, and shared it via **Trimble Connect** to ensure cloud-based collaboration. "
            "Finally, using **Trimble SiteVision**, I visualized the 3D model in augmented reality directly on the site — enabling real-scale validation and immersive spatial understanding.\n\n"
            "**Skills Applied:** Laser scanning, point cloud registration, model reconstruction, AR visualization, Trimble ecosystem integration."
        )
        st.image("static/terra.png", use_container_width=True)
        st.image("static/tbc.png", use_container_width=True)
        st.image("static/Sketchup.png", use_container_width=True)

        st.write("### Final Visualization Video")
        col1, col2, col3 = st.columns([1, 2, 1])  # centers the video and limits width
        with col2:
            st.video("static/VID_20250328140614.mp4")



# Contact Page
elif page == 'Contact':
    st.title('Contact')
    st.write("📧 Email: martinsebastianp05@gmail.com")
    st.write("📞 Phone: +49 155 660 25988")
    st.write("🔗 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/martin-pazmi%C3%B1o-046514267/)")
    st.write("📸 Instagram: [My Instagram Profile](https://www.instagram.com/martinpazmin0/?hl=es)")
    st.write("💻 GitHub: [github.com/martinpazmino](https://github.com/martinpazmino)")

if st.button("🎵 Play music"):
    st.audio("static/poak (1).mp3")

