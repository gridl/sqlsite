from http import HTTPStatus


class Response:
    def __init__(
        self, status=HTTPStatus.OK, headers=[], content="", content_type="text/plain"
    ):
        self.status = status
        self.headers = headers
        self.content = content
        self.content_type = content_type

    def get_status_line(self):
        return f"{self.status.value} {self.status.phrase}"

    def get_headers(self):
        headers = (
            [self.get_content_length_header()]
            + [self.get_content_type_header()]
            + self.headers
        )
        return [header for header in headers if header]

    def get_content(self):
        return [self.content.encode("utf-8")]

    def get_content_length_header(self):
        return ("Content-Length", str(len(self.content)))

    def get_content_type_header(self):
        return ("Content-Type", self.content_type)
