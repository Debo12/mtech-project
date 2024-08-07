from services.complaint_service import ComplaintService

class ComplaintController:
    def __init__(self) -> None:
        self.complaint_service = ComplaintService()

    def complaint_response(self, method, args, request_body_data):
        if method == "GET":
            if args is None:
                return self.complaint_service.get_all_complaint()
            return self.complaint_service.get_complaint_by_params(args)
        elif method == "POST":
            return self.complaint_service.insert_complaint(request_body_data)
        elif method == "PUT":
            return self.complaint_service.update_complaint(args, request_body_data)
        elif method == "DELETE":
            return self.complaint_service.delete_complaint(args)
