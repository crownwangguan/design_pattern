# Factory Pattern

## Problem:
Shipping <Flight, Ship, Truck> Calculate shipping fee based on shipping method.

## Solution:
Create Abstruction. Client doesn't need to know the underlying method. All shipping methods extend abstract class and override the interface. Produce concreate product based on the method to create.

## Applicability:
* When don't know beforehand the exact types and dependencies of the objects going to work with. (**To add a new product type to the app, only need to create a new creator subclass**)

* When want to provide users of the library with a way to extend its internal components. (**Reduce the code that constructs components across the library into a single factory method and let anyone override this method in addition to extending the component itself**)

## Implement:
1. Make all products follow the same interface. 
2. Add an empty factory method inside the creator class. The return type of the method should match the common product interface.
3. Create a set of creator subclasses for each type of product listed in the factory method.
