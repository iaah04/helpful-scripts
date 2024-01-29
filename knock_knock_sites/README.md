# Description
1. make_json.py - write link (only for clear site) and it will create a json files with all links on this site
2. sort_sites.py - sort union and clear links
3. ping_clear_sites.py and ping_dark_sites.py pings sites from the json site

# Tor network

1. Install tor:

```
brew install tor
```

2. Start network:
```
brew services start tor
```

3. Stop network:

```
brew services stop tor
```

4. Status:

```
brew services list
```

5. Write proxy ports here:

```
sudo nano /usr/local/etc/tor/torrc
```

like that:

```
SocksPort 9050
```

# Resources
- [Guide how to ping sites from tor](https://medium.com/@jasonrigden/using-tor-with-the-python-request-library-79015b2606cb)
