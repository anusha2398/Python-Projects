events_dict = {'1':'CS', '2':'Google it', '3':'Treasure Hunt'}
participant_details={}
def add_participant():
	name = input("Enter participant name:")
	event = input("Enter the serial number of event name from the following list:\n\
		1) CS\n\
		2) Google It\n\
		3) Treasure Hunt\n")
	participant_details[name] = events_dict[event]
	return participant_details

def see_participant():
	for key, value in participant_details.items():
		print(key,value, sep='-')

if __name__ == '__main__':
	add_participant()
	print(participant_details)
	see_participant()
	

	

