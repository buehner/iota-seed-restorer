# IOTA Seed Restorer

This python script may help you to restore your missing IOTA seed in the following scenario:

* You mistyped your seed at **EXACTLY ONE** of the 81 seed characters
* You know a public receive address of a transaction that has been performed (with the seed you are missing)

### How does it work?

If you mistyped exactly one (!) of 81 characters, there are `81*(27-1) = 81*26 = 2106` possibilities for your correct seed. This script makes use of the [PyOTA API](https://github.com/iotaledger/iota.lib.py) to check if the receive address (you made a transaction with) matches one or more of these 2106 seeds.

### Requirements

* [Python](https://www.python.org/downloads/) should be installed on your system
* The PyOTA and six libraries are required for the script to work:
  1. On Ubuntu-based distributions, install the `python-dev` package: `sudo apt-get install python-dev` (this will probably not be necessary on a windows system)
  2. Open a terminal, navigate to the directory of the script and call this command: `sudo pip install -r requirements.txt` (remove the `sudo` on windows)

I did not test this on windows, but it should also work there.

### Usage

Just call `python IotaSeedRestorer.py` (in a terminal in the directory of the script) and follow the instructions.

You will be asked for the following information:

1. The seed you possibly mistyped at exactly one (!) character.
2. The public receive address of a transaction you performed.
3. A node address/host to connect to with the PyOTA API. [See here](https://iota.dance/nodes).
4. You have to define how many of the first addresses of each of the 2106 seeds will be requested to find a match with the address from point 2.
  * **Large numbers will significantly increase the duration of the process!**
  * If you know that you only made one transaction (or you simply know the first address of your missing seed), use `1` as the value.
  * Be careful when increasing this number!

You can cancel the script anytime with `CTRL+C`.

If a matching seed candidate is found during the process, the seed will be printed (and the process will continue).

At the end of processing all 2106 seeds (which may take a while), there will be a summary with a list of all seeds you can try. Otherwise the script will inform you that it could not find any matching seeds.

### Donations

If this script could help you or you simply like it, feel free to send some :heart: to this address:

```
9EITUFEVHRFFFMCLLPEFPUYVCYEQZHXKXWQKIEKMUWDXPELEBZRTNYVNIKVVIJGMMQQJITQYKNTPUYAECKPOEHN9SX
```

### Credits

The script is inspired by [this balance checker](https://github.com/bahamapascal/IOTA-Balanace-Checker).
