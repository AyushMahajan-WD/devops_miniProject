Added multi-stage dockerfile as well which reduce size by 17%.


Clone the gihub repository https://github.com/DogukanUrker/FlaskBlog.git


Change the app/pyproject.toml as below:
    First add on top : [build-system]
                       requires = ["setuptools"]
                       build-backend = "setuptools.build_meta"
    At the bottom add: [tool.setuptools]
                       packages = []


In app/Settings.py chaange localhost to 0.0.0.0


Run: docker compose up

To run Dockerfile.builder

In docker-compose.yml file, change below

build:
    Dockerfile: Dockerfile.build

