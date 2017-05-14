# bothub.py

Check if a Github user is active, bot or just n00b 

## Usage

bothub.py requires [PyGithub](https://github.com/PyGithub/PyGithub)

You can run bothub.py with

`python3 bothub.py <username>`

This will print a report for `<username>`.

For example `bothub.py octocat`

```
-linguist -> Fork of github/linguist = Status diverged

Report for user octocat:
- 7 Repositories
- 1 Forks (14.285714285714285%)
- 0 Identical Forks (0.0% of all forks)
- 0 Ahead Forks (0.0% of all forks)
- 0 Behind Forks (0.0% of all forks)
- 1 Diverged Forks (100.0% of all forks)
```

### API limit

Github currently has an API limit for request. You can register an [OAuth2 Application](https://github.com/settings/developers) and use its `client_id` and `client_secret` to bypass those limits.  
*Remember, you must keep those key secretly!*