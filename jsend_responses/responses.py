from django.http import JsonResponse


class SuccessResponse(JsonResponse):
    status = 'success'

    def __init__(self, object, status_code=200):
        data = {
            'status': self.status,
            'data': {
                'object': object,
            }
        }
        super().__init__(data=data, status=status_code)


class SuccessListResponse(JsonResponse):
    status = 'success'

    def __init__(self, objects, pagination=None):
        data = {
            'status': self.status,
            'data': {
                'objects': objects,
                'pagination': pagination,
            }
        }
        super().__init__(data=data)


class FailResponse(JsonResponse):
    status = 'fail'

    def __init__(self, message='', status_code=404, details=None):
        data = {
            'status': self.status,
            'data': {
                'message': message,
                'details': details or []
            }
        }
        super().__init__(data=data, status=status_code)


class ErrorResponse(JsonResponse):
    status = 'error'

    def __init__(self, message, status_code=400, error_code=None, data=None):
        data = {
            'status': self.status,
            'code': error_code,
            'message': message,
            'data': data,
        }
        super().__init__(data=data, status=status_code)
