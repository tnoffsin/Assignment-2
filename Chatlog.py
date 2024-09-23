#This is the range for the age of people who are seeking loans. 
def is_eligible_for_loan(age, min_age=18, max_age=65):
    """
    Check if the age is within the eligible range for a loan.
    
    Parameters:
    age (int): The age of the person.
    min_age (int): The minimum eligible age for a loan. Default is 18.
    max_age (int): The maximum eligible age for a loan. Default is 65.
    
    Returns:
    bool: True if the age is within the range, False otherwise.
    """
    if min_age <= age <= max_age:
        return True
    return False

# Example usage:
age = 30
if is_eligible_for_loan(age):
    print("Eligible for loan")
else:
    print("Not eligible for loan")

#This is the median for the age of people who are seeking loans.
    def calculate_median_age(ages):
        """
        Calculate the median age from a list of ages.
        
        Parameters:
        ages (list): A list of ages.
        
        Returns:
        float: The median age.
        """
        sorted_ages = sorted(ages)
        n = len(sorted_ages)
        mid = n // 2

        if n % 2 == 0:
            median = (sorted_ages[mid - 1] + sorted_ages[mid]) / 2
        else:
            median = sorted_ages[mid]

        return median

    # Example usage:
    ages = [25, 30, 35, 40, 45, 50, 55, 60, 65]
    median_age = calculate_median_age(ages)
    print(f"The median age of people seeking loans is {median_age}")
