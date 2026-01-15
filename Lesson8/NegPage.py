import  requests


class NegPage:

    def __init__(self, base_url) -> None:
        self.base_url = base_url

    def get_projects_list(self, neg_key):
        my_headers = {}
        my_headers["Authorization"] = neg_key
        my_headers["Content-Type"] = "application/json; charset=utf-8"
        resp = requests.get(self.base_url + "/projects", headers=my_headers)
        assert resp.status_code == 401

    def create_project(self, project_new, my_headers):
        resp = requests.post(self.base_url + "/projects", json=project_new, headers=my_headers)
        assert resp.status_code == 400


    def modify_project(self, project_new, my_headers):
        project_id = requests.post(self.base_url + "/projects", json=project_new, headers=my_headers)
        resp_id = project_id.json()["id"]
        modified_project = {
            "title": "",
        }
        resp = requests.put(self.base_url + "/projects/" + resp_id, json=modified_project, headers=my_headers)
        assert resp.status_code == 400
        del_project = {
            "deleted": True,
        }
        del_resp = requests.put(self.base_url + "/projects/" + resp_id, json=del_project, headers=my_headers)
        assert del_resp.status_code == 200

    def get_project(self, project_id, my_headers):
        resp = requests.get(self.base_url + "/projects/" + project_id, headers=my_headers)
        assert resp.status_code == 404

