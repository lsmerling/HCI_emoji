from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import math, random
app = Flask(__name__)

current_id = 2
data = [
    {
        "id": 1,
        "name": "michael scott"
    },
    {
        "id": 2,
        "name": "jim halpert"
    },
]

EmojiData = [
	{
		"id": "thumbsup",
		"image": "👍"
	},
	{
		"id": "grinning",
		"image": "😀"
	},
	{
		"id": "heart_eyes",
		"image": "😍"
	},
	{
		"id": "kissing_heart",
		"image": "😘"
	},
	{
		"id": "laughing",
		"image": "😆"
	},
	{
		"id": "stuck_out_tongue_winking_eye",
		"image": "😜"
	},
	{
		"id": "sweat_smile",
		"image": "😅"
	},
	{
		"id": "joy",
		"image": "😂"
	},
	{
		"id": "scream",
		"image": "😱"
	},
]

seed_layout = ['thumbsup','grinning','heart_eyes','kissing_heart','laughing','stuck_out_tongue_winking_eye','sweat_smile','joy','scream']
e_weights = {'thumbsup':0.2,'grinning':0.19,'heart_eyes':0.18,'kissing_heart':0.17,'laughing':0.16,'stuck_out_tongue_winking_eye':0.15,'sweat_smile':0.14,'joy':0.13,'scream':0.12}
associations = {'thumbsupkissing_heart':0.2,'sweat_smilejoy':0.3,'laughingsweat_smile':0.2}
winner = {}
winner_score = {}
columns = 6

def distance (columns, i, j):
    return math.sqrt( abs(j / columns - i / columns)**2 + abs( i % columns - j % columns)**2) 

def linear_ST (layout, columns, o_inputs):
    ST = 0.0
    reading_cost = 0.4 # assumed that scanning a single item takes 400 ms
    for i,element in enumerate(layout):
        ST += o_inputs[0][layout[i]] * distance(columns,0,i) * reading_cost
    return ST

def optimize (iters, solver, *args):
    return solver(iters, *args)

def ST_and_myO (layout, columns, o_inputs):
    return linear_ST (layout,columns,o_inputs[0:]) + 0.5 * myObjective (layout,columns,o_inputs[1:])

def myObjective (layout, columns, o_inputs):
    ov = 0.0
    for i in range(0, len(layout)):
        for j in range(i+1, len(layout)):
            # association score: highest value in dict associations or 0.0
            association = max(value for value in [0.0,o_inputs[0].get(layout[i]+layout[j]), o_inputs[0].get(layout[j] + layout[i])] if value is not None)
            ov += distance(columns, i, j) * association
    return ov

# Returns a neighbor of a given layout (list);
# Has a parameter 'n' to control distance in the neighborhood (optional)
def neighbor(layout, n=1):
    for m in range(0, n):
        i = random.randrange(0,len(layout))
        j = random.randrange(0,len(layout))
        layout[i], layout[j] = layout[j], layout[i]

    return layout

# Solver: Simulated annealing using exponential cooling schedule
def anneal(k_max, *args):
    s = args[0] # solution seed
    columns = args[1]
    obj_f = args[2]
    o_inputs = args[3:]
    s_ov = obj_f(s, columns, o_inputs)
    T_min, T_initial, alpha = 0.0000001, 10000, 0.991 # Hyperparameters
    converged = False
    
    for k in range (0, k_max):
        T = max(T_min, T_initial * math.pow(alpha,k)) # exponential cooling schedule
        s_new = neighbor(s[:], args[-1])
        s_new_ov = obj_f(s_new, columns, o_inputs)
        
        delta = s_new_ov - s_ov
        if delta < 0: # accept the neighbor if it is better
            s = s_new[:]
            s_ov = s_new_ov
        elif random.random() < math.exp(-delta/T): # if not, decide according to the Metropolis rule
            s = s_new[:]
            s_ov = s_new_ov
    return s, s_ov


@app.route('/')
def hello_world():
   return seed_layout

@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)

@app.route('/gettext', methods=['GET', 'POST'])
def gettext():
	global EmojiData

	json_data = request.get_json()
	rawdata = json_data["rawdata"].split(',')

	for i in range(0,len(rawdata)):
		e_weights[rawdata[i]] += 1
		
		if i < rawdata - 1:
			try:
				associations[rawdata[i]+rawdata[i+1]] += 1
			except:
				associations[rawdata[i]+rawdata[i+1]] = 1

	winner, winner_score = optimize(10000, anneal, seed_layout, columns, ST_and_myO, e_weights, associations, 1)
    print(winner)

	return jsonify(winner = winner)

if __name__ == '__main__':
   app.run(debug = True)