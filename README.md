# llm-streamlit-app
## Intructions
### Must also have Python, and Docker installed.
Clone the repo to your local machine

```git clone https://github.com/bbonser/llm-streamlit-app```

Navigate to the folder where you pulled this down to and run the following command to build the Dockerfile and install the dependencies.

```docker
docker build -t llm-streamlit-app .
```
This will build the image from the Dockerfile.
Once completed run the following command to run the container.

```docker
docker run -p 8501:8501 llm-streamlit-app
```
Open a browser and navigate to http://localhost:8501

![image](https://github.com/bbonser/llm-streamlit-app/assets/26509652/114c7b91-864e-40b4-b659-a69c17b1c7d8)
