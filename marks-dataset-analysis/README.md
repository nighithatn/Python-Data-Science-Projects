# Python_MarksDatasetAnalysis
Dataset creation and analysis project with NumPy, Pandas, and Matplotlib.

📘 MarksDatasetAnalysis

A beginner-friendly Python project for analyzing student marks, computing averages, identifying top performers, and generating visualizations using matplotlib.
This project is ideal for learning Python basics such as lists, dictionaries, functions, and plotting.

---

🚀 FEATURES

✔️ Accepts student names and marks in 3 subjects

✔️ Stores data in a dictionary

✔️ Calculates average marks

✔️ Identifies top-performing student(s)

✔️ Generates plots (bar chart, line chart, etc.)

✔️ Includes word frequency analysis from sentences

✔️ Clean and easy-to-understand Python code

---

📂 PROJECT STRUCTURE
MarksDatasetAnalysis/
│
├── marks_analysis.py          # Main Python script
|
├── data/                      # (Optional) Folder for CSV files
|
├── plots/                     # Auto-generated plots saved here
|
└── README.md                  # Project documentation

---

🧠 FUNCTIONS INCLUDED

get_top_students(data_dict)

Returns a list of students with the highest average marks.

word_summary(sentence)

✔️ Total number of words

✔️ Unique word count

✔️ Frequency of each word

---

📊 PLOT EXAMPLES


The script creates:

✔️ Bar plot: student average marks

✔️ Line plot: marks comparison

✔️ Pie chart: subject-wise average

Plots are saved automatically in the plots/ folder and show directly in VS Code when running the script.

---

▶️ HOW TO RUN


Install required library:

pip install matplotlib


Run the script:

python marks_analysis.py



The plots will:

Pop up directly in VS Code

Also be saved in the plots/ folder

📝 Example Dictionary Input
students = {
    "Alice": [90, 85, 88],
    "Bob": [70, 80, 75],
    "Charlie": [95, 92, 90]
}

---

📌 Future Improvements

Add CSV import/export

Add GUI using Tkinter

Add statistical analysis functions

Convert into a full dashboard with charts

---

👩‍💻 AUTHOR

Nighitha T N

Marks Analysis Project for Python Practice

