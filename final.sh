#!/bin/bash
mkdir -p bd-a1/service-result
docker cp cc192d1c389a:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp cc192d1c389a:/home/doc-bd-a1/k.txt bd-a1/service-result/
docker stop cc192d1c389a