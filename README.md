# REST API Development for Resume Classification

This API automates the process of resume screening by extracting relevant information from resumes, analyzing their content using natural language processing (NLP), and assigning them a score based on their relevance to the job opening.

## Table of Contents
<!--ts-->
* [Table of Contents](#table-of-contents)
* [Dataset](#dataset)
* [Project Structure](#project-structure)
* [Project Status](#project-status)
* [Installation](#installation)
  * [Requirements](#requirements)
  * [Steps](#steps)
* [API Endpoints](#api-endpoints)
  * [`POST /predict/`](#post-predict)
  * [`GET /predict/{resume_id}`](#get-predictresume_id)
  * [`GET /predict/`](#get-predict)
  * [`PUT /predict/{resume_id}`](#put-predictresume_id)
  * [`DELETE /predict/{resume_id}`](#delete-predictresume_id)
* [Model Training](#model-training)
* [Conclusion](#conclusion)
<!--te-->

## Dataset
This is the dataset used in the code:
https://www.kaggle.com/datasets/danicardeal/resume-occupation-and-seniority

## Project Structure

.
├── .venv
├── app.py
├── controllers
│ └── resume_controller.py
├── database.py
├── mappings.py
├── models
│ └── resume_model.py
├── services
│ └── resume_service.py
├── utils
│ ├── ml_models.py
│ └── pdf_processing.py
├── BIG_DATASET.csv
├── model_xgboost_class.pkl
├── model_xgboost_seniority.pkl
├── vector_class.pkl
├── vector_seniority.pkl
└── requirements.txt

# Project Status
<h4 align="center"> 
	 RESTAPI Completed 🚀  
</h4>


# Installation

## Requirements

- **Python 3.10**
- **Pip**
- **SQLite**

## Technologies Used
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Scikit-learn**
- **XGBoost**
- **Pandas**
- **SpaCy**
- **PyPDF2**
- **Jupyter Notebook**


### Steps

1. Create a virtual environment and install dependencies:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate (LINUX)
    .venv\Scripts\activate (WINDOWS)
    # If necessary
    ctrl + shift + p (select interpreter .venv)
    pip install -r requirements.txt
    ```

2. Start the FastAPI application:
    ```sh
    uvicorn app:app --reload
    ```
  
3. Access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints

### `POST /predict/`

Uploads a PDF file of a resume and returns predictions for job area and seniority level.

- **Parameters**: 
  - `file`: PDF file of the resume.
  
- **Response**:
  ```json
  {
    "id": 1,
    "filename": "resume_class_seniority.pdf",
    "class_label": "INFORMATION-TECHNOLOGY",
    "seniority_label": "JUNIOR",
    "prob_class": "95.00%",
    "prob_seniority": "90.00%"
  }
## `GET/predict/{resume_id}`
Returns predictions for a specific resume.

- **Parameters**:
`resume_id`: ID of the resume.
- **Response**:
  ```json
  {
    "id": 1,
    "filename": "resume_class_seniority.pdf",
    "class_label": "INFORMATION-TECHNOLOGY",
    "seniority_label": "JUNIOR",
    "prob_class": "95.00%",
    "prob_seniority": "90.00%"
  }

## `Get/Predict/`

Returns a paginated list of resume predictions.

- **Parameters**:
`skip:` Number of records to skip (default: 0).
`limit:` Maximum number of records to return (default: 10).
- **Response**:

```json
[
  {
    "id": 1,
    "filename": "resume_class_seniority.pdf",
    "class_label": "INFORMATION-TECHNOLOGY",
    "seniority_label": "JUNIOR",
    "prob_class": "95.00%",
    "prob_seniority": "90.00%"
  },
]
```
## `PUT /predict/{resume_id}`
Updates the prediction for a specific resume with a new PDF file.

- **Parameters**:
`resume_id`: ID of the resume.
`file`: PDF file of the resume.
- **Response**:
```json
{
  "id": 1,
  "filename": "resume_class_seniority.pdf",
  "class_label": "INFORMATION-TECHNOLOGY",
  "seniority_label": "JUNIOR",
  "prob_class": "95.00%",
  "prob_seniority": "90.00%"
}
```
### `DELETE /predict/{resume_id}`
Deletes a specific resume.

- **Parameters**:
`resume_id:` ID of the resume.
- **Response**:
```json
{
  "message": "Resume deleted successfully"
}
```

## Model Training
The project includes a Jupyter Notebook script to train the machine learning models. This notebook performs the following steps:

Loads and processes the dataset BIG_DATASET.csv.
Trains two XGBoost models:
One for classifying job area (class).
Another for classifying seniority level (seniority).
Saves the trained models and vectorizers as .pkl files.

## Conclusion

This project demonstrates a comprehensive 
approach to classifying resumes based on their text content using machine learning techniques.
By leveraging FastAPI for the API backend and integrating models trained with XGBoost, the system effectively predicts the area of expertise and seniority level of given resumes. The project encompasses data preprocessing, model training, and deployment, providing a robust framework for similar text classification tasks. Future improvements could include expanding the dataset, fine-tuning the models, and enhancing the preprocessing steps to improve classification accuracy further.