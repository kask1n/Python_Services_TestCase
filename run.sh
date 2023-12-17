#!/bin/bash

touch ~/{cliapi_client.log,bgproc_data.txt}
chmod +x ~/{cliapi_client.log,bgproc_data.txt}

docker-compose up
