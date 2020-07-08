# Code Review

* Reviewed by Ekaterina Romanovskaya, DS 16 *


## Code Execution

I installed the package but failed to import the module and invoke the function.
When trying to import the package, I get the error `AttributeError: 'CallableDynamicDoc' object has no attribute 'display'`,
which is caused by
`setup = pd.set_option.display.max_columns = 999`. 
Didn't see the functional purpose of having that so I commented it out  -- and the code runs now.


## Package Structure

-- The package contains two setup.py files with different information;
-- README.md lacks specifics about funtions in the package. I would add useful descriptions and explanations;
-- __init__.py defines the function, but there are no comments about what it does (it's quite clear, though, from the code itself);
-- __init__.py seems to include test code and functions outside of module. I'd suggest moving `check_null` and `explore` functions to module. 


## Style

(+) The code looks clean;
(-) I would add more meaningful comments.


## Overall Impression

In my opinion, this work will gain more value for people, unfamilliar with the context of this assignment, if it provides more information about what the code does and what input it expects. 
