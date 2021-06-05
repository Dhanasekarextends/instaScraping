from instaloader import Instaloader, Profile, exceptions
loader = Instaloader()

target_profile = input("Enter the profile name : ")

# Return error message if there is no profile name
try:
    profile = Profile.from_username(loader.context, target_profile)
except exceptions.ProfileNotExistsException:
    print("This account does not exist")
    exit()

num_followers = profile.followers
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

# Fetch likes and comments details for first 10 posts
counter = 0
posts_to_count = 10

for post in profile.get_posts():
    if(counter >= posts_to_count):
        break
    total_num_likes += post.likes
    total_num_comments += post.comments
    total_num_posts += 1
    counter += 1

# Printing the number of followers 
print("Number of followers : ", num_followers)
