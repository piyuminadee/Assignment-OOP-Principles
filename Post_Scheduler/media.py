class Post:
    def __init__(self, content, scheduled_time, platform):
       self.content = content
       self.scheduled_time = scheduled_time
       self.platform = platform
       
    def edit_content(self, new_content):
        self.content = new_content
        
    def change_scheduled_time(self, new_time):
        self.scheduled_time = new_time
        
    def __str__(self):
       return f"The post content is : {self.content} scheduled for {self.scheduled_time} on {self.platform}" 
   
class Scheduler:
    def __init__(self):
        self.posts = []
        
    def add_post(self, post):
        self.posts.append(post)
        print(f"Post added successfully") 
        self.view_all_posts()
        
    def remove_post(self, post_id):
        if 0<=post_id<len(self.posts): 
          del self.posts[post_id]
          print(f"{post_id} is deleted") 
        else: 
         print(f"{post_id} is invalied post id")    
         
    def view_all_posts(self):
        for i, post in enumerate(self.posts):
            print(f"post id {i} : {post}")
            
                      
            
    def save_posts_to_file(self, filename):
        with open(filename, "w") as file:
            for post in self.posts:
                file.write(f"post content is : {post.content} | sceduled time at {post.scheduled_time} | on {post.platform}\n")
                print(f"Post saved to {filename}")
                
    def load_posts_from_file(self, filename):
        try: 
            with open(filename, "r") as file:
                self.posts = []
                for line in file:
                    content, scheduled_time, platform = line.strip().split("|")
                    self.posts.append(Post(content, scheduled_time, platform))
                   
        except FileNotFoundError: 
            print(f"File '{filename}' not found.") 
            
            
            
scheduler = Scheduler()
scheduler.add_post(Post("Harry Potter", "3:15 PM", "Facebook"))
scheduler.save_posts_to_file("posts.txt")
scheduler.load_posts_from_file("posts.txt")
scheduler.view_all_posts()                  
              

                       