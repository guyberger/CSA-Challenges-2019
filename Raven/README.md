# Raven
Opening the file in a text editor we can try to understand some of the information written.
First thing I noticed was the hexadecimal encoding
> #46#69#6C#74#65#72/#46#6C#61#74#65#44#65#63#6F#64#65

After decrypting we get 
> FilterFlateDecode

which is the compressing algorithm for the pdf file.
To decompress we can use the command 
```
pdf --qdf --object-streams=disable in.pdf out.pdf
```
in linux.

After decompression , we can see that each incremental update contains a hidden letter from the flag written between the texts
> "read between" 

and 
>"the lines".

To find all the hiddent letters of the flag simply save each letter and remove one incremental update by deleting everything after 
> %%EOF

### Flag:
> CSA{ke3P_caLm_4Nd_r7fM}
