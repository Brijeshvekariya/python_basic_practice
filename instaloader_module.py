import instaloader

name = input("Enter insta id : ")
insta = instaloader.Instaloader()


insta.download_profile(name , profile_pic_only=True)
print("Download Successfully")


# # # it will throw error
# insta.download_post(name,post=True)
# print("download Succesfully")

# insta.download_profile(name,profile_pic_only=False)
# print("Download Successfully")
# # # profile = insta.download_profile(name , download_stories_only= True)
# # # Replace 'target_username' with the username of the profile you want to access
# target_username = name

# # Get the profile of the target user
# profile = instaloader.Profile.from_username(insta.context, target_username)

# print(f"Username: {profile.username}")
# print(f"Full Name: {profile.full_name}")
# print(f"Followers: {profile.followers}")
# print(f"Followings: {profile.followees}")
# # for followers in profile.get_posts:
# #     print(followers)

# # Access
