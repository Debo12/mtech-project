from services.company_service import CompanyService

class CompanyController:
    def __init__(self) -> None:
        self.company_service = CompanyService()

    def companies_response(self, method, args, request_body_data):
        if method == "GET":
            if args is None:
                return self.company_service.get_all_companies()
            return self.company_service.get_companies_by_params(args)
        elif method == "POST":
            return self.company_service.insert_company(request_body_data)
        elif method == "PUT":
            return self.company_service.update_company(args, request_body_data)
        elif method == "DELETE":
            return self.company_service.delete_company(args)
