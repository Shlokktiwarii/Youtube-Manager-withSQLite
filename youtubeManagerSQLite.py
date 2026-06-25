import sqlite3
conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )   
''')
def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
      print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name ,time) VALUES(?,?)", (name,time))
    cursor.commit()

def update_video(name,time,video_id):
    cursor.execute("UPDATE videos SET name = ? time = ? WHERE id = ? ",(name,time,video_id))
    cursor.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ? ",(video_id,))
    cursor.commit()


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
            list_video()
        elif choice == '2':
            name = input ("enter the name:")
            time = input("enter the time:")
            add_video(name,time)
        elif choice == '3':
            name = input ("enter the name:")
            time = input("enter the time:")
            video_id = ("enter video id:")
            update_video(name,time,video_id)
        elif choice == '4':
            video_id = input("Enter video id to delete:")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")


        conn.close()





if __name__ == "__main__":
  main()
    