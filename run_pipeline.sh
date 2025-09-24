# export variables
echo "export variables"
source export_credentials.sh
echo "credentials successfuly exported"

# fire up postgres
echo "build postgres image.."
docker build -f Dockerfile.postgres -t postgres-image .
echo "postgres image successfully built"

# docker run --env-file .env postgres-image
echo "run postgres image..."
docker run -d --name postgres-image --env-file .env -p 5432:5432 postgres:15

# create a network for the postgres image
echo "creating network for image connection.."
docker network create etl-network
echo "network successfully created.."

# fire up etl image
echo "building python image.."
docker build -f Dockerfile.python -t etl_pipeline .
echo "python image successfully built.."

# run pipeline
echo "run data pipeline to ingest data to the database..."
docker run --env-file .env etl_pipeline

