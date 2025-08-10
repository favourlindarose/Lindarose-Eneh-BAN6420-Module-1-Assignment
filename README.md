### Highridge Construction Payment System 

##  Project Overview
A dual-language implementation (Python + R) for generating weekly payment slips for Highridge Construction Company workers, meeting all assignment requirements:

* Dynamically generates 400+ worker records  
* Creates individual payment slips  
* Generates consolidated CSV reports  
* Implements employee level logic (A1, A5-F)  
* Includes comprehensive error handling  

## Setup Instructions

### Prerequisites
** Python 3.8+ (`sudo apt install python3`)  
** R 4.0+ (`sudo apt install r-base`)   

### Clone/Setup
```bash
git clone [your-repo-url] highridge-payment-system
cd highridge-payment-system
````

### File Structure

python/
├── payment_system.py       # Main script
├── requirements.txt        # Dependencies
└── output/                 # Generated files
    ├── payment_slips_*.csv
    └── python_payment_slips/*.txt

### The script automatically generates the output file once it is run.
### Then inside the `output/` comes the payment slips and the rest.

### Command to run this:

```bash
cd python
chmod +x payment_system.py  ## an execution command this 
python3 payment_system.py
```

### Expected Output once the command is run on the terminal:

* Generating worker data...
* Generating payment slips...
* CSV report generated: output/payment\_slips\_20250807\_142022.csv
* Successfully generated 400 payment slips.
* Failed to generate 0 payment slips.

### Key Features

* Generates 400 workers with random data
* Creates individual payment slips in `output/python_payment_slips/`
* Produces consolidated CSV report with timestamp
* Implements employee level conditions:

  * A1: Salary >\$10k and <\$20k
  * A5-F: Salary >\$7.5k and <\$30k (Female only)


### R Implementation File Structure

```
r/
├── payment_system.R        # Main script
└── output/                 # Generated files
    ├── payment_slips_*.csv
    └── r_payment_slips/*.txt
```

### That `r/` is a directory that houses other files just like is stated in the structure.

### Run R Version Command


```bash
cd r
chmod +x payment_system.R
Rscript payment_system.R
```

### Final Output Structure

```
Highridge_Assignment.zip
├── python/
│   ├── payment_system.py
│   ├── requirements.txt
│   └── output/...
├── r/
│   ├── payment_system.R
│   └── output/...
└── README.md
