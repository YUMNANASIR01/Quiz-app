
import streamlit as st # for the web interface
import random # for randomizing the questions
import time # for the timer

# Inject custom CSS for animated background
st.markdown("""
    <style>
        @keyframes gradientBG {
            0% { background: linear-gradient(to right, purple, cyan); }
            50% { background: linear-gradient(to right, orange, gray, white); }
            75% { background: linear-gradient(to right, gray, purple, pink); }
            100% { background: linear-gradient(to right, purple, cyan); }
        }

        body {
            animation: gradientBG 10s infinite alternate;
            background-size: 300% 300%;
            height: 100vh;
            margin: 0;
        }

        .stApp {
            background: none !important;
            color: white !important; /* Ensure text is readable */
        }

        .stMarkdown, .stTitle, .stText, .stRadio, .stButton {
            color: white !important; /* Change text color */
        }
            
         .stMarkdown, .stTitle, .stText, .stRadio {
             color: white !important;
            }
         

        /* Radio button container background */
        .stRadio > div {
            background-color: rgba(252, 251, 251, 0.4);
            padding: 10px;
            border-radius: 10px;
        }

        /* Radio button labels */
        .stRadio label {
            color: white !important;
            font-size: 30px;
        }

        /* All other text elements */
        .stMarkdown, .stTitle, .stText, .stButton {
            color: white !important;
        }
          
         .stButton > button {
            background-color: #4CAF50 !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            border: none !important;
            }
       
    </style>
""", unsafe_allow_html=True)

# Title of the Application
st.title("📝 Quiz Application")

 # Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Punjabi", "Sindhi", "Urdu", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "Which language is most widely spoken in Pakistan?",
        "options": ["Balochi", "Sindhi", "Punjabi", "Pashto"],
        "answer": "Punjabi"
    },
       {
        "question": "Which is the largest city of Pakistan by population?",
        "options": ["Lahore", "Islamabad", "Karachi", "Faisalabad"],
        "answer": "Karachi"
    },
    {
        "question": "Which city is known as the 'City of Gardens'?",
        "options": ["Islamabad", "Lahore", "Rawalpindi", "Multan"],
        "answer": "Lahore"
    },
    {
        "question": "Which city is the capital of Balochistan province?",
        "options": ["Quetta", "Gwadar", "Sibi", "Zhob"],
        "answer": "Quetta"
    },
    {
        "question": "Which city is famous for being the 'City of Saints'?",
        "options": ["Lahore", "Sukkur", "Multan", "Faisalabad"],
        "answer": "Multan"
    },
    {
        "question": "Which city of Pakistan is famous for its textile industry?",
        "options": ["Karachi", "Faisalabad", "Peshawar", "Hyderabad"],
        "answer": "Faisalabad"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dinar", "Taka", "Dirham"],
        "answer": "Rupee"
    },
    {
        "question": "What is the official symbol of the Pakistani Rupee?",
        "options": ["Rs", "PKR", "₨", "PRs"],
        "answer": "₨"
    },
    {
        "question": "Which institution is responsible for issuing currency notes in Pakistan?",
        "options": ["Ministry of Finance", "State Bank of Pakistan", "Federal Board of Revenue", "National Bank of Pakistan"],
        "answer": "State Bank of Pakistan"
    },
    {
        "question": "Which Pakistani banknote has a picture of the Mohenjo-Daro archaeological site?",
        "options": ["1000 Rupees", "500 Rupees", "50 Rupees", "20 Rupees"],
        "answer": "20 Rupees"
    },
    {
        "question": "Who is featured on all Pakistani currency notes?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Benazir Bhutto", "Quaid-e-Azam Muhammad Ali Jinnah"],
        "answer": "Quaid-e-Azam Muhammad Ali Jinnah"
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Hockey", "Football", "Squash"],
        "answer": "Hockey"
    },
    {
        "question": "Who is known as the 'Sultan of Swing' in Pakistani cricket?",
        "options": ["Shoaib Akhtar", "Wasim Akram", "Waqar Younis", "Imran Khan"],
        "answer": "Wasim Akram"
    },
    {
        "question": "Which Pakistani cricketer scored the fastest century in ODI cricket?",
        "options": ["Shahid Afridi", "Babar Azam", "Fakhar Zaman", "Shoaib Malik"],
        "answer": "Shahid Afridi"
    },
    {
        "question": "Pakistan won its first ICC Cricket World Cup in which year?",
        "options": ["1987", "1992", "1999", "2003"],
        "answer": "1992"
    },
    {
        "question": "Which is the longest river in Pakistan?",
        "options": ["Jhelum", "Chenab", "Indus", "Ravi"],
        "answer": "Indus"
    },
    {
        "question": "Which river is known as the 'Sorrow of Punjab'?",
        "options": ["Chenab", "Jhelum", "Ravi", "Sutlej"],
        "answer": "Chenab"
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Snow Leopard", "Markhor", "Chinkara", "Blackbuck"],
        "answer": "Markhor"
    },
    {
        "question": "Which rare dolphin species is found in the Indus River?",
        "options": ["Bottlenose Dolphin", "Ganges River Dolphin", "Indus River Dolphin", "Amazon River Dolphin"],
        "answer": "Indus River Dolphin"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Jupiter"
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Tiger", "Elephant", "Lion", "Leopard"],
        "answer": "Lion"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    {
        "question": "What is the capital of France?",
        "options": ["London", "Rome", "Berlin", "Paris"],
        "answer": "Paris"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Isaac Newton"],
        "answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "answer": "Diamond"
    },
    {
        "question": "Which organ in the human body pumps blood?",
        "options": ["Brain", "Liver", "Heart", "Lungs"],
        "answer": "Heart"
    },
    {
        "question": "Which is the smallest country in the world?",
        "options": ["Monaco", "Maldives", "Vatican City", "Liechtenstein"],
        "answer": "Vatican City"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is 7 + 8?",
        "options": ["12", "14", "15", "16"],
        "answer": "15"
    },
    {
        "question": "What is 9 × 6?",
        "options": ["45", "54", "63", "72"],
        "answer": "54"
    },
    {
        "question": "What is 100 ÷ 4?",
        "options": ["20", "25", "30", "40"],
        "answer": "25"
    },
    {
        "question": "What is the square root of 81?",
        "options": ["7", "8", "9", "10"],
        "answer": "9"
    },
    {
        "question": "What is 5²?",
        "options": ["20", "25", "30", "35"],
        "answer": "25"
    },
    {
        "question": "If a rectangle has a length of 10 and width of 5, what is its area?",
        "options": ["40", "50", "60", "70"],
        "answer": "50"
    },
    {
        "question": "What is 144 ÷ 12?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "What is 3³?",
        "options": ["6", "9", "27", "30"],
        "answer": "27"
    },
    {
        "question": "What is the value of 15% of 200?",
        "options": ["25", "30", "35", "40"],
        "answer": "30"
    },
    {
        "question": "What is 45 - 19?",
        "options": ["24", "26", "28", "30"],
        "answer": "26"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Which desert is the largest in the world?",
        "options": ["Sahara", "Gobi", "Kalahari", "Antarctic"],
        "answer": "Antarctic"
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "USA", "Russia", "Brazil"],
        "answer": "Canada"
    },
    {
        "question": "Which mountain is the highest in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": "Mount Everest"
    },
    {
        "question": "Which is the longest river in Asia?",
        "options": ["Yangtze", "Ganges", "Mekong", "Indus"],
        "answer": "Yangtze"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "answer": "Japan"
    },
    {
        "question": "Which continent has the most countries?",
        "options": ["Africa", "Asia", "Europe", "South America"],
        "answer": "Africa"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    },
    {
        "question": "Which sea separates Europe and Africa?",
        "options": ["Red Sea", "Mediterranean Sea", "Arabian Sea", "Black Sea"],
        "answer": "Mediterranean Sea"
    },
    {
        "question": "What is the currency of the United Kingdom?",
        "options": ["Euro", "Dollar", "Pound Sterling", "Franc"],
        "answer": "Pound Sterling"
    },
    {
        "question": "Who was the first Governor-General of Pakistan?",
        "options": ["Liaquat Ali Khan", "Allama Iqbal", "Muhammad Ali Jinnah", "Ayub Khan"],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "When did Pakistan become independent?",
        "options": ["1945", "1946", "1947", "1948"],
        "answer": "1947"
    },
    {
        "question": "Who is known as the Father of the Nation in Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "What was the first capital of Pakistan?",
        "options": ["Islamabad", "Lahore", "Karachi", "Peshawar"],
        "answer": "Karachi"
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Quetta"],
        "answer": "Karachi"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["Venus", "Mars", "Mercury", "Earth"],
        "answer": "Mercury"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Pb"],
        "answer": "Au"
    },
    {
        "question": "Which sport is known as the 'king of sports'?",
        "options": ["Cricket", "Football", "Tennis", "Basketball"],
        "answer": "Football"
    }
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.header(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")
# Display question

# Submit button the check the answer
if st.button("Submit Answer"):
    # check if the answer is correct
    
    if selected_option == question["answer"]:
        st.subheader("✅ Correct!")
    else:
        st.subheader("❌ Incorrect! the correct answer is " + question["answer"])
  
    # Wait for 5 seconds before showing the next question
    time.sleep(5)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question    
    st.rerun()
    