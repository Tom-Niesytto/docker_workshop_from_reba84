# docker_workshop
We are going to run a flask app in a docker container to display an image then we will load a model to do a prediction on that image in the flask app.

### Build Docker Container
“docker build” does the building of the container  
-t gives the container a name which is “python-workshop”  
: gives the container ‘tag’ so you know where it was build from  
.  this says build from the current directory  


`docker build -t python_workshop:local .`  

### Check container built  
`docker images`  

###  Run Docker container

docker run runs the container
-p maps the ports in this case localhost port 8889 to the port 5000 we exposed in our docker file   
--name is the name of our running container
python_workshop:local references our image  
--rm removes the image after we exit

`docker run -p 8889:5000 --rm --name may21 python_workshop:local`

### Run Docker Container in Interactive mode  

Checking directory structure in container  
“Docker run” still runs the container   
-i starts in interactive mode  
-t starts a terminal  
`bash` starts a shell  

`docker run -p 8889:5000 -it --rm --name may21 python_workshop:local bash`

### Train a Quick Example Model
You can train and save a model using a jupyter notebook (or other code) and then use it to do things in your flask app.

### Run Docker Container and Mount Volume

-v mounts a volume with code (or saved model files) on the docker container  
 The format is `<directory on your local>:<directory in your container>`

`docker run -p 8889:5000 -v /home/becky/workshop_model:/app/model --rm --name may21 python_workshop:local`
