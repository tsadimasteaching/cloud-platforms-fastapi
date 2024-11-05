
## Clone repo
```bash
git clone https://github.com/tsadimasteaching/cloud-platforms-fastapi.git
```
### Create virtual Environment, activate and install requirements
```bash
python3 -m venv fapi
source fapi/bin/activate
pip install -r requirements.txt
```
### Copy .env.example to .env
```bash
cd api
cp .env.example .env
```

## run postgres as container

```bash
docker run --name cp-lab-pg --rm \
-e POSTGRES_PASSWORD=pass123 \
-e POSTGRES_USER=dbuser \
-e POSTGRES_DB=cplabdb \
-d \
-p 5432:5432 \
-v cp-lab-vol:/var/lib/postgresql/data \
postgres:16
```

### Run the app
```bash
source fapi/bin/activate
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```