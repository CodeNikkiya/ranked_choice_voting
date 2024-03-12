import random as rn

class voter:
	voters_ranked_choices = [] # list of candidates in order of preference
	#preference_of_eliminated_options = [] # list of candidates in order of preference that have been eliminated

class candidate:
	def __init__ (self, name):
		self.name = name
		self.is_option_nr = {} # keys are ranks the candidate can get in voting, values are percentages

number_of_votes =  (int)(input("Enter the number of voters: "))

list_of_candidates = ["Ivan", "George", "John", "Michael", "Peter", "Lora"]

for c in range (len (list_of_candidates)):
	list_of_candidates[c] = candidate(list_of_candidates[c])



total_voters = []

''' the following code is for manual input of test votes

for i in range(number_of_votes):
	v = voter()
	v.votes = input("Enter the votes of voter " + str(i+1) + ": ").split()
	while len(v.votes) > len(list_of_candidates) or  len(v.votes) == 0 or list(set(v.votes) - set(list_of_candidates)):
		if len(v.votes) > len(list_of_candidates) or  len(v.votes) == 0:
			print("Invalid number of votes. Please enter the votes again.")
		if list(set(v.votes) - set(list_of_candidates)):
			print(f"There are votes for invalid options {list(set(v.votes) - set(list_of_candidates))} Please enter the votes again.")
		v.votes = input("Enter the votes of voter " + str(i+1) + ": ").split() ##make all of this a sepaqarate function and also check if the votes are for people on the list
	total_voters.append(v)
	'''
 #test function:
def randomise_voter_input (list_of_candidates, number_of_votes) :
	votes_after_voting = []
	for i in range (number_of_votes):
		v = voter()
		her_votes = list(list_of_candidates)
		print (her_votes)
		rn.shuffle(her_votes)
		v.voters_ranked_choices = her_votes
		print(v.voters_ranked_choices)
		votes_after_voting.append(v)
	return (votes_after_voting)

total_voters = randomise_voter_input(list_of_candidates, number_of_votes)
for v in total_voters:
	for k in v.voters_ranked_choices:
		print (k.name, " ", end="")
	print("\n-------------------------")

def calculate_total_preferences(total_voters, list_of_candidates):
	for i in range (len (list_of_candidates)):
		names_for_preference = []
		for v in total_voters:
			names_for_preference.append(v.voters_ranked_choices[i].name)
		print (f"{i + 1} preferences are  {names_for_preference}")
		for c in list_of_candidates:
			c.is_option_nr[i+1] =         names_for_preference.count(c.name)/len(names_for_preference)
			print(c.name, c.is_option_nr)
			print("\n-------------------------")

calculate_total_preferences(total_voters, list_of_candidates)

lowest_candidate_of_round = ""
highest_candidate_of_round = ""





def round_of_vote_counting(total_voters, list_of_candidates):  #include individual round statistics and perhaps avoid recursion
	print (0)
def check_results(round_result):

	print(f"The results of the round are: {round_result}")
	if round_result[0] > 0.5:
		return round_result[0]
	else:
		round_result.popitem(-1)
		round_of_vote_counting(round_result)
		


#round_of_vote_counting()
