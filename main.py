import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it

data = fetch_movielens(min_rating=4.0)

#creates an interaction matrix from CSV file and stores it in a data variable as dictionary

#print training and testing data

print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss='warp')	#Weighted approximate-rank pairwise

#train model
model.fit(data['train'],epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

	#number of users and movies in training data
	n_users, n_items = data['train'].shape

	#generate recommendations for each user we input
	for user_id in user_ids:

		#movies they already like 
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

		#movies our model predicts users will like
		scores = model.predict(user_id, np.arange(n_items))
		#rank movies from most liked to least
		top_items = data['item_labels'][np.argsort(-scores)]

		#print results
		print("User %s" %user_id)
		print("		Known Positives:")

		for x in known_positives[:5]:
			print("				%s" % x)

		print("		Recommended:")

		for i in top_items[:5]:
			print("				%s" % i)

sample_recommendation(model, data, [2, 3, 23, 35, 450, 685])



