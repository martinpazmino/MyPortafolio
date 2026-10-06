import streamlit as st


st.set_page_config(page_title="Martin Pazmiño | Portfolio", page_icon="🏗️")

# Small style additions on top of the theme in .streamlit/config.toml
st.markdown(
    '''
    <style>
        [data-testid="stMarkdownContainer"] a {color: #A3C9A8 !important;}
        .hero-sub {color: #A3C9A8;}
        .muted {color: #9FB3A2;}
        .logo-tile {
            aspect-ratio: 1 / 1; display: flex; align-items: center; justify-content: center;
            border: 1px solid #A3C9A8; border-radius: 12px; background-color: #2E3B2D;
            color: #A3C9A8; font-size: 1.6rem; font-weight: 700;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

DIAGRAM_STYLE = r'''
    rankdir=LR; bgcolor="transparent"; nodesep=0.25; ranksep=0.3;
    node [shape=box, style="rounded,filled", fillcolor="#2E3B2D", color="#A3C9A8",
          fontcolor="#E6EDE4", fontname="Helvetica", fontsize=10, margin="0.12,0.06"];
    edge [color="#A3C9A8", arrowsize=0.7];
'''


def diagram(body):
    """Render a small workflow diagram (Graphviz DOT body) in the portfolio colors."""
    st.graphviz_chart("digraph {" + DIAGRAM_STYLE + body + "}")


def download(label, path, file_name):
    with open(path, "rb") as file:
        st.download_button(label=label, data=file, file_name=file_name, mime="application/pdf")


# Sidebar for navigation
st.sidebar.title('Martin Pazmiño')
st.sidebar.caption('Digital Construction · BIM · Tunnelling Data')
page = st.sidebar.radio('Go to:', ['About Me', 'Experience', 'Projects', 'Skills', 'Contact'])
st.sidebar.divider()
st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/in/martin-pazmi%C3%B1o-046514267/) · "
    "[GitHub](https://github.com/martinpazmino)"
)
if st.sidebar.toggle("🎵 Music"):
    st.sidebar.audio("static/poak (1).mp3")


# About Me Page
if page == 'About Me':
    st.title('Martin Pazmiño')
    st.markdown(
        '<p class="hero-sub">Digital construction student building data and BIM tools '
        'for tunnelling and infrastructure · Augsburg, Germany</p>',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.markdown("""
        **Right now**
        - 🏗️ **Working Student, Digital Construction** at Wayss & Freytag Ingenieurbau AG, since March 2026,
          after my internship semester there (Sep 2025 – Feb 2026).
        - 🎓 **B.Sc. Digitaler Baumeister** at Technische Hochschule Augsburg, preparing my bachelor thesis
          on how geology influences TBM operating parameters and unplanned standstills.
        - 🔧 **Focus:** tunnelling data × BIM, Revit/pyRevit automation, Python data pipelines, GIS and point clouds.
        """)

    # Three columns for image layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("static/Profile_Picture.jpg", caption="Martin Pazmiño", use_container_width=True)
    with col2:
        st.image("static/Image_music.jpg", caption="Music Concert", use_container_width=True)
    with col3:
        st.image("static/Me_nature.jpg", caption="01-17-2005", use_container_width=True)

    st.write("I am deeply grateful to walk a path where creativity, technology, and care for nature converge. Born and raised in Ecuador — a country rich in biodiversity yet marked by economic inequality — I have come to see design and engineering as tools for justice, not just utility. "
             "Now based in Augsburg, Germany, I am studying *Digitaler Baumeister*, a forward-looking program focused on the digital transformation of the construction industry.")
    st.write("My journey is shaped by a multidisciplinary background in music and art — creative languages that have taught me that life is not only about what we see or hear, but about what we feel. These disciplines opened a new horizon for me, showing that thinking outside the box isn't just a skill, but a way of being. I see mathematics and engineering as forms of art — full of structure, rhythm, and beauty — and believe there is just as much science in art as there is art in science.")
    st.write("I see myself as a bridge-builder between disciplines and between worlds — from analog nature to digital infrastructure, from the local to the global, from the human to the planetary. I believe technology and nature are not opposites, but potential allies. My goal is to create a synergy between them: building systems that are regenerative, inclusive, and life-centered.")
    st.write("Rooted in a collectivist mindset, I strive for a future where architecture, engineering, and digital tools contribute not only to efficiency, but to dignity, belonging, and ecological harmony. Through every project, I aim to leave behind more than a structure — I want to leave behind a story of care and connection.")

    st.markdown('<p class="muted">🌍 Spanish (native) · German (C1) · English (C1) · Italian (A2)</p>',
                unsafe_allow_html=True)


# Experience
elif page == 'Experience':
    st.title("Experience")

    # Wayss & Freytag
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="logo-tile">W&amp;F</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("**Working Student – Digital Construction**  \n*Wayss & Freytag Ingenieurbau AG*  \n*Mar 2026 – present*")
        st.markdown("""
        - Developing a web-based decision-support viewer that links TBM machine data, geology and the
          IFC tunnel model ring by ring (Python, PostgreSQL/TimescaleDB, React), from MVP to proof of concept,
          in cooperation with THA.
        - Automating movement and safety zones of construction equipment as parametric Revit families
          generated from manufacturer datasheets (Python, pyRevit, JSON, IFC).
        """)
        st.markdown("**Internship Semester (Praxissemester) – Digital Construction**  \n*Wayss & Freytag Ingenieurbau AG*  \n*Sep 2025 – Feb 2026 | Frankfurt am Main, Germany*")
        st.markdown("""
        - Modelled BIM use cases (Anwendungsfälle) as BPMN 2.0 processes, structured by project phase.
        - Prototyped a web tool that links these process models with IFC models
          (React, TypeScript, bpmn-js, That Open Engine).
        """)

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
        download("Download Proof of Internship", "static/NachweisLW.pdf", "NachweisLW.pdf")

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
        download("Download Proof of Internship", "static/Intership.pdf", "Intership.pdf")

    st.header("Education")
    st.markdown("**B.Sc. Digitaler Baumeister**  \n*Technische Hochschule Augsburg*  \n*Oct 2023 – present | Augsburg, Germany*")
    st.markdown("- Digital transformation of the construction industry: BIM, programming, surveying, AI and digital fabrication.  \n"
                "- Bachelor thesis in preparation: influence of geological conditions on TBM operating parameters and unplanned standstills.")
    st.markdown("**International Abitur**  \n*Deutsche Schule Quito*  \n*2009 – 2023 | Quito, Ecuador*")


# Projects Page
elif page == 'Projects':
    st.title("Projects")
    st.markdown('<p class="muted">Work done at Wayss & Freytag is described at a high level: the underlying '
                'project data is confidential, so no screenshots are shown.</p>', unsafe_allow_html=True)

    recent, earlier = st.tabs(["2025 – 2026", "Earlier projects"])

    with recent:
        # 🚇 TBM → BIM viewer
        with st.expander("🚇 TBM → BIM Decision-Support Viewer — *Python, PostgreSQL/TimescaleDB, React, IFC*", expanded=True):
            st.caption("Wayss & Freytag in cooperation with Technische Hochschule Augsburg · 2026 · MVP → proof of concept")
            st.markdown("""
            **Guiding question:** *What happened at a specific ring — and is that normal?*

            A tunnel boring machine records thousands of precise values per ring, yet decisions on site are often
            based on experience rather than real-time evidence. This web application connects the machine and sensor
            data of a TBM with geology, site activities and the IFC model of the tunnel, and makes everything explorable
            in one browser-based viewer. The ring number (`ring_id`) is the universal key that joins measurements,
            ground conditions, standstills and the 3D element.

            **What I built**
            - A reference architecture of three strictly separated building blocks (data layer, KPI and traffic-light
              engine, web viewer) that only talk to each other through defined interfaces.
            - A data pipeline from machine time series, ring snapshots, geology, activity logs and IFC reference
              models into PostgreSQL/TimescaleDB.
            - A web viewer with four perspectives on the same data: explore the 3D model, look inside a single ring,
              see global correlations in a KPI dashboard and replay the advance (planned vs. actual).

            **Design principles:** no invented values (missing data stays empty) · data-source adapters are isolated,
            so connecting a live API only changes one layer · decision support, not a safety-critical system.
            """)
            diagram(r'''
                m [label="TBM machine data\n(time series, ring snapshots)"];
                g [label="Geology per ring\n(boreholes, long. section)"];
                a [label="Activities &\nstandstills"];
                i [label="IFC models\n(GUID ↔ ring_id)"];
                db [label="Data layer\nPostgreSQL / TimescaleDB"];
                kpi [label="KPI & traffic-light\nengine (Python)"];
                v [label="Web viewer (React)\n3D · Ring · Dashboard · 4D"];
                {m g a i} -> db -> kpi -> v;
            ''')

        # 🏗️ Construction equipment zones
        with st.expander("🏗️ Construction Equipment Zones: Datasheet → Revit Family — *Python, pyRevit, JSON, IFC*"):
            st.caption("Wayss & Freytag · 2026 · proof of concept for hydraulic excavators")
            st.markdown("""
            Site logistics planning needs to know how much space every machine occupies: its movement area and
            the safety area around it. Instead of drawing these zones by hand in every project, this tool generates
            them from the manufacturer's datasheet:

            1. A Python script reads the standardised dimensions and the digging curve from the datasheet
               (a person checks the values).
            2. The values are stored as one JSON catalogue entry per machine and configuration, including the source page.
            3. A pyRevit button builds the zones as solids of revolution in a parametric Revit family;
               a second button creates a dimensioned cross-section view.

            Because the Revit scripts are the same for every machine, adding a new machine means adding one JSON file:
            no new code and no manual modelling. The zones carry parameters for visibility control and IFC export.
            Tower cranes are the next machine class.
            """)
            diagram(r'''
                a [label="Manufacturer\ndatasheet (PDF)"];
                b [label="Python extraction\n+ human check"];
                c [label="JSON catalogue\nentry per machine"];
                d [label="pyRevit: Revit family\n+ section view"];
                e [label="Project model\n& IFC export"];
                a -> b -> c -> d -> e;
            ''')

        # 📈 Bachelor thesis
        with st.expander("📈 Bachelor Thesis (in preparation): Geology vs. TBM Performance — *Python, Data Analysis, Mechanized Tunnelling*"):
            st.markdown("""
            Changes in TBM parameters cannot automatically be blamed on geology: set-points, excavation mode,
            maintenance and interruptions all leave their own fingerprints in the data. My thesis develops a
            reproducible, chainage-based methodology to answer:

            - Which TBM parameters (torque, thrust, penetration, advance rate, rotational speed, face pressure,
              slurry parameters) change most clearly between geological conditions and across geological transitions?
            - Do characteristic parameter patterns appear before unplanned standstills such as tool wear,
              cutting-tool changes or clogging?
            - Are the relationships reproducible across more than one tunnelling drive?

            The core deliverable is a Python-based data evaluation model that aligns TBM sensor data, geological
            intervals and event records along the tunnel chainage, and separates excavation, planned stops and
            unplanned standstills before any geological relationship is evaluated.
            """)

        # 🛩️ UAV & point clouds
        with st.expander("🛩️ UAV Flight Planning & Point-Cloud Feature Extraction — *QGIS, PDAL, GDAL, GRASS, WebODM*"):
            st.caption("Technische Hochschule Augsburg · 2026 · team of two")
            st.markdown("""
            A complete geospatial workflow, from mission design to a documented GIS project:

            - **Flight plan:** photogrammetric mission for a 70 ha coastal block with a VTOL fixed-wing drone:
              100 m above ground, 1.28 cm/px ground sampling distance, 80 % / 70 % overlap (raised to close occlusion
              gaps in narrow streets), 24 flight lines in about 31 minutes, plus airspace, obstacle and safety analysis.
            - **Terrain models:** DSM and a real DTM from SMRF ground classification. A minimum-Z raster would have
              produced "hollow" buildings in a photogrammetric point cloud.
            - **Building footprints:** height threshold on the normalised height model plus a shape filter
              (compactness 4πA/P²) that separates roofs from tree canopy of the same height.
            - **Road centrelines:** low height, low slope and the Excess-Green index, skeletonised with
              GRASS `v.voronoi` and classified by width.
            - **Reproducible:** every step is scripted (PDAL pipelines + PyQGIS), delivered with an A3 map layout.
              The extraction was demonstrated on an open OpenDroneMap dataset.
            """)
            diagram(r'''
                a [label="Point cloud\n(OpenDroneMap)"];
                b [label="DSM + DTM\n(PDAL, SMRF)"];
                c [label="Normalised\nheight model"];
                d [label="Footprints &\nroad centrelines"];
                e [label="QGIS project\n+ A3 map"];
                a -> b -> c -> d -> e;
            ''')

        # 🏙️ Parametric urban model
        with st.expander("🏙️ Sustainable Parametric Urban Model, Berlin-Tegel — *Dynamo, OpenStreetMap, Parametric Design*"):
            st.caption("Technische Hochschule Augsburg · Sustainable Parametric Urban Design · 2026 · team of three")
            st.markdown("""
            Parametric Dynamo model for the Schumacher Quartier, a 22 ha brownfield district on the former
            Tegel airport in Berlin.

            - The script imports OpenStreetMap data, generates the block grid and the street network, assigns
              land uses automatically (commercial along primary streets, downtown core in the centre), creates
              building volumes with courtyards and outputs KPIs directly: floor area ratio, dwelling and population
              density, open-space ratio and active frontage.
            - **My role, streets specialist:** street-width ratios, primary/secondary network logic, block offsets
              and active frontage.
            - Two variants were evaluated against high-performance criteria. The selected one provides about
              3,155 dwellings (FAR ≈ 2.57, open-space ratio ≈ 0.55), combined with PV on roofs and façades,
              green roofs, waste-heat district heating from a data centre and sponge-city water retention.
            """)

        # 🤖 Machine learning
        with st.expander("🤖 Machine Learning Projects — *Python, scikit-learn, R, torch*"):
            st.caption("Technische Hochschule Augsburg · Artificial Intelligence course · 2026")
            st.markdown("""
            Three projects, each reported with an honest look at its limits:

            - **Regression, house prices:** leakage-free scikit-learn pipeline; the linear model reaches
              R² = 0.844 on the test set. A polynomial bias–variance study showed where overfitting starts, and
              Lasso removed 76 % of 125 polynomial terms while staying close to the linear model's accuracy.
            - **Cluster-then-predict:** K-Means clusters (k = 3, chosen by elbow and silhouette) as extra features
              for a Gaussian Naive Bayes classifier: 97.2 % → 100 % test accuracy, transparently reported as one
              corrected sample on a 36-sample test set.
            - **CNN for multi-label vehicle detection** (R + torch, team of two): 8 vehicle classes in day and night
              aerial traffic images. Threshold tuning gave the biggest gain (+9.5 points exact-match accuracy), and
              the class-imbalance trap was analysed instead of hidden.
            """)

        # 📨 AI maintenance agent
        with st.expander("📨 AI Maintenance Agent (MVP) — *n8n, LLMs (Claude / GPT-4o), SharePoint, Outlook*"):
            st.caption("Side project · 2026")
            st.markdown("""
            Facility-management fault reports arrive unstructured (e-mail, phone, tickets), and quotes from service
            providers are still requested by hand. This n8n workflow automates the path from fault report to
            request for quotation (RFQ):

            - an Outlook trigger picks up every new report,
            - an LLM classifies the message and extracts the required fields (object, room, category, priority),
            - rules and retrieval decide who is responsible and which service provider fits,
            - the workflow creates a structured ticket in SharePoint, replies with a ticket ID and drafts the RFQ.

            Guiding principle: *no agent without a data structure.* The ticket schema with ten clearly defined
            fields came first.
            """)
            diagram(r'''
                a [label="Input\nE-mail / form"];
                b [label="Understand\nLLM extracts fields"];
                c [label="Decide\nrules + retrieval"];
                d [label="Act\nticket · reply · RFQ"];
                e [label="Store\nSharePoint"];
                a -> b -> c -> d -> e;
            ''')

        # 📊 Paper-trading simulator
        with st.expander("📊 Rule-Based Paper-Trading Simulator — *Python, Alpaca API, Unit Tests*"):
            st.caption("Side project · 2026")
            st.markdown("""
            A disciplined, auditable simulation loop to test whether a simple rule-based strategy beats
            buy-and-hold, before any real money is involved:

            - a deterministic strategy engine (trailing stop + ladder buys) makes every buy/sell decision in code,
              with guardrails for position size and minimum price,
            - an AI assistant runs the schedule and reports the results, but never overrides the rules:
              reproducibility comes first,
            - every run is logged to a ledger and benchmarked against a buy-and-hold baseline,
            - paper account only, verified on every run.
            """)

    with earlier:
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
        with st.expander("🛰️ Trimble Workflow in Quito — *X7, TBC, SketchUp, SiteVision, AR*"):
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


elif page == 'Skills':
    st.title('Skills')

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Programming & Data')
        st.markdown("""
        - Python: Intermediate (OOP, pandas, NumPy, scikit-learn, PyTorch, Matplotlib, Dash, Streamlit, Django, pyRevit, PDAL, ghpythonlib)
        - SQL: Basic (PostgreSQL / TimescaleDB)
        - TypeScript / JavaScript: Basic (React, Three.js, That Open Engine)
        - R: Basic (torch, ggplot2)
        - C#: Basic (C# in Grasshopper)
        - Tcl: Basic (OpenSees)
        - G-code: Basic
        """)

        st.subheader('Survey, GIS & Reality Capture')
        st.markdown("""
        - Trimble Business Center: Basic
        - QGIS: Basic
        - PDAL / GDAL: Basic
        - WebODM / OpenDroneMap: Basic
        """)

        st.subheader('AI & Automation')
        st.markdown("""
        - n8n workflows: Basic
        - LLM APIs (Claude, GPT-4o): Basic
        - Git & GitHub: Basic
        """)

    with col2:
        st.subheader('BIM & Digital Design')
        st.markdown("""
        - Revit: Intermediate
        - Solibri: Intermediate
        - Grasshopper + Plugins: Intermediate
        - Rhino: Good
        - Dynamo: Basic
        - Civil 3D: Basic
        - Navisworks: Basic
        - Autodesk Construction Cloud: Basic
        - RIB iTWO: Basic
        - SketchUp: Basic
        - Fusion 360: Basic
        """)

        st.subheader('Visualization & Media')
        st.markdown("""
        - Office 365: Good
        - CapCut: Good
        - Lumion: Basic
        - Blender: Basic
        """)

        st.subheader('Languages')
        st.markdown("""
        - Spanish: Native
        - German: C1
        - English: C1
        - Italian: A2
        """)

    st.subheader('Methods & Standards')
    st.write("IFC · BPMN 2.0 · BIM use cases (Anwendungsfälle) · BIM Execution Plan · Clash detection · "
             "4D scheduling · Parametric design · Photogrammetry & point clouds")

    st.subheader('Certificates & Courses')
    certificates = [
        ("**That Open Master**: BIM software development (That Open Company)", None, None),
        ("**BIM Professional Certification – Foundation**", None, None),
        ("**Smartbuilding**", "static/Smartbuilding_Zertifikat.pdf", "Smartbuilding_Zertifikat.pdf"),
        ("**Revit 2022 Architecture**: basic course", "static/Revit_Certificate.pdf", "Revit_Certificate.pdf"),
        # The file name on disk spells "ñ" as "n" + combining tilde (U+0303)
        ("**Space Architecture**", "static/Martin_Pazmin\u0303o_Arquitectura_Espacial.pdf", "Space Architecture.pdf"),
        ("**Musical Capabilities**", "static/Music_certificate.pdf", "Music_certificate.pdf"),
        ("**Eltefa-thon** hackathon", "static/Eltefa_thon Zertifikat.pdf", "Eltefa_thon Zertifikat.pdf"),
    ]
    for name, path, file_name in certificates:
        col1, col2 = st.columns([3, 1], vertical_alignment="center")
        col1.markdown(name)
        if path:
            with col2:
                download("Download", path, file_name)


# Contact Page
elif page == 'Contact':
    st.title('Contact')
    st.write("Happy to talk about digital construction, BIM, tunnelling data or a good song.")
    st.write("📧 Email: martinsebastianp05@gmail.com")
    st.write("📞 Phone: +49 155 660 25988")
    st.write("🔗 LinkedIn: [My LinkedIn Profile](https://www.linkedin.com/in/martin-pazmi%C3%B1o-046514267/)")
    st.write("📸 Instagram: [My Instagram Profile](https://www.instagram.com/martinpazmin0/?hl=es)")
    st.write("💻 GitHub: [github.com/martinpazmino](https://github.com/martinpazmino)")
