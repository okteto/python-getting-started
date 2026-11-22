# Getting Started with Okteto and Python

This sample shows how to build, deploy, test, and develop a Python application on Kubernetes with [Okteto](https://www.okteto.com). The application is a hello world service: its page shows a message, the Python version, and the pod that serves it.

![The page of the sample: the Okteto logo, the message, the Python version, and the name of the pod](images/hello-world.png)

Okteto builds its application and development images from the `Dockerfile`, deploys it with `kubectl`, runs its unit tests in the cluster, and replaces it with a Development Container that has hot reload and a debugger.

Follow the [Okteto with Python](https://www.okteto.com/docs/development/containers/python/) guide.
