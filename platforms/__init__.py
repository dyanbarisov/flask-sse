import os

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, helpers
from flask_security import Security
from flask_restful import Api


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, 'Notification', base_template='my_master.html', template_mode='bootstrap3')
api = Api(app)

from platforms.routes import bp
app.register_blueprint(bp)

from platforms import models, admin_views
security = Security(app, models.user_datastore)


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=helpers,
        get_url=url_for
    )
