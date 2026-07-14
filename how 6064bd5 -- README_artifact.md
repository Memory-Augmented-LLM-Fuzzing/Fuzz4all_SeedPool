[33mcommit 6064bd504a477e4929bfdca277fbdd62f58b6b8c[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m)[m
Author: Yapeng Zhang <729249339@qq.com>
Date:   Tue Jul 14 20:59:51 2026 +0200

    First Commit

[1mdiff --git a/.gitignore b/.gitignore[m
[1mnew file mode 100644[m
[1mindex 0000000..87db773[m
[1m--- /dev/null[m
[1m+++ b/.gitignore[m
[36m@@ -0,0 +1,171 @@[m
[32m+[m[32m# Byte-compiled / optimized / DLL files[m
[32m+[m[32m__pycache__/[m
[32m+[m[32m*.py[cod][m
[32m+[m[32m*$py.class[m
[32m+[m
[32m+[m[32m# C extensions[m
[32m+[m[32m*.so[m
[32m+[m
[32m+[m[32m# Distribution / packaging[m
[32m+[m[32m.Python[m
[32m+[m[32mbuild/[m
[32m+[m[32mdevelop-eggs/[m
[32m+[m[32mdist/[m
[32m+[m[32mdownloads/[m
[32m+[m[32meggs/[m
[32m+[m[32m.eggs/[m
[32m+[m[32mlib/[m
[32m+[m[32mlib64/[m
[32m+[m[32mparts/[m
[32m+[m[32msdist/[m
[32m+[m[32mvar/[m
[32m+[m[32mwheels/[m
[32m+[m[32mshare/python-wheels/[m
[32m+[m[32m*.egg-info/[m
[32m+[m[32m.installed.cfg[m
[32m+[m[32m*.egg[m
[32m+[m[32mMANIFEST[m
[32m+[m
[32m+[m[32m# PyInstaller[m
[32m+[m[32m#  Usually these files are written by a python script from a template[m
[32m+[m[32m#  before PyInstaller builds the exe, so as to inject date/other infos into it.[m
[32m+[m[32m*.manifest[m
[32m+[m[32m*.spec[m
[32m+[m
[32m+[m[32m# Installer logs[m
[32m+[m[32mpip-log.txt[m
[32m+[m[32mpip-delete-this-directory.txt[m
[32m+[m
[32m+[m[32m# Unit test / coverage reports[m
[32m+[m[32mhtmlcov/[m
[32m+[m[32m.tox/[m
[32m+[m[32m.nox/[m
[32m+[m[32m.coverage[m
[32m+[m[32m.coverage.*[m
[32m+[m[32m.cache[m
[32m+[m[32mnosetests.xml[m
[32m+[m[32mcoverage.xml[m
[32m+[m[32m*.cover[m
[32m+[m[32m*.py,cover[m
[32m+[m[32m.hypothesis/[m
[32m+[m[32m.pytest_cache/[m
[32m+[m[32mcover/[m
[32m+[m
[32m+[m[32m# Translations[m
[32m+[m[32m*.mo[m
[32m+[m[32m*.pot[m
[32m+[m
[32m+[m[32m# Django stuff:[m
[32m+[m[32m*.log[m
[32m+[m[32mlocal_settings.py[m
[32m+[m[32mdb.sqlite3[m
[32m+[m[32mdb.sqlite3-journal[m
[32m+[m
[32m+[m[32m# Flask stuff:[m
[32m+[m[32minstance/[m
[32m+[m[32m.webassets-cache[m
[32m+[m
[32m+[m[32m# Scrapy stuff:[m
[32m+[m[32m.scrapy[m
[32m+[m
[32m+[m[32m# Sphinx documentation[m
[32m+[m[32mdocs/_build/[m
[32m+[m
[32m+[m[32m# PyBuilder[m
[32m+[m[32m.pybuilder/[m
[32m+[m[32mtarget/[m
[32m+[m
[32m+[m[32m# Jupyter Notebook[m
[32m+[m[32m.ipynb_checkpoints[m
[32m+[m
[32m+[m[32m# IPython[m
[32m+[m[32mprofile_default/[m
[32m+[m[32mipython_config.py[m
[32m+[m
[32m+[m[32m# pyenv[m
[32m+[m[32m#   For a library or package, you might want to ignore these files since the code is[m
[32m+[m[32m#   intended to run in multiple environments; otherwise, check them in:[m
[32m+[m[32m# .python-version[m
[32m+[m
[32m+[m[32m# pipenv[m
[32m+[m[32m#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.[m
[32m+[m[32m#   However, in case of collaboration, if having platform-specific dependencies or dependencies[m
[32m+[m[32m#   having no cross-platform support, pipenv may install dependencies that don't work, or not[m
[32m+[m[32m#   install all needed dependencies.[m
[32m+[m[32m#Pipfile.lock[m
[32m+[m
[32m+[m[32m# poetry[m
[32m+[m[32m#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.[m
[32m+[m[32m#   This is especially recommended for binary packages to ensure reproducibility, and is more[m
[32m+[m[32m#   commonly ignored for libraries.[m
[32m+[m[32m#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control[m
[32m+[m[32m#poetry.lock[m
[32m+[m
[32m+[m[32m# pdm[m
[32m+[m[32m#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.[m
[32m+[m[32m#pdm.lock[m
[32m+[m[32m#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it[m
[32m+[m[32m#   in version control.[m
[32m+[m[32m#   https://pdm.fming.dev/#use-with-ide[m
[32m+[m[32m.pdm.toml[m
[32m+[m
[32m+[m[32m# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm[m
[32m+[m[32m__pypackages__/[m
[32m+[m
[32m+[m[32m# Celery stuff[m
[32m+[m[32mcelerybeat-schedule[m
[32m+[m[32mcelerybeat.pid[m
[32m+[m
[32m+[m[32m# SageMath parsed files[m
[32m+[m[32m*.sage.py[m
[32m+[m
[32m+[m[32m# Environments[m
[32m+[m[32m.env[m
[32m+[m[32m.venv[m
[32m+[m[32menv/[m
[32m+[m[32mvenv/[m
[32m+[m[32mENV/[m
[32m+[m[32menv.bak/[m
[32m+[m[32mvenv.bak/[m
[32m+[m
[32m+[m[32m# Spyder project settings[m
[32m+[m[32m.spyderproject[m
[32m+[m[32m.spyproject[m
[32m+[m
[32m+[m[32m# Rope project settings[m
[32m+[m[32m.ropeproject[m
[32m+[m
[32m+[m[32m# mkdocs documentation[m
[32m+[m[32m/site[m
[32m+[m
[32m+[m[32m# mypy[m
[32m+[m[32m.mypy_cache/[m
[32m+[m[32m.dmypy.json[m
[32m+[m[32mdmypy.json[m
[32m+[m
[32m+[m[32m# Pyre type checker[m
[32m+[m[32m.pyre/[m
[32m+[m
[32m+[m[32m# pytype static type analyzer[m
[32m+[m[32m.pytype/[m
[32m+[m
[32m+[m[32m# Cython debug symbols[m
[32m+[m[32mcython_debug/[m
[32m+[m
[32m+[m[32m# PyCharm[m
[32m+[m[32m#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can[m
[32m+[m[32m#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore[m
[32m+[m[32m#  and can be added to the global gitignore or merged into this file.  For a more nuclear[m
[32m+[m[32m#  option (not recommended) you can uncomment the following to ignore the entire idea folder.[m
[32m+[m[32m#  nuclear option because steven uses PyCharm.[m
[32m+[m[32m.idea/[m
[32m+[m
[32m+[m[32m# some project specific stuff[m
[32m+[m[32moutputs/[m
[32m+[m
[32m+[m[32m# data files[m
[32m+[m[32m*.jsonl[m
[32m+[m[32m*.json[m
[32m+[m
[32m+[m[32m# Jupyter Notebooks[m
[32m+[m[32m*.ipynb[m
[1mdiff --git a/.pre-commit-config.yaml b/.pre-commit-config.yaml[m
[1mnew file mode 100644[m
[1mindex 0000000..5b1474d[m
[1m--- /dev/null[m
[1m+++ b/.pre-commit-config.yaml[m
[36m@@ -0,0 +1,23 @@[m
[32m+[m[32mrepos:[m
[32m+[m[32m-   repo: https://github.com/pycqa/isort[m
[32m+[m[32m    rev: 5.12.0[m
[32m+[m[32m    hooks:[m
[32m+[m[32m    -   id: isort[m
[32m+[m[32m        name: isort (python)[m
[32m+[m[32m        args: ["--profile", "black"][m
[32m+[m[32m-   repo: https://github.com/psf/black[m
[32m+[m[32m    rev: 22.6.0[m
[32m+[m[32m    hooks:[m
[32m+[m[32m    -   id: black[m
[32m+[m[32m-   repo: https://github.com/pre-commit/pre-commit-hooks[m
[32m+[m[32m    rev: v4.3.0[m
[32m+[m[32m    hooks:[m
[32m+[m[32m    -   id: check-yaml[m
[32m+[m[32m    -   id: end-of-file-fixer[m
[32m+[m[32m    -   id: trailing-whitespace[m
[32m+[m[32mexclude: |[m
[32m+[m[32m    (?x)^([m
[32m+[m[32m        README.*|[m
[32m+[m[32m        config/.*|[m
[32m+[m[32m        bugs/.*|[m
[32m+[m[32m    )$[m
[1mdiff --git a/Fuzz4All/__init__.py b/Fuzz4All/__init__.py[m
[1mnew file mode 100644[m
[1mindex 0000000..e69de29[m
[1mdiff --git a/Fuzz4All/coverage_history.py b/Fuzz4All/coverage_history.py[m
[1mnew file mode 100644[m
[1mindex 0000000..769736c[m
[1m--- /dev/null[m
[1m+++ b/Fuzz4All/coverage_history.py[m
[36m@@ -0,0 +1,156 @@[m
[32m+[m[32m"""Coverage history tracking and delta calculation."""[m
[32m+[m
[32m+[m[32mfrom typing import Dict, List, Tuple[m
[32m+[m[32mfrom Fuzz4All.edge_detector import EdgeDetector, RareEdge[m
[32m+[m
[32m+[m
[32m+[m[32mclass CoverageHistory:[m
[32m+[m[32m    """Maintains coverage history and calculates coverage deltas."""[m
[32m+[m
[32m+[m[32m    def __init__(self, target_files: List[str], max_history: int = 50):[m
[32m+[m[32m        """[m
[