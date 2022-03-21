# Demo API

This is a small demo api project which is intended to demonstrate EKS deployment by Github Actions.

## Prerequisites
First you need to create infrastructure in AWS which includes creating kubernetes cluster and docker registry.
You can find terraform repo [here](https://github.com/GrigoriLab/demoapi_terraform)

Now you can deploy Demo API by merging PR into `main` branch.
You can check the deployment by forwarding port to `localhost` and go to [this](http://localhost:8000/api/v1/products/) url

`kubectl port-forward deployment/demoapi-deployment 8000:8000`