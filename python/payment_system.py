import random
import os
import csv
from datetime import datetime

def generate_workers(num_workers=400):
    """Generate a list of worker dictionaries with random data"""
    workers = []
    first_names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", 
                  "Michael", "Linda", "William", "Elizabeth", "David", "Barbara"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", 
                "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson"]
    
    for i in range(num_workers):
        gender = random.choice(["Male", "Female"])
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        worker_id = f"HRC-{1000 + i}"
        base_salary = random.randint(5000, 35000)
        overtime = random.randint(0, 20) * 100
        total_salary = base_salary + overtime
        
        workers.append({
            "worker_id": worker_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "base_salary": base_salary,
            "overtime": overtime,
            "total_salary": total_salary
        })
    
    return workers

def determine_employee_level(worker):
    """Determine employee level based on salary and gender"""
    salary = worker["total_salary"]
    gender = worker["gender"]
    
    if 10000 < salary < 20000:
        return "A1"
    elif 7500 < salary < 30000 and gender == "Female":
        return "A5-F"
    else:
        return "B2"  # Default level

def generate_payment_slip(worker, output_dir="output/python_payment_slips"):
    """Generate a payment slip for a single worker"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Determine employee level
        employee_level = determine_employee_level(worker)
        
        # Generate filename
        filename = f"{output_dir}/{worker['worker_id']}_{worker['last_name']}_payment_slip.txt"
        
        # Generate payment slip content
        slip_content = f"""
        HIGH RIDGE CONSTRUCTION COMPANY
        ----------------------------------------
        PAYMENT SLIP - WEEKLY
        ----------------------------------------
        Employee ID: {worker['worker_id']}
        Name: {worker['first_name']} {worker['last_name']}
        Gender: {worker['gender']}
        Employee Level: {employee_level}
        
        Base Salary: ${worker['base_salary']:,.2f}
        Overtime: ${worker['overtime']:,.2f}
        ----------------------------------------
        TOTAL SALARY: ${worker['total_salary']:,.2f}
        
        Date: {datetime.now().strftime('%Y-%m-%d')}
        ----------------------------------------
        """
        
        # Write to file
        with open(filename, 'w') as file:
            file.write(slip_content)
            
        return True
    
    except Exception as e:
        print(f"Error generating payment slip for {worker['worker_id']}: {str(e)}")
        return False

def export_to_csv(workers, output_dir="output"):
    """Export all worker data to a single CSV file"""
    try:
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/payment_slips_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ["Worker ID", "First Name", "Last Name", "Gender", 
                         "Base Salary", "Overtime", "Total Salary", "Employee Level"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for worker in workers:
                writer.writerow({
                    "Worker ID": worker["worker_id"],
                    "First Name": worker["first_name"],
                    "Last Name": worker["last_name"],
                    "Gender": worker["gender"],
                    "Base Salary": worker["base_salary"],
                    "Overtime": worker["overtime"],
                    "Total Salary": worker["total_salary"],
                    "Employee Level": determine_employee_level(worker)
                })
        print(f"CSV report generated: {filename}")
        return True
        
    except Exception as e:
        print(f"Error generating CSV report: {str(e)}")
        return False

def main():
    """Main function to generate payment slips for all workers"""
    try:
        print("Generating worker data...")
        workers = generate_workers(400)
        
        print("Generating payment slips...")
        success_count = 0
        for worker in workers:
            if generate_payment_slip(worker):
                success_count += 1
        
        # Generate CSV report
        export_to_csv(workers)
        
        print(f"Successfully generated {success_count} payment slips.")
        print(f"Failed to generate {400 - success_count} payment slips.")
        
    except Exception as e:
        print(f"An error occurred in the main process: {str(e)}")

if __name__ == "__main__":
    main() 