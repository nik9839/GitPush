from flask import Flask, current_app
import git, os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/createOrg')
def create_org():
    path = current_app.root_path
    if not os.path.isdir(path + "/HDoc"):  # change the name with your repo name
        git.Git(path + "/").clone("git://github.com/nik9839/HDoc.git")  # change the clone remote with your remote
    repo = git.Repo(path + "/HDoc", search_parent_directories=True)  # change the name with your repo name
    # ADD your file in the required directory
    repo.git.add(path + "/HDoc/Content/7.txt")  # modify the path with your file path
    repo.git.commit("-m \"my commit description\"")
    repo.git.push("git@github.com:nik9839/HDoc.git")  # change the remote with your remote
    return 'Hello!'


if __name__ == '__main__':
    app.run()
