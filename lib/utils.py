def build_request_header(access_token, content_type="application_json"):
    header = {
        "Authorization": f"Bearer {access_token}",
        "Accept": content_type
    }
    return header
