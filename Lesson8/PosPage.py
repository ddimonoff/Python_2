import requests


class PosPage:

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_projects_list(self, my_headers):
        resp = requests.get(self.base_url + "/projects", headers=my_headers)
        body = resp.json()['paging']['count']
        assert resp.status_code == 200
        return body

    def create_project(self, project_new, my_headers):
        resp = requests.post(self.base_url + "/projects", json=project_new, headers=my_headers)
        assert resp.status_code == 201
        body = resp.json()["id"]
        return body


    def get_project(self, my_headers, project_id):
        resp = requests.get(self.base_url + "/projects/" + project_id, headers=my_headers)
        body = resp.json()["title"]
        assert resp.status_code == 200
        return body

    def modify_project(self, project_id, modified_project, my_headers):
        resp = requests.put(self.base_url + "/projects/" + project_id, json=modified_project, headers=my_headers)
        assert resp.status_code == 200

    def delete_project(self, project_id, my_headers):
        del_project = {
            "deleted": True,
        }
        resp = requests.put(self.base_url + "/projects/" + project_id, json=del_project, headers=my_headers)
        assert resp.status_code == 200
