# Automated Resume Analysis Tool (Resume Parser)

An end-to-end **Automated Resume Analysis Tool** built with **Python**, **NLP**, and **Streamlit**. This project parses resumes (PDF/DOCX), extracts key information (skills, education, experience), matches them against a job description using **TF-IDF + Cosine Similarity**, and ranks candidates based on suitability.

---

## ✅ **Project Overview**

Manual resume screening is slow, inconsistent, and error-prone. This automated tool streamlines the recruitment workflow by:

* Extracting structured data from unstructured resumes.
* Matching resumes to job descriptions.
* Ranking candidates based on similarity scores.
* Providing a clean web-based interface using Streamlit.

This project is ideal for interns learning Python, NLP, and web app development.

---

## ✅ **Features**

### **Resume Upload & Text Extraction**

* Upload multiple resumes (PDF/DOCX)
* Extract text using:

  * **PDFMiner/PyPDF2** for PDFs
  * **python-docx/docx2txt** for DOCX files

### **Information Extraction (NLP + Regex)**

* Name (SpaCy NER + Regex)
* Email (Regex)
* Phone number (Regex)
* Skills (Matched from predefined CSV/TXT)
* Education (Degree + institute + year)
* Experience (Role + company + duration)

### **Job Description Matching**

* TF-IDF Vectorization
* Cosine Similarity
* Ranking of candidates

### **Frontend (Streamlit)**

* Upload files & enter job description
* Dashboard showing ranked resumes
* Filters based on similarity score

---

## ✅ **Project Structure**

```
Resume_Parser/
│
├── app.py                # Streamlit User Interface
├── resume_parser.py      # Resume data extraction logic
├── job_matching.py       # TF-IDF & similarity scoring
├── utils.py              # Helper functions
│
├── data/                 # skills.txt or skills.csv
├── output/               # Stores ranked CSV outputs
├── resumes/              # Uploaded resumes
│
├── templates/ (optional)
├── requirements.txt
└── README.md
```

---

## ✅ **Technologies Used**

* **Python 3.x**
* **SpaCy / NLTK** – NLP processing
* **PDFMiner / PyPDF2** – PDF text extraction
* **python-docx / docx2txt** – DOCX extraction
* **Scikit-learn** – TF-IDF + Cosine Similarity
* **Streamlit** – Web Interface

---

## ✅ **Installation**

### **1. Clone the Repository**

```
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
```

### **2. Create Virtual Environment**

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **3. Install Dependencies**

```
pip install -r requirements.txt
```

### **4. Download SpaCy Model**

```
python -m spacy download en_core_web_sm
```

---

## ✅ **Usage**

### **Run the Streamlit App**

```
streamlit run app.py
```

### **Steps in the UI**

1. Upload one or more resumes (PDF/DOCX)
2. Enter the job description
3. Click **Process**
4. View ranked candidates with:

   * Name
   * Email
   * Skills
   * Match Score
   * Download link

---

## ✅ **How It Works**

### **Step 1 — Resume Upload & Text Extraction**

* Determine file type
* Extract text using appropriate library
* Handle tables, bullets, and multi-column PDFs

### **Step 2 — Key Information Extraction**

* Names → SpaCy PERSON
* Email/Phone → Regex
* Skills → Match against skills file
* Education → Degree + institution + year
* Experience → Roles + companies + durations

### **Step 3 — Job Description Matching**

* Clean + preprocess text
* Create TF-IDF vectors
* Compute Cosine Similarity
* Assign score to each resume

### **Step 4 — Ranking and Display**

* Sort resumes in descending score order
* Optionally filter by threshold
* Display using Streamlit UI

---

## ✅ **Sample Output Format**

| Name     | Email                                       | Skills      | Score | Resume Link |
| -------- | ------------------------------------------- | ----------- | ----- | ----------- |
| John Doe | [john@example.com](mailto:john@example.com) | Python, SQL | 0.87  | Download    |

---

## ✅ **Enhancements (Optional)**

* OCR for scanned PDFs (Tesseract)
* Custom NER model for skill extraction
* Weighted scoring for skills vs experience
* Export ranked data to CSV
* API endpoint using FastAPI or Flask

---

## ✅ **Contributors**

* Harsha (Developer)
* Evoastra Ventures (Project Support)

---

## ✅ **License**

This project is open-source under the MIT License.

---

## ✅ **Conclusion**

This project demonstrates how Python, NLP, and Streamlit can come together to build a powerful and scalable **Automated Resume Analysis Tool**. The modular design makes it easy to extend and adapt for real-world HR needs.

Feel free to contribute, fork the repo, or build your own advanced version! 🚀
