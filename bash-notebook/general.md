# General examples.  

## Example 1. Get the number of columns in terminal  
```
$(tput cols)
```  

## Example 2. Get and Set backlight  
* To get and set, read and write a file in /sys/class/backlight
```
/sys/class/backlight/intel_backlight/brightness
```  

## Example 3. Verifying authenticity of a Debian iso
* Download the checksum file and the signed file and try to verify with gpg
```
gpg --verify SHA512SUMS.sign.txt SHA512SUMS.txt
```  
* If the output gives the message "Can't check signature: No public key"  
*	Get the key from key ID in the output from debian keyring  
```
gpg --keyserver keyring.debian.org --recv-keys PUT-THE-KEY-ID-HERE
```  
* If you get the error "gpg: keyserver receive failed: No dirmngr", install the dirmngr
```
apt-get update && apt-get install dirmngr
```  
* Try to verify again the checksum file with gpg
```
gpg --verify SHA512SUMS.sign.txt SHA512SUMS.txt
```
* You must see "gpg: Good signature from "Debian CD signing key <debian-cd@lists.debian.org>""
* Verify the iso checksum (for sha256 and sha1 algorithm, just change the number in the command)
```
sha512sum -c SHA512SUMS.txt
```  

## Example 4. Take a screenshot (run the command and click in the target screen)  
```
xwd | xwdtopnm | pnmtopng > capture.png
```
