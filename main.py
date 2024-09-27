from fastapi import FastAPI

app=FastAPI()

''' make a dummy items '''
developers=[
    {'id':1,"name":"shanzy","description":"Django backend developer"},
    {'id':2,"name":"saira","description":"React Frontend developer"},
]
# GET record
@app.get("/developers")
def get_data():
    return developers

# Create/Add new record
@app.post("/developers/add/")
def create_developers(name:str,description:str):
    new_developers={"id":len(developers)+1,"name":name,"description":description}
    developers.append(new_developers)
    return {"message":"add new developers successfully","developers":new_developers}

# UPDATE already existing developer
@app.put("/developers/{developer_id}/")
def update_developers(developer_id:int, name:str, description:str):
    for developer in developers:
        if developer["id"]==developer_id:
            developer["name"]=name
            developer["description"]=description
            return {"message":"update developers successfully","developers":developers}
    return {"message":"developers not found"}

# DELETE already existing developer
@app.delete("/developers/{developer_id}/")
def delete_developers(developer_id:int):
    for developer in developers:
        if developer["id"]==developer_id:
            developers.remove(developer)
            return {"message":"delete developers successfully","developers":developers}
    return {"message":"developers not found"}


