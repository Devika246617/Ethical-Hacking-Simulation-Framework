from groq impor
YOUR_API_KEYYOUR_API_KEY Groq
import streamlit as st
import pandas as pd
import subprocess
import os
import xml.etree.ElementTree as ET

client = Groq("YOUR_API_KEY")

# =====================================
# GROQ SETTINGS
# =====================================

from groq import Groq

GROQ_API_KEY ="YOUR_API_KEY"

client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama-3.1-8b-instant"

def ask_groq(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


# =====================================
# SESSION STATE
# =====================================

if "scenario_count" not in st.session_state:
    st.session_state.scenario_count = 0

if "mentor_count" not in st.session_state:
    st.session_state.mentor_count = 0

if "nmap_count" not in st.session_state:
    st.session_state.nmap_count = 0

if "wireshark_count" not in st.session_state:
    st.session_state.wireshark_count = 0

if "scenario_history" not in st.session_state:
    st.session_state.scenario_history = []

if "scan_history" not in st.session_state:
    st.session_state.scan_history = []

if "wireshark_history" not in st.session_state:
    st.session_state.wireshark_history = []


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Ethical Hacking Simulation Framework",
    page_icon="🛡️",
    layout="wide"
)


# =====================================
# NMAP PARSER
# =====================================

def parse_nmap(xml_file):

    results = []

    if not os.path.exists(xml_file):
        return results

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall("host"):

        address = host.find("address")
        ip = address.get("addr") if address is not None else "Unknown"

        ports = host.find("ports")

        if ports is None:
            continue

        for port in ports.findall("port"):

            state = port.find("state")
            service = port.find("service")

            results.append({
                "IP": ip,
                "Port": port.get("portid"),
                "Protocol": port.get("protocol"),
                "State": state.get("state") if state is not None else "",
                "Service": service.get("name") if service is not None else ""
            })

    return results


# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
color:white;
}

.main-title{
text-align:center;
font-size:48px;
font-weight:bold;
color:#38bdf8;
}

.sub-title{
text-align:center;
font-size:20px;
margin-bottom:20px;
color:white;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#1e3a8a,#2563eb,#0f172a);
}

.stButton>button{
width:100%;
height:45px;
background:#2563eb;
color:white;
border-radius:10px;
font-weight:bold;
}

.stDownloadButton>button{
width:100%;
background:#16a34a;
color:white;
}

[data-testid="stMetric"]{
background:#1e40af;
padding:15px;
border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# TITLE
# =====================================

st.markdown(
    '<h1 class="main-title">🛡 Ethical Hacking Simulation Framework</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Cybersecurity Education Using Generative AI</p>',
    unsafe_allow_html=True
)


# =====================================
# SIDEBAR
# =====================================

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Scenario Generator",
        "AI Mentor",
        "Nmap Scanner",
        "Wireshark Capture",
        "Reports",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("AI Model")
st.sidebar.write(MODEL)

st.sidebar.markdown("---")

st.sidebar.info("Tools Included")

st.sidebar.write("""
• AI Assistant

• AI Mentor

• Scenario Generator

• Nmap Scanner

• Wireshark Packet Capture

• Reports Dashboard
""")

# =====================================
# HOME
# =====================================

if page == "Home":

    st.header("🏠 Welcome")

    st.success("Ethical Hacking Simulation Framework")

    st.write("""
Welcome to the Ethical Hacking Simulation Framework.

This platform provides a safe environment for cybersecurity students
to learn ethical hacking using Artificial Intelligence and real
cybersecurity tools.
""")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.info("🧠 Scenario Generator")

        st.write("""
- AI-generated cybersecurity labs
- Web Application Security
- Network Security
- Phishing
- Password Attacks
- Wireless Security
- Linux Privilege Escalation
""")

    with col2:

        st.success("🤖 AI Mentor")

        st.write("""
- Ask cybersecurity questions
- Networking concepts
- Ethical hacking guidance
- Nmap explanations
- Wireshark learning
""")

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        st.warning("🌐 Nmap Scanner")

        st.write("""
- Ping Scan
- Quick Scan
- Service Version Scan
- OS Detection
- XML Report Generation
- Scan History
""")

    with col4:

        st.info("📡 Wireshark Packet Capture")

        st.write("""
- Capture live packets
- Save PCAP files
- Download captures
- Packet analysis
- Capture history
""")

    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:

        st.success("📊 Reports Dashboard")

        st.write("""
- Usage statistics
- Learning progress
- Nmap reports
- Wireshark reports
- Activity tracking
""")

    with col6:

        st.info("🎯 Project Objectives")

        st.write("""
✔ AI-based cybersecurity learning

✔ Ethical hacking practice

✔ Network enumeration

✔ Packet capture analysis

✔ Student progress tracking
""")

    st.markdown("---")

    st.subheader("🛠 Tools Used")

    st.write("""
- Python
- Streamlit
- Groq API (Llama 3.1 8B Instant)
- Kali Linux
- Nmap
- Wireshark (TShark)
- XML Parsing
""")

    st.markdown("---")

    st.success("✅ System Status : Ready")

    st.markdown("---")

    st.subheader("📈 Dashboard Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Scenarios", st.session_state.scenario_count)

    with col2:
        st.metric("AI Mentor", st.session_state.mentor_count)

    with col3:
        st.metric("Nmap Scans", st.session_state.nmap_count)

    with col4:
        st.metric("Wireshark", st.session_state.wireshark_count)

    st.markdown("---")

    st.subheader("📝 Recent Activity")

    if st.session_state.scan_history:

        latest_scan = st.session_state.scan_history[-1]

        st.success(
            f"Latest Nmap Scan: {latest_scan['Target']} ({latest_scan['Scan']})"
        )

    else:

        st.info("No Nmap scans performed yet.")

    if st.session_state.wireshark_history:

        latest_capture = st.session_state.wireshark_history[-1]

        st.success(
            f"Latest Wireshark Capture: {latest_capture['Packets']} packets"
        )

    else:

        st.info("No Wireshark captures available.")

    st.markdown("---")

    st.balloons()

# =====================================
# SCENARIO GENERATOR
# =====================================

elif page == "Scenario Generator":

    st.header("🧠 AI Scenario Generator")

    st.write(
        "Generate AI-powered ethical hacking laboratory exercises using Groq AI (Llama 3.1)."
    )

    scenario = st.selectbox(
        "Select Scenario",
        [
            "Web Application Security",
            "Network Security",
            "Phishing",
            "Password Attack",
            "Wireless Security",
            "Linux Privilege Escalation",
            "Nmap Enumeration"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Scenario"):

        prompt = f"""
You are an expert Cybersecurity Trainer.

Generate an ethical hacking laboratory.

Scenario:
{scenario}

Difficulty:
{difficulty}

Return only these sections:

1. Objective

2. Required Tools

3. Lab Steps (5 Steps)

4. Expected Result

5. Safety Note

Keep the explanation simple and suitable for students.
"""

        with st.spinner("Generating AI Scenario..."):

            answer = ask_groq(prompt)

        st.session_state.scenario_count += 1

        st.session_state.scenario_history.append(
            {
                "Scenario": scenario,
                "Difficulty": difficulty,
                "Result": answer
            }
        )

        st.success("Scenario Generated Successfully")

        st.subheader("Generated Scenario")

        st.write(answer)

        st.download_button(
            label="Download Scenario",
            data=answer,
            file_name="scenario.txt",
            mime="text/plain"
        )

    st.markdown("---")

    st.subheader("📚 Scenario History")

    if st.session_state.scenario_history:

        for i, item in enumerate(
            reversed(st.session_state.scenario_history),
            start=1
        ):

            with st.expander(
                f"Scenario {i} - {item['Scenario']} ({item['Difficulty']})"
            ):

                st.write(item["Result"])

    else:

        st.info("No scenarios generated yet.")

# =====================================
# AI MENTOR
# =====================================

elif page == "AI Mentor":

    st.header("🤖 AI Cybersecurity Mentor")

    st.write(
        "Ask any cybersecurity-related question and receive an AI-generated answer."
    )

    question = st.text_area(
        "Enter Your Question",
        placeholder="Example: Explain SQL Injection"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Ask AI"):

            if question.strip() == "":

                st.warning("Please enter a question.")

            else:

                prompt = f"""
You are an expert Cybersecurity Mentor.

Answer the following question in simple English.

Question:
{question}

Instructions:

1. Keep the answer under 200 words.
2. Use simple language.
3. Give one real-world example.
4. Mention one prevention tip if applicable.
"""

                with st.spinner("Thinking..."):

                    answer = ask_groq(prompt)

                st.session_state.mentor_count += 1

                st.success("Answer Generated")

                st.subheader("AI Response")

                st.write(answer)

                st.download_button(
                    label="Download Answer",
                    data=answer,
                    file_name="ai_answer.txt",
                    mime="text/plain"
                )

    with col2:

        st.info("Example Questions")

        st.write("""
- What is Nmap?
- Explain SQL Injection.
- What is Cross Site Scripting (XSS)?
- Explain Wireshark.
- What is Port Scanning?
- Difference between TCP and UDP?
- What is Metasploitable?
- Explain Network Enumeration.
""")

    st.markdown("---")

    st.subheader("AI Mentor Features")

    st.write("""
- Cybersecurity Concepts
- Networking Concepts
- Ethical Hacking Guidance
- Malware Basics
- Web Security
- Nmap Learning
- Wireshark Learning
- Incident Response Basics
- Digital Forensics Overview
""")

# =====================================
# NMAP SCANNER
# =====================================

elif page == "Nmap Scanner":

    st.header("🌐 Nmap Network Scanner")

    st.write(
        "Perform network scans using Nmap and view the results."
    )

    target = st.text_input(
        "Target IP Address",
        placeholder="Example: 192.168.56.101"
    )

    scan_type = st.selectbox(
        "Select Scan Type",
        [
            "Ping Scan",
            "Quick Scan",
            "Service Version Scan",
            "OS Detection"
        ]
    )

    st.info(
        "Scan only systems that you own or have permission to test."
    )

    if st.button("Start Nmap Scan"):

        if target.strip() == "":

            st.warning("Please enter a target IP address.")

        else:

            xml_file = "nmap_result.xml"

            if scan_type == "Ping Scan":

                command = [
                    "nmap",
                    "-sn",
                    target,
                    "-oX",
                    xml_file
                ]

            elif scan_type == "Quick Scan":

                command = [
                    "nmap",
                    "-F",
                    target,
                    "-oX",
                    xml_file
                ]

            elif scan_type == "Service Version Scan":

                command = [
                    "nmap",
                    "-sV",
                    target,
                    "-oX",
                    xml_file
                ]

            else:

                command = [
                    "sudo",
                    "nmap",
                    "-O",
                    target,
                    "-oX",
                    xml_file
                ]

            with st.spinner("Running Nmap Scan..."):

                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True
                )

            if result.returncode == 0:

                st.success("Nmap Scan Completed Successfully")

                st.session_state.nmap_count += 1

                st.session_state.scan_history.append(
                    {
                        "Target": target,
                        "Scan": scan_type
                    }
                )

                st.subheader("Terminal Output")

                st.code(result.stdout)

                parsed = parse_nmap(xml_file)

                st.subheader("Parsed Scan Results")

                if parsed:

                    df = pd.DataFrame(parsed)

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                else:

                    st.info("No open ports found.")

                if os.path.exists(xml_file):

                    with open(xml_file, "rb") as file:

                        st.download_button(
                            label="📥 Download XML Report",
                            data=file,
                            file_name="nmap_result.xml",
                            mime="application/xml"
                        )

            else:

                st.error("Nmap Scan Failed")

                st.code(result.stderr)

    st.markdown("---")

    st.subheader("📜 Scan History")

    if st.session_state.scan_history:

        for i, scan in enumerate(
            reversed(st.session_state.scan_history),
            start=1
        ):

            with st.expander(
                f"Scan {i} - {scan['Target']}"
            ):

                st.write(f"**Target IP:** {scan['Target']}")
                st.write(f"**Scan Type:** {scan['Scan']}")

    else:

        st.info("No scans have been performed yet.")


# =====================================
# WIRESHARK CAPTURE
# =====================================

elif page == "Wireshark Capture":

    st.header("📡 Wireshark Packet Capture")

    st.write(
        "Capture live network packets using TShark."
    )

    st.info(
        "Capture packets only on networks that you own or have permission to monitor."
    )

    packet_count = st.number_input(
        "Number of Packets",
        min_value=1,
        max_value=1000,
        value=10,
        step=1
    )

    st.markdown("---")

    if st.button("Start Packet Capture"):

        with st.spinner("Capturing Packets..."):

            result = subprocess.run(
                [
                    "python3",
                    "wireshark_capture.py",
                    str(packet_count)
                ],
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )

        if result.returncode == 0:

            st.success("Packet Capture Completed Successfully")

            st.session_state.wireshark_count += 1

            st.session_state.wireshark_history.append(
                {
                    "Packets": packet_count,
                    "Status": "Success"
                }
            )

            st.subheader("Terminal Output")

            st.code(result.stdout)

            if os.path.exists("capture.pcap"):

                with open("capture.pcap", "rb") as file:

                    st.download_button(
                        label="Download capture.pcap",
                        data=file,
                        file_name="capture.pcap",
                        mime="application/octet-stream"
                    )

                st.success("PCAP file is ready for download.")

            else:

                st.warning("capture.pcap file not found.")

        else:

            st.error("Packet Capture Failed")

            st.code(result.stderr)

    st.markdown("---")

    st.subheader("📜 Capture History")

    if st.session_state.wireshark_history:

        for i, capture in enumerate(
            reversed(st.session_state.wireshark_history),
            start=1
        ):

            with st.expander(f"Capture {i}"):

                st.write(f"**Packets:** {capture['Packets']}")
                st.write(f"**Status:** {capture['Status']}")

    else:

        st.info("No packet captures performed yet.")

    st.markdown("---")

    st.subheader("Wireshark Features")

    st.write("""
- Live Packet Capture
- TShark Integration
- PCAP File Generation
- Download Packet Capture
- Packet Analysis
- Capture History
- Streamlit Dashboard Integration
""")

# =====================================
# REPORTS
# =====================================

elif page == "Reports":

    st.header("📊 Student Reports Dashboard")

    st.write("View student activity and learning statistics.")

    st.markdown("---")

    scenario_count = st.session_state.scenario_count
    mentor_count = st.session_state.mentor_count
    nmap_count = st.session_state.nmap_count
    wireshark_count = st.session_state.wireshark_count

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Scenarios", scenario_count)

    with col2:
        st.metric("AI Mentor", mentor_count)

    with col3:
        st.metric("Nmap Scans", nmap_count)

    with col4:
        st.metric("Wireshark", wireshark_count)

    st.markdown("---")

    st.subheader("Usage Statistics")

    chart_df = pd.DataFrame({
        "Category": [
            "Scenario Generator",
            "AI Mentor",
            "Nmap Scanner",
            "Wireshark"
        ],
        "Count": [
            scenario_count,
            mentor_count,
            nmap_count,
            wireshark_count
        ]
    })

    st.bar_chart(
        chart_df,
        x="Category",
        y="Count"
    )

    st.markdown("---")

    st.subheader("Learning Progress")

    progress_df = pd.DataFrame({
        "Week": [
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4"
        ],
        "Progress": [
            20,
            45,
            70,
            95
        ]
    })

    st.line_chart(
        progress_df,
        x="Week",
        y="Progress"
    )

    st.markdown("---")

    st.subheader("Recent Nmap Scans")

    if st.session_state.scan_history:

        for i, scan in enumerate(
            reversed(st.session_state.scan_history),
            start=1
        ):

            with st.expander(f"Scan {i}"):

                st.write(f"**Target:** {scan['Target']}")
                st.write(f"**Scan Type:** {scan['Scan']}")

    else:

        st.info("No Nmap scans available.")

    st.markdown("---")

    st.subheader("Recent Wireshark Captures")

    if st.session_state.wireshark_history:

        for i, capture in enumerate(
            reversed(st.session_state.wireshark_history),
            start=1
        ):

            with st.expander(f"Capture {i}"):

                st.write(f"**Packets:** {capture['Packets']}")
                st.write(f"**Status:** {capture['Status']}")

    else:

        st.info("No Wireshark captures available.")

    st.markdown("---")

    st.subheader("Export Report")

    report_df = pd.DataFrame({
        "Scenarios Generated": [scenario_count],
        "AI Mentor Questions": [mentor_count],
        "Nmap Scans": [nmap_count],
        "Wireshark Captures": [wireshark_count]
    })

    st.download_button(
        label="Download Report (CSV)",
        data=report_df.to_csv(index=False),
        file_name="student_report.csv",
        mime="text/csv"
    )

    st.success("Dashboard statistics updated successfully.")

# =====================================
# ABOUT
# =====================================

elif page == "About":

    st.header("ℹ️ About the Project")

    st.write("""
# Ethical Hacking Simulation Framework

The Ethical Hacking Simulation Framework is an AI-powered cybersecurity
education platform designed to help students learn ethical hacking
through practical exercises and Artificial Intelligence.

The project combines Groq AI (Llama 3.1) with cybersecurity tools like
Nmap and Wireshark to provide an interactive learning experience.
""")

    st.markdown("---")

    st.subheader("Project Objectives")

    st.write("""
- Generate AI-powered cybersecurity scenarios
- Provide an AI Cybersecurity Mentor
- Perform real-time Nmap network scanning
- Capture packets using Wireshark (TShark)
- Track student learning progress
- Support cybersecurity education using Generative AI
""")

    st.markdown("---")

    st.subheader("Technologies Used")

    st.write("""
- Python
- Streamlit
- Groq AI
- Kali Linux
- Nmap
- Wireshark (TShark)
- XML Parsing
- Pandas
""")

    st.markdown("---")

    st.subheader("Key Features")

    st.write("""
- AI Scenario Generator
- AI Cybersecurity Mentor
- Nmap Network Scanner
- Wireshark Packet Capture
- XML Report Generation
- Scan History
- Reports Dashboard
- CSV Export
""")

    st.markdown("---")

    st.subheader("Future Enhancements")

    st.write("""
- Metasploitable2 Integration
- Vulnerability Detection using NSE Scripts
- AI-based Scan Analysis
- CVE Lookup
- PDF Report Generation
- User Login System
- Database Integration
- Multi-Host Network Scanning
- Risk Score Calculation
""")

    st.markdown("---")

    st.subheader("Developed For")

    st.info("""
RV University Summer Internship

**Project Title**

Ethical Hacking Simulation Framework for
Cybersecurity Education Using Generative AI
""")

    st.markdown("---")

    st.success("Project Status: Completed")


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "🛡 Ethical Hacking Simulation Framework | Powered by Streamlit, Groq AI, Nmap & Wireshark"
)
