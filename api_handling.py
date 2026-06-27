import requests

def game_of_thrones():
    url = "https://anapioficeandfire.com/api/characters/583"
    response =  requests.get(url)
    data =  response.json()  

    
    name  = data["name"]
    culture = data["culture"]
    gender = data["gender"]
    born =  data["born"]
    return name,culture,gender,born 

def main():
    try:
       name ,  culture , born , gender = game_of_thrones()

       print("NAME:",name)
       print("CULTURE:",culture)
       print("GENDER:",gender)
       print("BORN:",born)
    except Exception as e:
        print(str(e))
if __name__ == "__main__":
    main()
     
        


