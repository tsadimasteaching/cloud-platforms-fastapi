


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