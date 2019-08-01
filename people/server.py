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

seed_layout = ['Tasks','Word','Excel','PPT','Admin','Mail','Cal','Ppl','News','Drive','Sites','Notes']
e_weights = {'Tasks':0.1,'Word':0.2,'Excel':0.15,'PPT':0.2,'Admin':0.05,'Mail':0.5,'Cal':0.4,'Ppl':0.4,'News':0.4,'Drive':0.2,'Sites':0.01, 'Notes':0.05}
associations = {'WordExcel':0.5,'WordPPT':0.5,'MailCal':0.3,'PplCal':0.3,'TasksCal':0.2,'NotesTasks': 0.3}
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

def random_search(max_iters, *args):
    columns = args[1] # Number of columns in this layout (=1) 
    obj_f = args[2]   # Handle to the objective function (=linear_ST)
    o_inputs = args[3:] # Arguments simply passed on to the objective function
    incumbent = args[0] # Best-known design thus far
    incumbent_ov = obj_f(incumbent, columns, o_inputs) # Set initial objective value

    for iter in range (0, max_iters):
        # TASK: FIX THE NEXT LINE
        # candidate = incumbent # this is wrong
        candidate = random.sample(incumbent, len(incumbent))
        candidate_ov = obj_f(candidate, columns, o_inputs) # Then compute its objective value

        if candidate_ov < incumbent_ov: # Update best known if an improvement was found
            incumbent = candidate[:]
            incumbent_ov = candidate_ov
    return incumbent, incumbent_ov

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




@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 

@app.route('/people')
def people(name=None):
    return render_template('people.html', data=data)  
  
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
 


@app.route('/emoji')
def emoji():
    winner, winner_score = optimize(3000, random_search, seed_layout, columns, ST_and_myO, e_weights, associations)
    print(winner)
    return jsonify(winner = winner)



if __name__ == '__main__':
   app.run(debug = True)

