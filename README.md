# Installation

1. Clone repository

```console
git clone https://github.com/prangel-git/legendre_pairs_py.git
cd legendre_pairs_py/ 
```

2. Create and activate a new virtual environment (you need python 3)

```console
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages from pip

```console
python -m pip install -r requirements.txt
```

4. Run tests

```console
pytest
```

5. Run test coverage

```console
coverage run -m pytest
coverage report -m 
```