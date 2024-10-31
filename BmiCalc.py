from fastapi import FastAPI,Query
app=FastAPI()


@app.get("/")
def Hi():
    return {"message" :"maroc"}

@app.get("/calculate_bmi")
def calculat_bmi(
    weight:float=Query(...,gt=20,lt=200,description="le poid en KG"),
    height:float=Query(...,gt=1,lt=3,description="longeur en m")):
    bmi=weight/(height**2)
    if bmi<18.5:
        message="nahif"
    elif 18.5<=bmi<25:
        message="moyen"
    elif 25<=bmi<30:
        message="samin"
    else:
        message="see doctor"

    return {
        "your bmi ":bmi,
        "advice":message
        }

@app.get("/comptau")
def comptabilite(
    compte_d:str=Query(...,description="le poid en KG"),
    compte_c:str=Query(...,description="longeur en m"),
    montant_d:str=Query(...,description="longeur en m"),
    montant_c:str=Query(...,description="longeur en m")):

    if compte_d=="6111" and compte_c=="4411" and montant_d=="6000" and montant_c=="6000":
        return "good answer"
    else:
        return "bad answer"
    

    