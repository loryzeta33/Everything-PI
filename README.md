# Everything-PI

Everything-PI is a fun script that lets you search for a number or text (converted into its ASCII code) inside the digits of π.

## Pi value

The digits of π are stored in text files:
 - `pi_dec_1m.txt` → first **1 million** digits (already in the repository).
 - `pi_dec_1b.txt` → first **1 billion** digits (≈1 GB, not included).

### Download 1 billion digits

#### Automatically

You can download the `pi_dec_1b.txt` file automatically by running `download.py`.

#### Manually

You can also manually download it from [archive.org](https://archive.org/download/Math_Constants/Pi.zip), extract the file `PI - Dec.txt` into the `pi_values/` folder and rename it to `pi_dec_1b.txt`.

### Use a custom value

You can also use your own `.txt` file:
 - put it in the `pi_values/` directory
 - rename it `pi_dec_custom.txt`
 - the script will load it automatically.

### File priority

If multiple files are present in the pi_values/ directory, the script will automatically select one according to the following priority:
 1.	`pi_dec_custom.txt` (custom file)
 2.	`pi_dec_1b.txt` (1 billion digits)
 3.	`pi_dec_1m.txt` (1 million digits, default)

### References

Digits are taken from: [pi2e.ch](https://pi2e.ch/blog/2017/03/10/pi-digits-download/)

---

## How to use

Clone the repository and install dependencies:

```bash
git clone https://github.com/loryzeta33/Everything-PI.git
cd Everything-PI
pip install -r requirements.txt
```

Run the main script:

```bash
python main.py
```

### Example

<img width="418" alt="image" src="https://user-images.githubusercontent.com/73521240/233862094-e5e9d992-773c-4b51-bf90-b1e56c7f21e5.png">

---

## Requirements

See [requirements.txt](requirements.txt) for the full list.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.