#!/bin/bash

# Example script to run validator clients in one windows using tmux
# Copy this into the validator directory of prysm repo

tmux \
  new-session  "./validator --beacon-rpc-provider=:50051 --ssv-mode=true --disable-accounts-v2 --unencrypted-keys=threshold_key_0.json --datadir val0; read" \; \
  split-window "./validator --beacon-rpc-provider=:50052 --ssv-mode=true --disable-accounts-v2 --unencrypted-keys=threshold_key_1.json --datadir val1; read" \; \
  split-window "./validator --beacon-rpc-provider=:50053 --ssv-mode=true --disable-accounts-v2 --unencrypted-keys=threshold_key_2.json --datadir val2; read" \; \
  split-window "./validator --beacon-rpc-provider=:50054 --ssv-mode=true --disable-accounts-v2 --unencrypted-keys=threshold_key_3.json --datadir val3; read" \; \
  split-window "bash wait.sh" \; \
  select-layout tiled
