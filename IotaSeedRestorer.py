from six import moves
from iota import Iota
import sys
import string

# get user input
mistypedSeed = moves.input("\nPlease enter the seed you possibly mistyped at EXACTLY ONE character:\n").upper()
publicTransactionAddress = moves.input("\nPlease enter the public receive address of a transaction you performed:\n").upper()
iotaNode = moves.input("\nPlease enter a node address/host to connect to (something like http://{HOST}:14265):\n")
numberOfAddresses = int(moves.input("\nHow many of the first addresses of a seed do you want to check? (Large numbers will significantly increase the duration of the process!)\n"))

# build the iota seed alphabet
seedAlphabet = list(string.ascii_uppercase) # A-Z
seedAlphabet.append("9")

# a list for "correct" seed candidates
seedCandidates = list()

# just a helper ;-)
def printDonation():
	print "\nIf this script could help you to get your IOTAs back, feel free to send some love to the following address:\n"
	print "9EITUFEVHRFFFMCLLPEFPUYVCYEQZHXKXWQKIEKMUWDXPELEBZRTNYVNIKVVIJGMMQQJITQYKNTPUYAECKPOEHN9SX"
	print ""

# This will generate all 81*26=2106 alternative seeds when mistyping a seed at EXACTLY ONE character
def generateSeeds():
	altSeeds = list()

	for i in range(0, 81):
		currentChar = mistypedSeed[i]

		# build all possible other chars that may come from mistyping
		altChars = list(seedAlphabet)
		altChars.remove(currentChar)

		for j in range(len(altChars)):
			altChar = altChars[j]
			altSeedCharList = list(mistypedSeed)
			altSeedCharList[i] = altChar
			altSeed = "".join(altSeedCharList)
			altSeeds.append(altSeed)

	return altSeeds

# Takes a list of seeds and calls the checkAddresses function for each seed
def checkSeeds(seeds):
	nrOfSeeds = len(seeds)
	i = 0
	while i <= nrOfSeeds - 1:
		seed = seeds[i].strip()
		if seed:
			print("Checking seed " + str(i + 1) + " of " + str(nrOfSeeds))
			checkAddresses(seed)
		i += 1
	else:
		if len(seedCandidates) > 0:
			seedCandidates.reverse()
			print "\n###############"
			print "### SUMMARY ###"
			print "###############\n"
			print "One of the following seeds could be the one that you were missing."
			print "Please check their balances manually:\n"

			print("\n".join(seedCandidates))

			printDonation()
		else:
			print ("\nSorry, but the script has finished and could not find your seed :-(\n")
		sys.exit()


# Generates addresses for a seed and checks if one of them matches
def checkAddresses(seed):
	# use IOTA api to get first n addresses of the seed
	api = Iota(iotaNode, seed)
	apiAdresses = api.get_new_addresses(count=numberOfAddresses)
	addresses = apiAdresses['addresses']

	# check if one of the addresses matches the public known transaction address
	i = 0
	while i < numberOfAddresses:
		address = str([addresses[i]][0].with_valid_checksum())
		if(publicTransactionAddress.startswith(address)):
			if(numberOfAddresses == 1):
				print "\nAs we only checked one (i.e. the first) address of a seed, there can only be one result."
				print "Please try to login with the following seed and check your balance:\n\n" + seed + "\n"
				printDonation()
				sys.exit()
			else:
				print "\nTry to login with this seed (others may follow): " + seed + "\n"
				seedCandidates.append(seed)
		i += 1

# run the script...
# start with generation of 2106 seeds
seeds = generateSeeds();

# some info
print ("\nDepending on the number of addresses you passed above, this may take a while (up to hours).")
print ("Trying another host/node may increase the speed of the process.\n")
print ("If there is a possible key, then you will be notified during the process.")
print ("At the end you will get a summary with all possible seeds (if there are any)\n")

print ("Starting to check a total of " + str(numberOfAddresses * len(seeds)) + " addresses for " + str(len(seeds)) + " seeds now...\n")
print ("To cancel, press CTRL+C!\n")

# check the seeds and its addresses
checkSeeds(seeds)
