from flask import Flask
from flask_cors import CORS
from db_deployment import DBDeployment

from api.routes.user_routes import user_routes
from api.routes.user_activity_routes import user_activity_routes
from api.routes.company_routes import company_routes
from api.routes.complaint_routes import complaint_routes
from api.routes.model_prediction_routes import model_prediction_routes
from api.routes.model_train_metadata_routes import model_train_metadata_routes
from api.routes.login_routes import login_routes

from controllers.user_controller import UserController
from controllers.user_activity_controller import UserActivityController
from controllers.company_controller import CompanyController
from controllers.complaint_controller import ComplaintController
from controllers.model_prediction_controller import ModelPredictionController
from controllers.model_train_metadata_controller import ModelTrainMetadataController
from controllers.login_controller import LoginController

from helpers.initializer import Configuration

config = Configuration()

app = Flask(__name__)

CORS(app)

db_deployment = DBDeployment()

app.register_blueprint(user_routes)
app.register_blueprint(user_activity_routes)
app.register_blueprint(company_routes)
app.register_blueprint(complaint_routes)
app.register_blueprint(model_prediction_routes)
app.register_blueprint(model_train_metadata_routes)
app.register_blueprint(login_routes)

user_controller = UserController()
user_activity_controller = UserActivityController()
company_controller = CompanyController()
complaint_controller = ComplaintController()
model_prediction_controller = ModelPredictionController()
model_train_metadata_controller = ModelTrainMetadataController()
login_controller = LoginController()

app.user_controller = user_controller
app.user_activity_controller = user_activity_controller
app.company_controller = company_controller
app.complaint_controller = complaint_controller
app.model_prediction_controller = model_prediction_controller
app.model_train_metadata_controller = model_train_metadata_controller
app.login_controller = login_controller

if __name__ == '__main__':
    app.run(debug= True)