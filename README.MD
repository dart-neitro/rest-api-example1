# This is broken API for testing


Clone repo 
> git clone git@github.com:dart-neitro/rest-api-example1.git

Change directory  
> cd rest-api-example1

Build image  
> docker build -t rest-api-example1 .

Run container in detached mode and publish port 5000 
> docker run -d -p 5000:5000 rest-api-example1

API should be accessible on port 5000 
Get all users
> curl -i localhost:5000/users

Get user with id 1
> curl -i localhost:5000/user/1


Add user (wrong data)
> curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://localhost:5000/user/add


Add user (correct data)
> curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"id":3,"name":"Sergey Sidorov"}' \
  http://localhost:5000/user/add