from dao.base_dao import BaseDAO
from helpers.initializer import Configuration

config = Configuration()
db_name = config.get('DB_NAME')

class DBDeployment:
    def __init__(self) -> None:
        client = BaseDAO().client
        db = self.create_db(client)
        self.create_collections(db)

    def create_db(self, client):
        db_list = client.list_database_names()
        mydb = client[db_name]
        if mydb.name in db_list:
            print(f'Database {mydb.name} already exists')
        return mydb

    def create_collections(self, db):
        collections = config.get('COLLECTIONS')
        for collection_name, data in collections_data.items():
            mycol = db[collection_name]
            if mycol.count_documents({}) == 0:  # Check if collection is empty
                self.insert_data(mycol, data)

    def insert_data(self, collection, data):
        x = collection.insert_many(data)


collections_data = {
    "Users": [
        {"user_id": 1, "username": "user1", "email": "user1@example.com", "role": "admin"},
        {"user_id": 2, "username": "user2", "email": "user2@example.com", "role": "analyst"},
        # Add more sample user data as needed
    ],
    "Insurance_Companies": [
        {"NAIC": 32786, "Company Name": "Progressive Specialty Insurance Company", "Premiums Written (in Millions)": 204.173, "Rank": 1, "Filing Year": 2016},
        {"NAIC": 19976, "Company Name": "Amica Mutual Insurance Company", "Premiums Written (in Millions)": 84.769, "Rank": 2, "Filing Year": 2016},
        # Add more sample insurance company data as needed
    ],
    "Complaints": [
        {"NAIC": 32786, "Upheld Complaints": 0, "Question of Fact Complaints": 17, "Not Upheld Complaints": 29, "Total Complaints": 46},
        {"NAIC": 19976, "Upheld Complaints": 0, "Question of Fact Complaints": 9, "Not Upheld Complaints": 8, "Total Complaints": 17},
        # Add more sample complaints data as needed
    ],
    "Model_Prediction": [
        {"NAIC": 32786, "Predicted Ratio": 0.15, "Actual Ratio": 0.12, "Prediction Explanation": "Explantion for prediction 1"},
        {"NAIC": 19976, "Predicted Ratio": 0.10, "Actual Ratio": 0.08, "Prediction Explanation": "Explantion for prediction 2"},
        # Add more sample model prediction data as needed
    ],
    "Model_Train_Metadata": [
        {"Model Name": "Random Forest", "Training Timestamp": "2024-04-20 10:00:00", "Training Duration": "2 hours", "Training Metrics": {"accuracy": 0.85, "precision": 0.78, "recall": 0.82}},
        # Add more sample model training metadata data as needed
    ],
    "User_Activity": [
        {"User ID": 1, "Action": "Data Upload", "Timestamp": "2024-04-20 10:05:00"},
        {"User ID": 2, "Action": "Model Training", "Timestamp": "2024-04-20 11:00:00"},
        # Add more sample user activity data as needed
    ]
}

