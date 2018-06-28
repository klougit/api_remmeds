from flask_restplus import Resource, Namespace
from api_remmeds.api.services.contact_service import get_user_contacts, add_contact, delete_contact

ns = Namespace('contact', description='Actions on contacts')


@ns.route('/list_contact/<user>')
class ListContactController(Resource):
    @staticmethod
    def get(user):
        result = get_user_contacts(user)
        return {"contact": result}


@ns.route('/add_contact/<user>&<lastname>&<firstname>&<phone>&<mail>&<chxSMS>&<chxMail>&<note>', methods=['POST'])
class AddContactController(Resource):
    @staticmethod
    def post(user, lastname, firstname, phone, mail, chxSMS, chxMail, note):
        add_contact(user, lastname, firstname, phone, mail, chxSMS, chxMail, note)
        return {"response": "DONE"}


@ns.route('/delete_contact/<user>&<lastname>&<firstname>', methods=['POST'])
class DeleteContactController(Resource):
    @staticmethod
    def post(user, lastname, firstname):
        delete_contact(user, lastname, firstname)
        return {"response": "DONE"}
