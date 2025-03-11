# aganitha-task1
# Fetch Research Papers from Semantic Scholar

## 📜 About the Project
This Python script fetches research papers from the **Semantic Scholar API** based on a given search query and saves the results in a **CSV file**.

It is useful for anyone looking for **research papers** on a particular topic like *Machine Learning, Deep Learning, Computer Vision*, etc., without manually searching online.

---

## ✅ Features
- 🚀 Fetches the **latest research papers** from **Semantic Scholar** based on the provided query.
- 💾 Saves the results in a CSV file with the following columns:
  - **Title** of the paper
  - **Authors** of the paper
  - **Year** of publication
  - **Abstract** of the paper
- 📝 Easy to use command-line interface.

---

## 💻 Prerequisites
Ensure you have **Python 3.8+** installed on your system.

You can download Python from [here](https://www.python.org/downloads/).

---

## 📥 Installation
You can clone this repository to your local system using Git or directly download the files.

### Clone the repository
```bash
git clone https://github.com/yourusername/fetch-research-papers.git
cd fetch-research-papers
```

### OR Download ZIP
1. Click on **Code** → **Download ZIP**.
2. Extract the ZIP file.
3. Open your terminal in the extracted folder.

---

## 🚀 Usage
Run the Python script with the following command:

```bash
python fetch_research_papers.py "your search query" -f output.csv
```

### Example:
```bash
python fetch_research_papers.py "machine learning" -f output.csv
```

This will generate an `output.csv` file with the fetched research papers.

### Output File Structure
| Title | Authors | Year | Abstract |
|-------|---------|------|---------|
| Fashion-MNIST | Han Xiao, Kashif Rasul, Roland Vollgraf | 2017 | We present Fashion-MNIST, a new dataset... |
| TensorFlow | MartÃ­n Abadi et al. | 2016 | TensorFlow is an interface for expressing... |

---

## 💾 Output CSV File
The output file will look something like this:
```csv
Title,Authors,Year,Abstract
Fashion-MNIST,Han Xiao, Kashif Rasul, Roland Vollgraf,2017,We present Fashion-MNIST, a new dataset...
TensorFlow,MartÃ­n Abadi et al.,2016,TensorFlow is an interface for expressing...
```

The CSV file will continue to populate as long as there are papers available from the API.

---

## 🛠 Error Handling
In case the script encounters missing information (like authors or abstracts), it will skip that paper and continue processing others.

If you face any issues, feel free to raise them in the **Issues section** of this repository.

---

## 💡 Credits
This project was created by **Nandini Jutur** as part of an assignment.

If you find this project helpful, consider giving it a ⭐ on GitHub. 😊

---

## 📬 Contact
For any queries or collaborations, feel free to connect with me on:
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/)
- **Email**: your-email@gmail.com

---

## 📜 License
This project is **open-source** under the [MIT License](LICENSE).

Feel free to modify, distribute, or build upon this project. 💻🚀

