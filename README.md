#  Hello World FastAPI application instrumented with AWS Distro for Open Telemetry and deployed in ECS

##  Steps
  1. Install aws-opentelemetry-distro package:
     ```
     pip install aws-opentelemetry-distro
     ```
  2. The application must be started using the opentelemetry-instrument wrapper (ENV variables can be referred here or omitted and set them from the ECS task definition):
     ```
      OTEL_PYTHON_DISTRO="aws_distro" \
	    OTEL_PYTHON_CONFIGURATOR="aws_configurator" \
	    opentelemetry-instrument python ./path/to/your/app.py
     ```
