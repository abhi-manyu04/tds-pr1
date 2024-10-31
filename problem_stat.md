## Create a GitHub repo with these files in the main branch:

- users.csv. See below. Use the SAME values as in the API response. For booleans, use true and false and empty strings for null.
- repositories.csv. See below. Use the SAME values as in the API response. For booleans, use true and false and empty strings for null.
- README.md. See below.
Optional but recommended: your code and/or spreadsheet, in whichever language you analyzed the data in.

### users.csv has following information about each user in Austin with over 100 followers, with fields:

- login: Their Github user ID
- name: Their full name
- company: The company they work at. Clean up company names. At least make sure:
    - They're trimmed of whitespace
    - Leading @ symbol is stripped (Note: ONLY the first one is stripped)
    - They are converted to UPPERCASE
- location: The city they are in
- email: Their email address
- hireable: Whether they are open to being hired
- bio: A short bio about them
- public_repos: The number of public repositories they have
- followers: The number of followers they have
- following: The number of people they are following
- created_at: When they joined Github

### repositories.csv has these users' public repositories. For each user in users.csv, fetch up to the 500 most recently pushed repositories, with fields:

- login: The Github user ID (login) of the owner, which, BTW, is not directly in the API response.)
- full_name: Full name of the repository
- created_at: When the repository was created
- stargazers_count: Number of stars the repository has
- watchers_count: Number of watchers the repository has
- language: The programming language the repository is written in
- has_projects: Whether the repository has projects enabled
- has_wiki: Whether the repository has a wiki
- license_name: Name of the license the repository is under (This is under license.key)

### README.md must begin with 3 bullet points. Each bullet must be one sentence no more than 50 words.

- An explanation of how you scraped the data
- The most interesting and surprising fact you found after analyzing the the data
- An actionable recommendation for developers based on your analysis

Your peers will rank your README.md subjectively. You can add anything else you like in the README.md but your peers will only focus on the 3 bullet points.

We'll distribute 5 repos to each peer to rank based on:

- Whose PROCESS of analysis looks best to you? (Peers wil rank from 1 - best to 5 - worst)
- Whose RESULTS did you find most interesting? (Peers wil rank from 1 - best to 5 - worst)

Peer scores are calculated as follows:

- PROCESS SCORE = 2% of project grade for rank 1, 1.5% for rank 2, 1% for rank 3, 0.5% for rank 4, 0% for rank 5
- RESULT SCORE = 2% of project grade for rank 1, 1.5% for rank 2, 1% for rank 3, 0.5% for rank 4, 0% for rank 5