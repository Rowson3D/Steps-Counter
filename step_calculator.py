def calculate_steps(num_images, batch_size, min1, max1, min2, max2, step_mode):
    """
    Calculates the steps based on the provided parameters, dynamically selecting the
    calculation routine based on the chosen mode.

    Args:
        num_images (int): The number of images.
        batch_size (int): The batch size.
        min1 (int): The minimum value for the first step.
        max1 (int): The maximum value for the first step.
        min2 (int): The minimum value for the second step.
        max2 (int): The maximum value for the second step.
        step_mode (str): The step calculation mode (Normal, Strict, Prioritize Epochs, Prioritize Repeats)

    Returns:
        dict or None: A dictionary containing the 'repeats', 'epochs', and 'total_steps',
                     or None if no suitable factors are found.
    """

    factor1 = get_repeats_factor(num_images, min1, max1, step_mode)
    if not factor1:
        return None
    
    divided_result = (num_images * factor1) // batch_size

    factor2 = get_epochs_factor(divided_result, min2, max2, min_result=min2, step_mode=step_mode)
    if not factor2:
         return None
    
    total_steps = divided_result * factor2
    return {
        "repeats": factor1,
        "epochs": factor2,
        "total_steps": total_steps,
    }

def get_repeats_factor(value, min_range, max_range, step_mode):
     """
     Returns the correct function to use to calculate the factor1, based on mode.
     """
     if step_mode == "Strict":
          return find_strict_repeats_factor(value, min_range, max_range)
     elif step_mode == "Prioritize Repeats":
         return find_repeats_factor(value, min_range, max_range, prioritize="repeats")
     else: #Normal and Prioritize Epochs
          return find_repeats_factor(value, min_range, max_range)


def find_repeats_factor(value, min_range, max_range, prioritize=None):
      """
      Finds a factor for repeats where (value * factor) is within the given range.
      
      Args:
         value (int): The value to multiply.
         min_range (int): The minimum value of the range.
         max_range (int): The maximum value of the range.
         prioritize (str or None): If repeats or epochs should be prioritized, from highest to lowest.
      Returns:
         int or None: The found factor, or None if no factor is found.
      """
      if prioritize == "repeats":
          for i in reversed(range(1,1001)): #Reverse to get a lower value.
            result = value * i
            if min_range <= result <= max_range:
                return i
      else: #normal
          for i in range(1,1001):
            result = value * i
            if min_range <= result <= max_range:
                return i
      return None
   
def find_strict_repeats_factor(value, min_range, max_range):
       """
      Finds a factor for repeats where (value * factor) matches exactly the minimum range.
      
      Args:
         value (int): The value to multiply.
         min_range (int): The minimum value of the range.
         max_range (int): The maximum value of the range.
      Returns:
         int or None: The found factor, or None if no factor is found.
      """
       for i in range(1,1001):
            result = value * i
            if result == min_range:
                  return i
       return None

def get_epochs_factor(value, min_range, max_range, min_result, step_mode):
    """
    Returns the correct function to use to calculate factor2, based on mode.
    """
    if step_mode == "Prioritize Epochs":
         return find_epochs_factor(value, min_range, max_range, min_result, prioritize="epochs")
    elif step_mode == "Prioritize Repeats":
         return find_epochs_factor(value, min_range, max_range, min_result, prioritize="repeats")
    else: # Normal and strict mode use this.
        return find_epochs_factor(value, min_range, max_range, min_result)


def find_epochs_factor(value, min_range, max_range, min_result=0, prioritize=None):
    """
    Finds a factor for epochs such that (value * factor) is within the given range.

    Args:
        value (int): The value to multiply.
        min_range (int): The minimum value of the range.
        max_range (int): The maximum value of the range.
        min_result(int): Minimum result that needs to be met.
        prioritize (str or None): If epochs or repeats should be prioritized.
    Returns:
        int or None: The found factor, or None if no factor is found.
    """
    if prioritize == "epochs":
         for i in reversed(range(1, 1001)): #From high to low to find highest value
            result = value * i
            if min_range <= result <= max_range and result >= min_result:
                return i
    elif prioritize == "repeats":
          for i in range(1, 1001): #From low to high to find smallest value
            result = value * i
            if min_range <= result <= max_range and result >= min_result:
                return i
    else:
      for i in range(1, 1001): #Normal value.
            result = value * i
            if min_range <= result <= max_range and result >= min_result:
                return i
    return None