# Highridge Construction Payment System in R

# Function to generate worker data
generate_workers <- function(num_workers = 400) {
  first_names <- c("James", "Mary", "John", "Patricia", "Robert", "Jennifer",
                  "Michael", "Linda", "William", "Elizabeth", "David", "Barbara")
  last_names <- c("Smith", "Johnson", "Williams", "Brown", "Jones", "Miller",
                 "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson")
  
  workers <- data.frame(
    worker_id = paste0("HRC-", 1000:(1000 + num_workers - 1)),
    first_name = sample(first_names, num_workers, replace = TRUE),
    last_name = sample(last_names, num_workers, replace = TRUE),
    gender = sample(c("Male", "Female"), num_workers, replace = TRUE),
    base_salary = sample(5000:35000, num_workers),
    overtime = sample(0:20, num_workers, replace = TRUE) * 100,
    stringsAsFactors = FALSE
  )
  
  workers$total_salary <- workers$base_salary + workers$overtime
  return(workers)
}

# Function to determine employee level
determine_employee_level <- function(salary, gender) {
  if (salary > 10000 & salary < 20000) {
    return("A1")
  } else if (salary > 7500 & salary < 30000 & gender == "Female") {
    return("A5-F")
  } else {
    return("B2")
  }
}

# Function to generate payment slip
generate_payment_slip <- function(worker, output_dir = "output/r_payment_slips") {
  tryCatch({
    if (!dir.exists(output_dir)) {
      dir.create(output_dir, recursive = TRUE)
    }
    
    employee_level <- determine_employee_level(worker$total_salary, worker$gender)
    
    filename <- file.path(output_dir, paste0(worker$worker_id, "_", worker$last_name, "_payment_slip.txt"))
    
    slip_content <- paste0(
      "\nHIGH RIDGE CONSTRUCTION COMPANY\n",
      "----------------------------------------\n",
      "PAYMENT SLIP - WEEKLY\n",
      "----------------------------------------\n",
      "Employee ID: ", worker$worker_id, "\n",
      "Name: ", worker$first_name, " ", worker$last_name, "\n",
      "Gender: ", worker$gender, "\n",
      "Employee Level: ", employee_level, "\n\n",
      "Base Salary: $", format(worker$base_salary, big.mark = ",", nsmall = 2), "\n",
      "Overtime: $", format(worker$overtime, big.mark = ",", nsmall = 2), "\n",
      "----------------------------------------\n",
      "TOTAL SALARY: $", format(worker$total_salary, big.mark = ",", nsmall = 2), "\n\n",
      "Date: ", format(Sys.Date(), "%Y-%m-%d"), "\n",
      "----------------------------------------\n"
    )
    
    writeLines(slip_content, filename)
    return(TRUE)
  }, error = function(e) {
    message(paste0("Error generating slip for ", worker$worker_id, ": ", e$message))
    return(FALSE)
  })
}

# Function to export CSV report
export_to_csv <- function(workers, output_dir = "output") {
  tryCatch({
    if (!dir.exists(output_dir)) {
      dir.create(output_dir, recursive = TRUE)
    }
    
    workers$employee_level <- mapply(determine_employee_level, 
                                   workers$total_salary, 
                                   workers$gender)
    
    timestamp <- format(Sys.time(), "%Y%m%d_%H%M%S")
    filename <- file.path(output_dir, paste0("payment_slips_", timestamp, ".csv"))
    
    write.csv(workers, filename, row.names = FALSE)
    message(paste("CSV report saved to:", filename))
    return(TRUE)
  }, error = function(e) {
    message(paste("Failed to export CSV:", e$message))
    return(FALSE)
  })
}

# Main function
main <- function() {
  tryCatch({
    message("Generating worker data...")
    workers <- generate_workers(400)
    
    message("Generating payment slips...")
    success_count <- 0
    for (i in 1:nrow(workers)) {
      if (generate_payment_slip(workers[i, ])) {
        success_count <- success_count + 1
      }
    }
    
    # Export CSV report
    export_to_csv(workers)
    
    message(paste("Successfully generated", success_count, "payment slips"))
    message(paste("Failed to generate", 400 - success_count, "payment slips"))
    
  }, error = function(e) {
    message(paste("Main process failed:", e$message))
  })
}

# Execute
main()