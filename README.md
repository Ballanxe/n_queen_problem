# N Queens Problem

OOP aproach to the n queen problems using brute force and backtracking and adding persistency

## Getting Started 

This project assumes you have docker installed on your machine. 

### Step 1 

Create a docker image 

```
$ docker build -t n-queens .
```

### Step 2 

Create a docker container

```
docker run -it n-queens
```

## Runinng Tests

### Step 1 

Start the container 

```
$ docker start n-queens
``` 

### Step 2

Create a interactive mode

```
$ docker exec -it n-queens bash
```

### Step 3

Run pytest

```
$ pytest
```