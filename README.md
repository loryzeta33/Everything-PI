# Everything-PI

Everything-PI is a funny script which let you search in the PI value a number or a text (its related ASCII code).


## Pi value

The PI value is stored in 2 file:
- the first contains the value with 1 million places and it's already in the repository `pi_dec_1m.txt`
- the second contains the value with 1 billion places and it's not in the repository because its dimension is 1 GB; you can download it at https://archive.org/download/Math_Constants/Pi.zip.
The ZIP contains 2 file, put the `PI - Dec.txt` file in the `Pi values` folder, then change the name to `pi_dec_1b.txt` (the script will automatically use it).

The script also works with the first file, but if you want a better search you can download and use the second file.
(This choice let you try and use the script without download 1 GB of file, in case you don't have a good connection).

### Use other value

If you want, you can use a custom `.txt` file: just put it in the `PI values` directory and change its name in `pi_dec_custom.txt` (then the script will automatically use it).

### References

All values are downloaded from: https://pi2e.ch/blog/2017/03/10/pi-digits-download/

## How to use

Just run the `main.py` file and type what you want to search.

It returns where the number or the text was found and the relative index.

<img width="418" alt="image" src="https://user-images.githubusercontent.com/73521240/233862094-e5e9d992-773c-4b51-bf90-b1e56c7f21e5.png">
