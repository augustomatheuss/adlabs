# Users, login and auth examples.  

## Example 1. See all users in the system.  
```
awk -F':' '{ print $1}' /etc/passwd
```

## Example 2. See all users logged.  
```
w
```
