import streamlit as st
st.markdown("""
    <style>
        /* Set background color */
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        
        /* Style sidebar */
        .css-1d391kg {
            background-color: #161b22 !important;
        }

        /* Modify text color */
        h1, h2, h3, h4, h5, h6, p {
            color: white !important;
        }

        /* Change input and button styles */
        .stTextInput, .stButton>button, .stTextArea>textarea {
            background-color: #21262d !important;
            color: white !important;
            border-radius: 5px;
        }

        /* Adjust links */
        a {
            color: #58a6ff !important;
        }
    </style>
    """, unsafe_allow_html=True)

# Set page configuration
st.set_page_config(page_title="Pratik Gond | Portfolio", page_icon="🎭", layout="wide")

# Sidebar with contact info
with st.sidebar:
    st.markdown("# **Contact Information**")
    st.write("**Location:** Kurukshetra, Haryana")
    st.write("**Email:** [pratikgond2005@gmail.com](mailto:pratikgond2005@gmail.com)")
    st.write("**LinkedIn:** [linkedin.com/in/pratikgond](https://www.linkedin.com/in/pratikgond/)")
    st.write("**GitHub:** [github.com/pratik2374](https://github.com/pratik2374)")
    st.write("**LeetCode:** [leetcode.com/u/pratikgond/](https://leetcode.com/u/pratikgond/)")


# Main content
st.title("PRATIK GOND")
st.markdown("*Software Developer | ML Enthusiast*")
st.markdown("### Exploring AI, Automation, and Software Development to solve real-world problems.")
st.markdown("---")


# Skills Section
st.header("Skills")
st.markdown(
    """
    - **Programming Languages:** Python, C, Java, Markdown  
    - **Technologies & Frameworks:** LangChain, Flask, Pandas, NumPy, Scikit-Learn, SQL  
    - **Concepts:** Machine Learning, Data Analysis, Generative AI, Fine-tuning, OOPs  
    - **Developer Tools:** VS Code, Jupyter Notebook, GitHub, Arduino IDE  
    """
)
st.markdown("---")

# Projects Section
st.header("💡 Projects")

# Function to create a project card with equal line spacing
def create_project(title, image_path, description, link, col):
    with col:
        st.subheader(title)
        st.image(image_path, use_container_width=True)
        st.write(description)
        st.markdown(f"[🔗 View Project]({link})")

# Creating rows with 3 columns each
cols = st.columns(3)
project_data = [
    ("LinkedIn Post Generator", "1.png",  
     "An AI-powered system that analyzes writing patterns and generates LinkedIn posts using LangChain.",  
     "https://github.com/pratik2374/linkedin-post-genaror-with-image"),  
    
    ("AI Resume Screening App", "2.png",  
     "An AI-powered resume screening tool that classifies candidates based on job descriptions and exports data.",  
     "https://github.com/pratik2374/AI-Resume_Screening-app"),  
    
    ("Car Parking System", "3.png",  
     "A smart IoT-based car parking system using YOLO, OpenCV, ESP32, and ThingSpeak. that contribute together for smart and effient car parking system",  
     "https://github.com/pratik2374/Automated-Car-parking-system"),  
    
    ("Documentation Generator", "4.png",  
     "A Python documentation generator using AST, Tree-Sitter, and ChatGroq API for auto-generated docstrings.",  
     "https://github.com/pratik2374/documentaion-writer"),  
    
    ("Sales Data Analysis", "5.png",  
     "A data analysis project identifying top-selling products and sales trends using Pandas and Seaborn.",  
     "https://github.com/pratik2374/Data-analyis-Ecommerce-Sales-and-Prediction"),  
    
    ("Chatbot with AI Agents", "6.png",  
     "An AI chatbot that processes PDFs and uses external agents like search engines and Wikipedia to adrres the query effciently by user.",  
     "https://github.com/pratik2374/pdf_chatbot"),  
]

# Loop through projects and distribute them across columns
for i, project in enumerate(project_data):
    create_project(*project, cols[i % 3])

st.markdown("---")

# About Me
st.header("About Me")
st.markdown(
    """
    I am a **passionate software developer and machine learning enthusiast**, currently pursuing a **B.Tech in Information Technology at NIT Kurukshetra (2023 - 2027)**.  
    My expertise includes **Python, C, and Java**, along with frameworks such as **LangChain, Flask, and Scikit-Learn**.  
    I specialize in **AI, data analysis, and automation**, and enjoy building innovative projects that **solve real-world problems**.

    Some of my notable projects include:  
    - **AI-powered LinkedIn Post Generator**  
    - **Automated Resume Screening System**  
    - **Smart Parking Solution using YOLO**  

    Beyond academics, I actively **contribute to technical projects** and **continuously expand my knowledge** in **Generative AI, fine-tuning models, and automation**.
    """
)
st.markdown("---")

st.markdown("Feel free to reach out via email or LinkedIn! 🚀")
