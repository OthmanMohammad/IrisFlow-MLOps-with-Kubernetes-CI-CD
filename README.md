# MLOps Project with Flask, Docker, CI/CD, and Kubernetes

This README will walk you through the steps I took to create a simple Machine Learning model, containerize it with Docker, set up a CI/CD pipeline using GitHub Actions, and deploy it on Kubernetes.

## Flask

1. **Set Up Virtual Environment**:
```bash
   python -m venv myenv
   .\myenv\Scripts\activate
  ```

1. **Install Flask:**
```bash
pip install Flask
```
2. **Create a Flask App (`app.py`): A simple app that hosts our ML model and exposes an endpoint for predictions.**
3. **Run Flask App:**
```bash
python app.py
```

## 🐳 Docker

1. **Write a Dockerfile**:
In the root directory, write a Dockerfile that provides instructions on how to containerize the Flask app.

2. **Build the Docker Image:**
   ```bash
   docker build -t iris-classifier .
   ```
   This command builds an image from the Dockerfile and tags it as iris-classifier.

3. **Run Docker Container:**
   ```bash
   docker run -p 5000:5000 iris-classifier
   ```
Here, we're running the container and mapping the host port 5000 to the container's port 5000.

## 🔄 CI/CD with GitHub Actions

1. **Set Up GitHub Secrets**:
   Store DockerHub credentials in GitHub secrets. Use `DOCKER_HUB_USERNAME` for your username and `DOCKER_HUB_ACCESS_TOKEN` for your access token.

2. **CI/CD Pipeline (`./github/workflows/main.yml`)**:
   This file configures the GitHub Actions workflow. The workflow does the following:

   - Check out the latest code.
   - Install required dependencies.
   - Log in to Docker Hub.
   - Build a new Docker image.
   - Push the Docker image to Docker Hub.

3. **Push Changes to GitHub**:
   When you make changes to the main branch and push them, the CI/CD pipeline will automatically trigger.

## 🚢 Kubernetes Deployment

1. **Install and Start Minikube**:
   Use Minikube to simulate a local Kubernetes cluster.

2. **Kubernetes Deployment Configuration (`deployment.yaml`)**:
   This file defines how the application should be deployed on Kubernetes.

3. **Deploy to Kubernetes**:
   To deploy, execute the following command:
   ```bash
   kubectl apply -f deployment.yaml
   ```

4. **Access the Deployed Application:**
    ```bash
    minikube service iris-classifier-deployment
    ```

To put it simply, the process involves packaging your application in a container using Docker. Next, you define how Kubernetes should run this container in the `deployment.yaml` file. Finally, you deploy and manage it using `kubectl` and `minikube`.
