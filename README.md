This is a throw-away proof of uploading a file to a Hawk protected API
endpoint. The code will probably be broken and/or irrelevant by the time
you read this.

**The verdict is in**: As suspected, Hawk doesn't seem like a good fit
for protecting endpoints that need to receive large files.
Thoughts:

- Hawk needs to store all content data in memory to check the signature;
  no libraries specify how to stream data efficiently.
- Turning off content checks in Hawk is one way to do it but that leaves
  you vulnerable to poisoned files.
- It's probably ok to store file data in memory for most files but even so
  it's hard to get at final payload data such as multi-part boundaries.
  This means the client will have a hard time calculating a signature.

## Run the example

Run this to build and start the container(s):

    docker-compose build
    docker-compose up -d

Find your IP somehow (maybe like this):

    $ boot2docker ip
    192.168.59.103

Open the site at `http://192.168.59.103:8000/`

Run this to try uploading a file:

    docker-compose run web ./scripts/upload_with_hawk.py
