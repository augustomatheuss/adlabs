# Awk command examples.  

## Example 1. Cut column 5.  
```
awk '{print $5}' 
```

## Example 2. Cut columns 1 and 2.  
```
awk '{print $1, $2}'
```

## Example 3. Get the line 16 from a file my-file.txt.  
```
awk NR==16 my-file.txt
```
