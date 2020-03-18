# Search files and expressions examples.  

## Example 1. Get largest file in a directory  
```
'$(ls the-directory --sort=size | head -n 1)'
```  

## Example 2. Get text between the parentesis  
```
grep -Po '(?<=\().*(?=\))' 
```

## Example 3. Find file with expression inside current directory or subs  
```
grep -r . -e "the-expression"
```

## Example 4. Example 3 with types of file in specific (C code in example)  
```
grep --include=\*.{c,h} -r . -e "the-expression"
```

## Example 5. Get n lines before every result in file search  
```
grep -B n "the-pattern"  
```

## Example 6. Get n lines after every result in file search  
```
grep -A n "the-pattern"  
```

## Example 7. Get n lines arround (context) every result in file search  
```
grep -C n "the-pattern"  
```  

## Example 8. Search all files inside a directory and shred them.  
## In this example all regular files with ".jp" in the name will be shred 5 times and rewritten with zeros (verbose mode).  
```
sudo find `pwd` -type f -name "*.jp*" | xargs sudo shred -n 5 -z -v
```

