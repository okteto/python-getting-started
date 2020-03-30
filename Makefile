.PHONY: push
push:
	okteto build -t okteto/hello-world:python-dev --target dev .
	okteto build -t okteto/hello-world:python --target dev .
