import ollama
import csv

# question1 = [{'role': 'system', 'content': "Please tell me whether there was high-energy risk present in this work site?"}]
#question2 = [{'role': 'system', 'content': "Please tell me whether there was a high-energy release present?"}]

file_input = "data.csv"
output_file="output.csv"

with open(file_input, "r") as file, open(output_file, "w") as output: 

    model = "llama3.2:3b"
    is_first = True
    reader = csv.reader(file)
    writer = csv.writer(output)
    # row_num = 1
    
    for row in reader:
        context = [{
            "role": "system",  # Base context as the system message
            "content": """You are a data analyst working for an electrical company who classifies high-energy incidents.

            The following 13 sentences are examples of high-energy situations (which are high-energy incidents):
            - Employee was in line of fire while crane was moving load.
            - Member successfully lowered from elevated position while cutting down tree.
            - During road inspection, crew members were within 5 feet of the highway
            - On the way to the job site, the team was travelled in a pickup truck going 50 mph.
            - The crew was performing routine maintenance within the vicinity of a running turbine.
            - The job site was an operation metal foundry with the crew working near molten metal.
            - Hot steam leaks occurred while on the job site.
            - One work vehicle caught fire while in proximity to several crew members.
            - A battery that was being worked on by a member exploded.
            - The team was required to dig a 7 foot deep trench for the installation project.
            - A crew member had to ascend the transformer to perform maintenence.
            - While inspecting a circuit breaker, an arc flash was incited.
            - Member came into contact with toxic chemicals by accident.
            - The crew member is 4 feet or more off the ground.
            
            The energy variety to consider in the following case is temperature, gravity, motion, 
            mechanical, electrical, pressure, sound, radiation, biological and chemical."""
        }, {
            "role": "user",
            "content": f"""So, given a situation with description: "{row[4]}" and incident information: "{row[3]}".
            Is this a high-energy situation?Please answer yes or no."""
        }]
        
        count = 0
        total_runs = 5
        yes = False
        if not is_first:
            for _ in range(total_runs):
                response_q = ollama.chat(model=model, messages=context)
                if "yes" in response_q['message']['content'].lower() or "probably" in response_q['message']['content'].lower():
                    count += 1
            yes = count / total_runs >= .5

        if is_first:
            writer.writerow(["High Energy","Comment","Description"])
            is_first = False
        else:
            writer.writerow([str(yes), row[3], row[4]])
            #output.write(f'"{str(yes)}","{row[3]}","{row[4]}"\n')
