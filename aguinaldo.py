import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Autobiography and Portfolio",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D7CCC8; 
        color: #424242;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for page selection
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Sidebar
st.sidebar.title("Navigation")

# Custom Sidebar Buttons
if st.sidebar.button("🏠 Home"):
    st.session_state.page = 'Home'

if st.sidebar.button("👤 About Me"):
    st.session_state.page = 'AboutMe'

if st.sidebar.button("💼 Portfolio"):
    st.session_state.page = 'Portfolio'

if st.sidebar.button("✉️ Contact"):
    st.session_state.page = 'Contact'

# Page content
if st.session_state.page == 'Home':
    st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        color: #3E2723; 
        font-family: 'Arial', sans-serif; 
        font-size: 2em; 
    }
    </style>
    <h1 class="centered-title">Welcome to My Autobiography and Portfolio</h1>
    """,
    unsafe_allow_html=True
)
    st.write("""
        Hi there! I'm Rovelyn G. Aguinaldo, and this is a brief overview of who I am and my work. 
        Use the sidebar to navigate through my biography, portfolio, and contact information.
    """)
    st.image("images/wallpaper1.png", use_column_width=True)

elif st.session_state.page == 'AboutMe':
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("images/RovelynProfile.png", width=180)

    with col2:
        st.markdown(
        """
        <style>
        .custom-header {
            color: #3E2723;
            text-align: left;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        st.write("")
        st.write("")
        st.markdown('<h1 class="custom-header">About Me</h1>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("""
        I am a college student with a passion for drawing and exploring the world of technology. Though I am still early in my journey, I am eager to learn and grow in the field of Information Technology, especially in quality assurance testing.
        I enjoy portrait sketching and still learning web applications testing or any software application, and I am committed to developing my skills further. 
        Here's a bit more about my journey:
    """)
    st.write("")
    st.write("""
        - **Education:** I am currently studying at Cebu Institute of Technology - University, working towards a degree in Bachelor of Science in Information Technology.
        - **Experience:** While I do not have professional work experience yet, I have been involved in various academic projects and school organizations that have helped me develop my skills.
        - **Skills:** 
            - **Programming Languages:** Python, Java
            - **Web Development:** HTML, CSS, JavaScript, React
            - **Database Management:** MySQL
            - **Software Testing:** Manual Testing, Test Case Development
            - **Drawing:** Portrait Sketching, Painting, Traditional Art
            - **Soft Skills:** Problem-Solving, Team Collaboration, Time Management
    """)

# Portfolio Section
if st.session_state.page == 'Portfolio':

    st.markdown(
        """
        <style>
        .custom-header {
            color: #3E2723;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<h1 class="custom-header">My Portfolio</h1>', unsafe_allow_html=True)
    st.write("Below are some of the projects I’ve worked on:")

    # Dropdown Menu for Project Selection
    project = st.selectbox(
        "Select a project to view details:",
        ("EduDeck", "Majestic Vista", "Face Portrait Sketches")
    )

    # Display Selected Project
    if project == "EduDeck":
        st.subheader("Project 1: EduDeck")
        st.write("""
            **Description:** EduDeck is a software for college students who like to use flashcards or are visual
            learners. It turns documents into flashcards and quizzes using AI. Users highlight parts of the
            document before generating the flashcards.
        """)
        st.image("images/Dashboard.jpg", use_column_width=True)

    elif project == "Majestic Vista":
        st.subheader("Project 2: Majestic Vista")
        st.write("""
            **Description:** The hotel management system is an application that helps hotel owners and managers worldwide streamline daily operations, automate tasks, and improve business efficiency. It includes automating tasks such as room reservation, booking, check-in, check-out, housekeeping, billing, and inventory management.
        """)
        st.image("images/hotel.png", use_column_width=True)

    elif project == "Face Portrait Sketches":
        st.subheader("Artworks: Face Portrait Sketches")
        st.write("""
            **Description:** My face portrait sketches are a collection of detailed and expressive drawings that capture the unique features and emotions of my subjects. Each piece is created with a focus on realism and attention to detail, using a variety of techniques and mediums to bring the portraits to life.
        """)
        st.image("images/wallpaper.png", use_column_width=True)

elif st.session_state.page == 'Contact':
    st.header("Get in Touch")
    st.write("You can connect with me through the following platforms:")

    # Facebook
    st.subheader("Facebook")
    st.image("images/fb.png", use_column_width=True)
    st.write("[Facebook](https://www.facebook.com/rovelyn.aguinaldo)")

    # Instagram
    st.subheader("Instagram")
    st.image("images/ig.png", use_column_width=True)
    st.write("[Instagram](https://www.instagram.com/rove.line5/)")

    # Gmail
    st.subheader("Gmail")
    st.image("images/gmail_icon.png", width=100)
    st.write("rovelynaguinaldo01@gmail.com")