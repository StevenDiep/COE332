# Homework 7
Homework 7 focuses on putting together a flask api, redis database, and a basic worker together in order to make a basic system. Spent time creating flask and worker images, pushing them to docker, and then letting the kubernetes deployments pull these images to create our pods

# Part A

1. Updated the dockerfile for the flask application and worker for our image and ultimately the kubenetes pods. Made sure that the flask and worker used environment variables for their redis service IP instead of hardcoding the IP address directly into the code.

To build the images, use 

```bin
docker build -t stevendiep/test-flask:1.0 -f Dockerfile.api .
```

```bin
docker build -t stevendiep/test-worker:1.0 -f Dockerfile.worker .
```

If we wanted to run the images, use the following commands. Although in this case the containters won't work since we have our IP addresses pointing to the redis service IP instead of the 127.0.0.1 host IP

```bin
docker run --rm -d -p 5000:5000 stevendiep/test-flask:1.0
```

```bin
docker run stevendiep/test-worker:1.0
```

2. In this part, we change the spec:spec:containers:image: and put in the image we want to pull. For the api and workers, pull their respective images we created in step one.

Then, to run the deployments use the following commands:

```bin
kubectl apply -f stevend-test-flask-deployment
```

```bin
kubectl apply -f stevend-test-worker-deployment
```

3. We now verify that the applications in the system are communicating with each other correctly. 

To use curl statements and check so, run the following command:

```bin
kubectl get services -o wide
```

This will tell us the redis_IP which we will insert to our deployments env variable for both worker and flask yml files.

We then look at the flask serivce IP, which we will use as the IP address for making our curl statements. For example purposes, we will call this <flask_service_IP>

We now need to exec into our python debug pod to check our curl statements, use the following command to do so:

```bin
kubectl exec -it <your debug pod name> -- /bin/bash
```

When you are successfully in, you should see the root prompt

Next, use the following command to see if the server is up and running:

```bin
curl <flask_service_IP>:5000/hello
```

You should see a message pop up indicating that your server is up and running


To check that we can post jobs, use:

```bin
curl <flask_service_IP>:5000/jobs -d '{"start":1100, "end":1300}'
```

You should see a message that the job is submitted

Now, to check that the job is correctly seen by the worker, copy the uid from the submission message youjust got. Use the following command

```bin 
curl <flask_service_IP>:5000/jobs/<paste uid here>
```

You should now see that the job is now in progress or completed

# Part B

1. Added the env change in the worker deployment yml file

2. In the code, we added the pod's personal IP address to the output of the complete status


# Part C

Use the same curl commands to post and check on the jobs
When you have two workers and 10 jobs posted, each worker worked on 5 jobs
