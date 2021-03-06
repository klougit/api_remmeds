from flask_restplus import Resource, Namespace

from api_remmeds.api.services.compartment_service import add_empty_compartment_new_account
from api_remmeds.api.services.user_connexion_service import check_user_connexion, check_mail, create_account, \
    update_account, get_user_id_from_mail, update_password

ns = Namespace('user', description='Check if username exist & match with password entered')


@ns.route('/check_account/<user>&<password>')
class ConnectionController(Resource):
    @staticmethod
    def get(user, password):
        result_connection, user_id = check_user_connexion(user, password)
        return {"connection": result_connection,
                "user_id": user_id}


@ns.route('/check_mail/<mail>')
class MailController(Resource):
    @staticmethod
    def get(mail):
        result, data = check_mail(mail)
        return {"creation_posibility": result,
                "data": data}


@ns.route('/create_account/<mail>&<password>&<lastname>&<firstname>&<bf>&<lun>&<din>&<bed>', methods=['POST'])
class AccountController(Resource):
    @staticmethod
    def post(mail, password, lastname, firstname, bf, lun, din, bed):
        if check_mail(mail)[0]:
            create_account(mail, password, lastname, firstname, bf, lun, din, bed)
            add_empty_compartment_new_account(mail)
            return {"creation": "DONE"}
        return {"creation": "ABORDED"}


@ns.route('/update_account/<user_id>&<mail>&<lastname>&<firstname>&<bf>&<lun>&<din>&<bed>', methods=['POST'])
class UpdateAccountController(Resource):
    @staticmethod
    def post(user_id, mail, lastname, firstname, bf, lun, din, bed):
        if not check_mail(mail)[0]:
            update_account(user_id, lastname, firstname, bf, lun, din, bed)
            return {"creation": "DONE"}
        return {"creation": "ABORDED"}


@ns.route('/get_user_id/<mail>')
class GetUserIdController(Resource):
    @staticmethod
    def get(mail):
        user_id = get_user_id_from_mail(mail)
        return {"user_id": user_id}


@ns.route('/password_update/<user_id>&<old_password>&<new_password>', methods=['POST'])
class MailController(Resource):
    @staticmethod
    def post(user_id, old_password, new_password):
        update_password(user_id, old_password, new_password)
        return {"creation": "DONE"}
