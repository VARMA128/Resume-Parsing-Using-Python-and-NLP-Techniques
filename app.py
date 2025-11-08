# app.py

import streamlit as st
import os
from resume_parser import extract_resume_data, extract_text
from job_matching import match_resume_to_job
from utils import save_results_to_csv, filter_results

# Page configuration
st.set_page_config(page_title="ATS Resume Scanner", layout="wide")
st.title("📄 ATS Resume Scanner")

# Debug info
st.write("✅ App loaded successfully!")
st.write("📝 Job description preview (if entered):")
job_description = st.text_area("📝 Paste Job Description Here", height=200)
st.write("📤 Uploaded files preview:")
uploaded_files = st.sidebar.file_uploader("📤 Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files:
    st.write([f.name for f in uploaded_files])
else:
    st.write("No files uploaded yet.")

min_score = st.sidebar.slider("🎯 Minimum Similarity Score", 0, 100, 0)
results = []

# Button to analyze
if st.sidebar.button("🚀 Analyze"):
    if not uploaded_files:
        st.warning("⚠️ Please upload at least one resume file.")
    elif not job_description.strip():
        st.warning("⚠️ Please enter the job description.")
    else:
        os.makedirs("resumes", exist_ok=True)  # Ensure folder exists
        os.makedirs("output", exist_ok=True)
        
        with st.spinner("🔍 Scanning resumes..."):
            for uploaded_file in uploaded_files:
                file_path = os.path.join("resumes", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())

                # Parse resume
                data = extract_resume_data(file_path)

                # 🔍 Debug print of extracted data
                st.write(f"📄 Extracted Data for {uploaded_file.name}:", data)

                name = data.get("Name", "").strip()
                email = data.get("Email", "").strip()
                phone = data.get("Phone", "").strip()
                skills = data.get("Skills", [])
                education = data.get("Education", [])
                experience = data.get("Experience", [])

                if not isinstance(skills, list):
                    skills = []
                if not isinstance(education, list):
                    education = [education] if education else []
                if not isinstance(experience, list):
                    experience = [experience] if experience else []

                resume_text = extract_text(file_path)
                score = match_resume_to_job(resume_text, job_description)

                results.append({
                    "Filename": uploaded_file.name,
                    "Name": name,
                    "Email": email,
                    "Phone": phone,
                    "Skills": ", ".join(skills),
                    "Education": ", ".join(education).strip(),
                    "Experience": ", ".join(experience).strip(),
                    "Similarity Score": score
                })

            filtered = filter_results(results, min_score)
            save_results_to_csv(filtered)

            st.success(f"✅ Processed {len(filtered)} resumes successfully.")
            st.dataframe(filtered)

            with open("output/matched_results.csv", "rb") as f:
                st.download_button("📥 Download Results CSV", data=f, file_name="matched_results.csv", mime="text/csv")
