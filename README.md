### Scraping
- I began by obtaining a sample request from users and their repositories, which helped refine my script. Discovering 475 users in Austin with over 100 followers led to five API requests (pages 1 to 5). I implemented a cached_get function, inspired by Anand sir, which improved efficiency and saved time. Despite some encoding errors due to special characters in bios, the caching feature allowed me to resume progress easily. I then used the users' logins to scrape their repositories. 
    - I didn't use asynchronous requests because of the rate limit of github API, but also I didn't add delay in my requests and somehow I didn't excede any limit.
    - I also tried graphql API it was easier to work with but due to rate limit it didn't quite work for me.
    - The cache generated were 200+ MB in size which was suprising, I thought json files would be smaller.

### After analysis
- The most intresting thing that I found was that having most repositories doesn't necessarily mean having many followers. THe most followed accounts had small number of repositories. and the most repositories accounts had less comparatively.
- Hireable users have more repositories. Meaning, you are likely an open source developer or freelance developer.
    - Project and wiki are highly correleted, and this makes sense, if you are enabling one you are more likely to enable the other.
### Action
- Working on niche programming languages can boost your repository's popularity due to less competition, unique solutions, and dedicated communities. By providing solution for forsaken programms and language one can earn respect and recognition from the community.