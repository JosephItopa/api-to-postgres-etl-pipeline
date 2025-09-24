# export variables
echo "export variables"

# run pipeline
echo "running data pipeline"

docker run --env-file .env etl_pipeline
