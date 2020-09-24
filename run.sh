#!/bin/bash

tmux \
  new-session  "python ssv_node.py 0 --port 50051; read" \; \
  split-window "python ssv_node.py 1 --port 50052; read" \; \
  split-window "python ssv_node.py 2 --port 50053; read" \; \
  split-window "python ssv_node.py 3 --port 50054; read" \; \
  split-window "bash wait.sh" \; \
  select-layout tiled
