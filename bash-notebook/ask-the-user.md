# Interactions with the user  

## Example 1. Ask the user Y/n  
```
read ok  
if [ "$ok" = "Y" ]; then ok="y";fi  
if [ "$ok" = "y" ]  
then  
	echo "Do something!"  
fi  
```

