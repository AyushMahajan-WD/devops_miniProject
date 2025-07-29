Clone the gihub repository https://github.com/DogukanUrker/FlaskBlog.git


Change the app/pyproject.toml as below:
    First add on top : [build-system]
                       requires = ["setuptools"]
                       build-backend = "setuptools.build_meta"
    At the bottom add: [tool.setuptools]
                       packages = []


In app/Settings.py chaange localhost to 0.0.0.0


Run: docker compose up