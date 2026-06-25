import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL,
               )   
''')
def main():
    while True:
        print("/youtube manager with db.")
        print("1.list videos")
        print("2.add videos")
        print("3.update videos")
        print("4.delete videos")
        print("5.exit app")
        
        choice = input("enter your choice:")

        if choice == '1':
            list_videos()
            




    if __name__ == "__main__"
    main()
    