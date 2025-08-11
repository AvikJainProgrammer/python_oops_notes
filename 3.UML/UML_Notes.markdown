# Unified Modeling Language (UML) Overview

## Introduction
- **Definition**: UML is a standardized visual language for modeling classes and their relationships in software systems.
- **Purpose**: Provides a graphical representation of class structures, attributes, methods, and relationships to aid design and communication.
- **Tools**: Can be hand-drawn or created using tools like diagrams.net.

## Representing Classes in UML
- **Structure**: A class is depicted as a box with three sections:
  1. **Class Name**: Top section (e.g., `Dog`).
  2. **Attributes**: Middle section, listing attributes with access modifiers and types.
  3. **Methods**: Bottom section, listing methods with access modifiers and return types.
- **Access Modifiers**:
  - `-` (private, e.g., `-name: string` in Python with `__name`).
  - `#` (protected, e.g., `#email: string` in Python with `_email`).
  - `+` (public, e.g., `+bark(): void`).
- **Conventions**:
  - If access modifier is omitted, assume attributes are private/protected and methods are public.
  - No colon or empty colon after a method (e.g., `+bark()`) indicates a `void` return type.
- **Example**:
  - **Dog Class**:
    - Attributes: `-name: string`
    - Methods: `+bark(): void`
  - **User Class**:
    - Attributes: `+username: string`, `#email: string`, `-password: string`
    - Methods: `+getEmail(): string`, `-encryptPassword(): void`

## UML Relationships
1. **Inheritance**:
   - **Representation**: Solid arrow pointing from subclass to superclass.
   - **Description**: Models an "is-a" relationship (e.g., `Dog` is an `Animal`).
   - **Example**:
     - `Animal` class with `+move(): void`.
     - `Dog` inherits `Animal`, adds `-name: string`, `+bark(): void`.
     - UML: `Dog` → `Animal` (solid arrow).

2. **Composition**:
   - **Representation**: Solid arrow with a filled diamond at the parent end.
   - **Description**: Models a "has-a" relationship where the child cannot exist without the parent (e.g., `Dog` has an `Owner`).
   - **Example**:
     - `Owner` class with attributes (e.g., `name`, `contactInfo`).
     - `Dog` composed of an `Owner` instance.
     - UML: `Dog` ◇— `Owner` (filled diamond at `Dog`).
     - Code: `Dog.__init__(self, owner: Owner)`.

3. **Association**:
   - **Representation**: Solid arrow between classes.
   - **Description**: Models a "has-a" relationship where objects can exist independently (e.g., `Person` has a `Car` but can exist without it).
   - **Example**:
     - `Person` associated with `Car`.
     - UML: `Person` — `Car` (solid arrow).
     - Unlike composition, destroying `Person` doesn’t destroy `Car`.

4. **Dependency**:
   - **Representation**: Dashed arrow from the dependent class to the depended-on class.
   - **Description**: Indicates a class uses another class (e.g., as a method parameter or local variable) without owning it.
   - **Example**:
     - `Dog` has a `+playWithToy(toy: Toy)` method, using a `Toy` object.
     - UML: `Dog` - - > `Toy` (dashed arrow).
     - Code: `Dog.playWithToy(self, toy: Toy)` or creating a `Toy` locally in a method.

## Composition vs. Association
- **Composition**:
  - Stronger relationship: Child cannot exist without the parent (e.g., `Hotel` composed of `Rooms`; destroying `Hotel` destroys `Rooms`).
  - Example: `Customer` composed of `ShoppingCart` and `Orders`; destroying `Customer` destroys `Orders` and their `OrderDetails`/`ShippingInfo`.
- **Association**:
  - Weaker relationship: Objects can exist independently (e.g., `Person` associated with `Car`).
  - Example: `Person` can exist without a `Car`, and vice versa.
- **Note**: Distinction is minor and not critical to focus on excessively.

## Summary
- **UML**: Visualizes classes, attributes, methods, and relationships (inheritance, composition, association, dependency).
- **Class Representation**: Uses boxes with sections for name, attributes, and methods; access modifiers (`-`, `#`, `+`) denote visibility.
- **Relationships**:
  - **Inheritance**: Solid arrow (`is-a`).
  - **Composition**: Filled diamond arrow (`has-a`, strong ownership).
  - **Association**: Solid arrow (`has-a`, loose relationship).
  - **Dependency**: Dashed arrow (temporary use of another class).
- **Practical Use**: Helps design and communicate software structure, clarifying relationships and dependencies.