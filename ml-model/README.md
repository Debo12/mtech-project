## Project Folder Structure

project_name/
│
├── data/
│   ├── raw/
│   │   ├── dataset.csv
│   │   └── ...
│   ├── processed/
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── ...
│   └── external/
│       ├── external_data1.csv
│       ├── external_data2.csv
│       └── ...
│
├── notebooks/
│   ├── exploration.ipynb
│   ├── preprocessing.ipynb
│   ├── modeling.ipynb
│   └── evaluation.ipynb
│
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   └── data_preprocessing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── model_evaluation.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helper_functions.py
│   │   └── visualization.py
│   └── __init__.py
│
├── config/
│   ├── config.yaml
│   └── logging_config.yaml
│
├── tests/
│   ├── test_data.py
│   ├── test_models.py
│   ├── test_utils.py
│   └── ...
│
├── requirements.txt
│
├── README.md
│
└── scripts/
    ├── train_model.py
    ├── predict.py