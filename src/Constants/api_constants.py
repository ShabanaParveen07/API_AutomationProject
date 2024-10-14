#API Constants - class which contains all the endpoint
# keep the URL

class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"


    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    # Update -> PUT, PATCH, DELETE - bookingId
    def url_patch_put_del(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str("booking_id")

