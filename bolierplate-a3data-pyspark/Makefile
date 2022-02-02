PY_MODULES=app tests
DOCKER_REGISTRY=carlosbpy
IMAGE_NAME=spark-py
IMAGE_TAG=latest
DOCKER_WORKDIR=/tmp
DOCKER_ARGS=-v $(PWD):$(DOCKER_WORKDIR) -w $(DOCKER_WORKDIR) -u root 

#----------- Tests -------------------------------------------------------------
test-unit:
	pytest -vvv -rf -q --cov \
		--cov-report term \
		$(PY_MODULES) \
		$(PYTESTFLAGS)
		
test-docker:
	docker run --rm \
	  ${DOCKER_ARGS} \
	  ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
	  make test-unit 
#------------ PACKAGING  -------------------------------------------------------
package:
	./docker/script/package_zip.sh 
#------------ RUN/DEBUG  -------------------------------------------------------
run:
	spark-submit \
	--py-files app.zip \
	app/cli.py
#------------ DOCKER -----------------------------------------------------------
build-docker: ### Build the docker image
	docker build .\
	  -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
	  -f docker/dev.Dockerfile
#------------ MISC -----------------------------------------------------------
install-py-deps:
	poetry config virtualenvs.create false && poetry install
