# python-ssv
Proof of concept of an Eth2 secret shared validator node

# Requirements

 * Python 3.8. Use `venv.sh` to create a virtualenv with the required packages.
 * `python-ibft`: https://github.com/dankrad/python-ibft
 * Prysm beacon node and validator client, adapted for SSV node: `https://github.com/alonmuroch/ethereumapis/tree/feature/ssv`
 * `tmux` for demo scripts

# Usage

 * You can split a validator private key into the threshold keys using `privkey_to_threshold.py`.
 * Then use `run.sh` to run all the SSV nodes in one tmux window
 * `run_validators.sh` needs to be copied into the `validator` directory of the prysm SSV node. Running it will launch the 4 VCs to connect to the SSV nodes in a tmux window