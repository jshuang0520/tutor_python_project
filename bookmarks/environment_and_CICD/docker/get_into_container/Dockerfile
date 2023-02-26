FROM python:3.8-slim
ENV PROJECT_WORK_DIR /get_into_container

# update os system
RUN apt-get update && \
    apt-get install -y apt-transport-https

WORKDIR ${PROJECT_WORK_DIR}

COPY . .

RUN chmod +x ${PROJECT_WORK_DIR}/scripts/*.sh

ENTRYPOINT ["bash"]
CMD ["scripts/run_python.sh"]

##-------------------------------------------------
##notes.
##-------------------------------------------------
## method 0
#RUN chmod +x ${PROJECT_WORK_DIR}/scripts/*.sh

## method 1
# CMD ["bash", "scripts/run_python.sh"]

## method 2
# ENTRYPOINT ["bash"]
# CMD ["scripts/api_syncer.sh", "ENV_FILE_DIR"]
## sample command to run this docker
## docker run ml-etl:latest "scripts/api_syncer.sh" "develop"

##-------------------------------------------------
# build docker - sample command
## docker build -f Dockerfile -t try_python_slim:latest . --no-cache  # need the final dot "."

