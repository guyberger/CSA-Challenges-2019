# Pinball Cipher
## Getting started
After playing a bit with pinball.elf provided we see that the way to decrypt the messege is to use the "transform" command.
However, the command needs to be run with 4 additional arguments (other than input/output files).
```
<INPUT_FILE> <OUTPUT_FILE> <KEY_PY> <KEY_PX> <KEY_VY> <KEY_VX>
```
We can try some random options and quickly see that the valid options for the keys are:
```
<KEY_PY>, <KEY_PX>: {'1', '2', ..., '9'}
<KEY_VY>, <KEY_VX>: {'+', '-'}
```
## Decription
Since the search space is relatively small, brute force search will quickly provide the answer.
### Flag:
> CSA{wE_sh0uLd_hav3_BeEn_n1cer_t0_oUr_siST3r}
