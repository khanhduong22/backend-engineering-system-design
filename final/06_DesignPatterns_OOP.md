# 06_DesignPatterns_OOP - Software Design Patterns & Object-Oriented Design Study Guide

- **Total Master Cards**: 61

---

## 📂 Category: Design Patterns & OOP (38 cards)

### 🟡 Mid Level

#### 1. How does the Abstract Factory pattern compare to the Builder pattern?
**Answer:**
Definition & Core Intent Comparison:
- Abstract Factory focuses on producing families of related or dependent objects. It returns the requested product immediately without intermediate configuration steps.
- Builder focuses on constructing a complex object step-by-step. It separates the construction process from the final representation and often utilizes a Director to dictate the sequence of building steps before the final product is fetched.

Structural and Use-Case Differences:
- Abstract Factory places emphasis on product families where the variants must be compatible with each other (e.g., UI themes). 
- Builder places emphasis on the intricate, multi-step assembly of a single complex object where configuration options can vary widely during construction.

#### 2. How does the Command pattern compare to Strategy, and what is Command-Query Separation (CQS)?
**Answer:**
Design Pattern & Principle Comparisons:

1. Command vs. Strategy:
- Command: Converts any operation into an object, storing parameters as fields to defer execution, queue, log, or support undo/redo. It establishes unidirectional connections between senders and receivers.
- Strategy: Describes different interchangeable ways of doing the same thing within a single context, focusing on the algorithm used to achieve a goal rather than turning individual method calls into independent lifecycle-managed objects.

2. Command-Query Separation (CQS):
- Definition: A principle stating that every method should either be a command that performs an action (mutates state) and returns void, or a query that returns data to the caller without mutating state, but never both. Asking a question should not change the answer.
- Commands: Mutate system state; should not return values.
- Queries: Return data; are completely side-effect free (idempotent).
- Pros & Cons: CQS eliminates side-effect bugs, simplifies reasoning about code execution order, and improves readability, though it can occasionally lead to a higher number of method calls or verbose code.

#### 3. How does the Strategy pattern differ from the Template Method pattern?
**Answer:**
Definition & Core Intent of Template Method:
A behavioral pattern that defines the skeleton of an algorithm in a base operation, deferring some steps to client subclasses. It lets subclasses redefine certain steps of an algorithm without changing its overall structure.

Key Components of Template Method:
A base class declares algorithm placeholders (abstract methods), and derived classes implement these specific placeholders.

Core Differences:
- Level of Operation: Template Method is based on inheritance (works at the class level, making it static and fixed at compile-time), letting you alter parts of an algorithm by extending them in subclasses. Strategy is based on composition (works at the object level), letting you switch behaviors dynamically at runtime by supplying different strategy objects.
- Flexibility: Strategy allows complete replacement of the algorithm's entire behavior dynamically, whereas Template Method alters only specific steps of a pre-defined algorithmic skeleton.

#### 4. What are the General OOP Concepts and Core Design Principles, how do they work, and when should they be used?
**Answer:**
Definition & Core Intent: General OOP Concepts and foundational software design principles encompass strategies for structuring code, managing complexity, and ensuring maintainability. Key principles include:
- Open-Closed Principle (OCP): Software entities should be open for extension but closed for modification (analogy: 'brain surgery is not necessary when putting on a hat'). Achieved via inheritance, interfaces, or composition.
- Object Composition & Composition Over Inheritance: Building functionality by assembling an aggregate of different classes rather than inheriting behavior, avoiding rigid 'is-a' coupling.
- Separation of Concerns (SoC): Dividing a program into distinct sections where each addresses a separate concern (e.g., business logic vs presentation), allowing independent development and modularity.
- Convention Over Configuration: Frameworks assuming sensible defaults, reducing configuration decisions while maintaining flexibility.
- Kent Beck's Four Rules of Simple Design: Prioritized by 1) Tests Pass, 2) Expresses Intent, 3) No Duplication (DRY), 4) Small (YAGNI).
- KISS (Keep It Simple, Stupid) & Rule of Least Power: Minimizing architectural complexity and selecting the least powerful suitable language/tool to reduce bugs, maintenance overhead, and security vulnerabilities.
- Polymorphism: Providing a single interface to entities of different types to promote loose coupling and extensibility.

Concrete Code Example / Use Case:
Refactoring a monolithic service class by applying Separation of Concerns, extracting domain logic into cohesive classes, relying on interfaces for polymorphism, and using composition over inheritance while keeping tests green.

Trade-offs / Pros & Cons:
- Pros: High maintainability, readability, testability, lower defect rates, and flexibility for future changes.
- Cons: Initial architectural overhead, potential boilerplate code, increased number of classes/interfaces, and the risk of over-abstraction if principles are applied prematurely.

#### 5. What is the Template Method design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: The Template Method is a behavioral design pattern that defines the skeleton of an algorithm in a superclass (typically an abstract class) but lets subclasses override specific steps of the algorithm without altering its overall structure or sequence.

Key Components & Structure:
- AbstractClass: Declares the template method (often marked as final to prevent overriding) which dictates the invariant algorithm skeleton through a sequence of method calls. It defines primitive abstract steps that subclasses must implement, and optional 'hook' methods that provide default behavior which subclasses may override.
- ConcreteClass: Inherits the abstract class and overrides the specific primitive steps or hooks to supply custom implementation details while leaving the core algorithm flow untouched.

Concrete Code Example / Use Case:
- Data mining framework: Parsing different file formats (e.g., CSV, XML, DOC). The high-level workflow—opening the file, extracting data, parsing data, analyzing, and closing—remains identical across all file types. The base class implements the template method controlling this exact workflow, while concrete subclasses (CsvDataMiner, XmlDataMiner) implement the specific extraction and parsing steps.
- Use when you have several classes containing almost identical algorithms with minor, localized differences, or when you want to let clients extend only particular steps of an algorithm rather than its entire structure.

Pros, Cons & Trade-offs:
- Pros: Reduces code duplication by pulling common algorithm logic and boilerplate code into a single superclass; centralizes control of the algorithm skeleton; lets clients override only certain parts of a large workflow.
- Cons: Subclasses are strictly limited and constrained by the rigid skeleton provided by the base algorithm; maintenance overhead increases if the template method grows to include too many steps; potential violations of the Liskov Substitution Principle if subclasses improperly suppress or break default step implementations; results in rigid inheritance hierarchies if overused.


### 🔴 Senior Level

#### 1. How does the Adapter pattern compare to Decorator, Proxy, Bridge, and Facade structural patterns?
**Answer:**
Core Comparisons & Structural Differences:

- vs. Adapter vs. Decorator vs. Proxy (Wrapper Variations):
  - Adapter: Provides a completely different interface to its subject to make incompatible interfaces work together.
  - Proxy: Provides the exact same interface as its subject, acting as a surrogate or placeholder to control access, lazy-initialize, or cache.
  - Decorator: Provides an enhanced or extended interface (or maintains the same signature) to dynamically add responsibilities or behaviors via recursive composition.

- vs. Bridge:
  - Bridge is designed up-front to decouple an abstraction from its implementation so they can vary independently, supporting run-time binding.
  - Adapter is typically retrofitted after design to make otherwise incompatible classes work together.

- vs. Facade:
  - Facade defines a brand new, simplified, unified interface for an entire complex subsystem of objects.
  - Adapter makes an existing single incompatible interface usable, typically wrapping a single object rather than an entire subsystem.

#### 2. How does the Composite pattern compare structurally and intent-wise to Decorator and Proxy patterns?
**Answer:**
Definition & Core Intent:
Structural comparison of patterns that rely on recursive composition and delegation (Composite, Decorator, and Proxy).

Key Differences & Mechanisms:
- Composite: Organizes open-ended objects into tree hierarchies to represent part-whole structures, where a container can hold multiple children and aggregates or sums up results across them, treating individuals and compositions uniformly.
- Decorator: Wraps a single child component dynamically to add extra responsibilities or behaviors while preserving or extending the base interface. Unlike Composite, it only wraps one component and focuses on behavior enhancement rather than tree aggregation.
- Proxy: Acts as a surrogate or placeholder for another object to control access, lazy-load, or manage its lifecycle entirely on its own, hiding the underlying service object from the client.

Trade-offs & Architectural Considerations:
- Pros: High flexibility, adherence to core OOP principles (Open/Closed, Single Responsibility), and clean separation of concerns regarding structure, behavior, and access control.
- Cons: Can result in complex, deeply nested class hierarchies and potential debugging difficulty due to heavy reliance on recursive delegation and interception layers.

#### 3. How does the Decorator pattern compare to Strategy, Proxy, and Chain of Responsibility patterns?
**Answer:**
Understanding structural and behavioral boundaries with similar patterns helps prevent misuse:

- Decorator vs. Strategy: A Decorator lets you change the 'skin' of an object by adding outward behavior via wrappers, while a Strategy lets you change the 'guts' by swapping its internal algorithm.

- Decorator vs. Proxy: Both share similar structures based on composition, but a Proxy usually manages the lifecycle and access control of its service object on its own, whereas the composition of Decorators is controlled externally by the client.

- Decorator vs. Chain of Responsibility: Structurally nearly identical as both pass requests through a sequence of objects. However, in a Decorator, all classes process the request along a pipeline (wrapping and accumulating behavior), whereas in a Chain of Responsibility, execution stops as soon as exactly one object handles the request.

When NOT to use Decorator:
Avoid using it when your system requires frequent removal or inspection of specific middle wrappers in a deep stack, or when the initialization code becomes excessively verbose and complex (e.g., severe 'wrapper hell').

#### 4. How does the Mediator pattern compare to the Observer pattern?
**Answer:**
Both are behavioral design patterns used to manage communication between objects and achieve decoupling, but they implement communication flows differently:

- Mediator: Encapsulates complex communication and control logic into a single central hub object. Colleague components communicate exclusively through the mediator rather than knowing about each other directly. This centralizes multi-way interactions and coordination.

- Observer: Establishes dynamic, one-way event-driven relationships where 'Subjects' (publishers) broadcast notifications to a list of registered 'Observers' (subscribers) without knowing their concrete implementations.

Trade-offs:
- Observer is great for dynamic publisher-subscriber setups, but can lead to cascading updates, hidden control flows, or memory leaks if unmanaged.
- Mediator centralizes control and clarifies complex multi-object protocols, but risks turning the mediator into a monolithic God Object.

#### 5. How does the Prototype pattern relate to the Memento pattern and when should it be used as an alternative?
**Answer:**
Definition & Core Intent Comparison:
- Prototype: A creational pattern used to clone objects without coupling code to their specific classes, optimizing performance and hiding complex instantiation.
- Memento: A behavioral pattern that allows capturing and externalizing an object's internal state so it can be restored later without violating encapsulation.

Relationship & Alternative Use Case:
Prototype can serve as a simpler alternative to Memento for saving state in undo/redo or history stacks. This works effectively if the object whose state you want to store is straightforward, contains no complex links to external resources, or those links are easy to re-establish upon cloning. However, if state restoration requires strict encapsulation boundaries or complex delta calculations, Memento is preferred.

#### 6. How does the State pattern compare to the Strategy pattern, and what is its relationship to Finite-State Machines?
**Answer:**
Relationship to Finite-State Machines (FSM):
- The State pattern is a direct code-level object-oriented implementation of a Finite-State Machine concept, turning states into classes and transitions into method calls.

Comparison with Strategy Pattern:
- Structural Similarity: Both are behavioral design patterns that rely on composition to change a context's behavior by delegating work to helper objects. Both eliminate complex conditional (switch/if-else) statements.
- Dependency & Autonomy:
  - Strategy: Makes helper objects completely independent and unaware of each other. Strategies are usually selected by client code and swapped from the outside.
  - State: Does not restrict dependencies between concrete states. Concrete states are often aware of other states and can actively trigger state transitions, altering the context's state at will from the inside.

Trade-offs:
- While Strategy focuses on interchangeable algorithms chosen by clients, State focuses on self-driven or event-driven lifecycle transitions within an enclosed object context.

#### 7. What is the Abstract Factory design pattern, how does it work, and when should it be used?
**Answer:**
Core Intent & Problem Solved: The Abstract Factory pattern is a creational design pattern that lets you produce families of related or dependent objects without specifying their concrete classes. It solves the problem of tightly coupling client code to specific implementations of objects, ensuring that a system remains extensible and consistent when introducing new variants.

Key Components & Structure:
- Abstract Factory: Declares an interface for operations that create abstract product objects.
- Concrete Factories: Implements the operations to create concrete product objects.
- Abstract Products: Declares an interface for a type of product object.
- Concrete Products: Defines a product object to be created by the corresponding concrete factory, implementing the Abstract Product interface.

Concrete Code Example / Use Case: Cross-platform UI toolkits. When a client needs to render controls (e.g., Button, Checkbox, Window) matching a specific OS theme (e.g., Windows vs. macOS), the client requests them from a factory (WinFactory or MacFactory). This guarantees that a Windows button is never accidentally paired with a macOS checkbox.

Pros, Cons & Trade-offs:
- Pros: Guarantees product compatibility and consistency within a family; isolates concrete classes from client code; adheres to the Single Responsibility Principle and Open/Closed Principle by making it easy to swap out entire product families.
- Cons: Significantly increases code complexity and verbosity due to the proliferation of numerous new interfaces and classes; extending the factory to support entirely new kinds of products is difficult because it requires changing the abstract factory interface and all of its subclasses.

#### 8. What is the Adapter design pattern, how does it work, and when should it be used?
**Answer:**
Core Intent & Problem Solved:
The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. It acts as a wrapper that translates the interface of an existing class (the adaptee) into another interface expected by the client, without modifying the underlying source code. It is typically retrofitted to an existing application to integrate legacy systems, 3rd-party libraries, or reusable subclasses that lack common functionality.

Key Components & Structure:
- Client: Contains the existing business logic of the program.
- Client Interface (Target): The protocol or interface that collaborating classes must follow.
- Service / Adaptee: The useful legacy or 3rd-party class with an incompatible interface.
- Adapter: Wraps the service object while implementing the client interface, serving as a translator.

Concrete Code Example / Use Case:
Integrating a modern analytics library that expects JSON data into a legacy system that only outputs XML strings by creating an XML-to-JSON Adapter class that implements the target JSON interface and translates XML inputs behind the scenes.

Pros, Cons & Trade-offs:
- Pros: 
  - Single Responsibility Principle (separates interface/data conversion code from business logic).
  - Open/Closed Principle (allows introduction of new adapters safely without breaking existing client code).
  - Improves reusability and flexibility.
- Cons: 
  - Increases overall code complexity due to the introduction of new helper interfaces and indirection layers.

#### 9. What is the Bridge design pattern, how does it work, and when should it be used?
**Answer:**
Core Intent & Problem Solved:
The Bridge pattern is a structural design pattern that decouples an abstraction from its implementation so that the two can vary independently. It divides a monolithic class or a closely related set of classes into two separate hierarchies—abstraction and implementation—preventing a combinatorial explosion of subclasses (e.g., managing cross-platform graphics or multiple database servers simultaneously).

Key Components & Structure:
- Abstraction: Provides high-level control logic and maintains a reference to an implementation object.
- Refined Abstraction: Provides variants of the control logic.
- Implementor (Implementation): Declares the interface common for all concrete implementations.
- Concrete Implementors: Contain platform-specific or detail-specific code.

Concrete Code Example / Use Case:
Imagine an application with a `Shape` abstraction (with `RefinedAbstraction` variants like `Circle` and `Square`) and a `Color` implementation interface (with `ConcreteImplementations` like `Red` and `Blue`). Instead of creating `RedCircle`, `BlueCircle`, `RedSquare`, and `BlueSquare` subclasses, the `Shape` holds a reference to a `Color` object. This allows shapes and colors to be combined dynamically and extended independently.

Pros, Cons & Trade-offs:
- Pros:
  - Allows creating platform-independent classes and apps.
  - Client code works with high-level abstractions and is not exposed to platform details.
  - Open/Closed Principle: You can introduce new abstractions and implementations independently.
  - Single Responsibility Principle: Focus on high-level logic in the abstraction and platform details in the implementation.
  - Allows run-time binding of implementations.
- Cons:
  - Might make the code more complicated by introducing additional abstraction layers or applying the pattern to a highly cohesive/simple class.

#### 10. What is the Builder design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: The Builder pattern is a creational design pattern that lets you construct complex objects step by step. It separates the construction of a complex object from its representation, allowing the same construction process to create different types and representations. Unlike other creational patterns, Builder does not require products to share a common interface.

Key Components & Structure:
- Product: The final complex object being built.
- Builder Interface: Declares steps common to all types of builders.
- Concrete Builders: Provide specific implementations of the construction steps and assemble the final product.
- Director (Optional): Defines the order in which to call construction steps, isolating the product's construction sequence.
- Recursive Mechanisms: Can be used to build complex recursive object structures like Composite trees or DOM trees.

Concrete Code Example / Use Case:
- Eliminating 'telescoping constructors' (constructors overloaded with a massive number of optional parameters).
- Constructing immutable domain objects with massive optional configurations (e.g., HTTP Request builders, complex UI components).
- Building different representations of a product (e.g., building stone vs. wooden houses using the same steps).

Pros, Cons & Trade-offs:
- Pros: Isolates complex construction code from business logic; allows step-by-step object construction and deferred execution; improves readability over telescopic constructors; enables reuse of construction code for different representations.
- Cons: Increases overall code complexity and maintenance overhead by requiring the creation of multiple new classes.

#### 11. What is the Command design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent:
A behavioral design pattern that encapsulates a request as a stand-alone object containing all information needed for the request (method, parameters, and receiver). This transformation lets you parameterize clients with different requests, queue or log requests, delay execution, and support undoable operations.

Key Components & Structure:
- Command Interface: Usually declares an execution method like execute(), and optionally an undo() method.
- Concrete Commands: Implement various types of requests and bind a receiver to an action.
- Invoker: Asks the command to carry out the request, without knowing the concrete receiver or business logic.
- Receiver: Contains the actual business logic to perform the operation.

Concrete Code Example / Use Case:
- Use Case: Implementing GUI buttons, menu items, macro recording, remote procedure calls, or transactional task queues.
- Undo/Redo Integration: Often works in tandem with the Memento pattern, where commands trigger operations and mementos capture and externalize an object's internal state before execution. To undo, the system pops the last executed command and applies its paired memento to restore the prior state.

Pros, Cons & Trade-offs:
- Pros: Decouples the object that invokes the operation from the one knowing how to perform it; supports the Open/Closed Principle; enables queuing, logging, macro recording, and robust undo/redo operations.
- Cons: Code can become more complex and verbose as a large number of small classes are introduced; mementos can consume significant memory if large object states are saved frequently.

#### 12. What is the Composite design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent:
A structural design pattern that lets you compose objects into tree structures to represent part-whole hierarchies. It enables clients to treat individual objects (leaves) and compositions of objects (containers/composites) uniformly.

Key Components & Structure:
- Component: Declares the common interface for both primitive objects and complex containers in the tree, defining operations that can be performed on them.
- Leaf: The basic element of a tree that has no sub-elements or children. Leaves typically perform the actual application logic/work since they have no children to delegate to.
- Composite (Container): An element that stores child components (which can be leaves or other composites) and implements child-related operations (e.g., add, remove). It delegates work to its children via the Component interface using polymorphism and recursion.

Concrete Code Example / Use Case:
- Use Case: Representing tree-like object models such as UI component hierarchies (e.g., panels containing buttons and text fields) or file systems (e.g., directories containing files and sub-directories).
- Interaction with other patterns:
  - Flyweight: Shared leaf nodes of a Composite tree can be implemented as Flyweights to drastically reduce memory consumption when identical leaf structures repeat.
  - Visitor / Iterator: Visitors and Iterators are frequently used to traverse complex Composite trees and execute operations over heterogeneous element classes without modifying their structures (e.g., exporting a Composite tree to XML/JSON).
  - Chain of Responsibility: Often combined with Composite where a leaf component receiving a request passes it up through parent components toward the root.

Pros, Cons & Trade-offs:
- Pros: Simplifies client code by making operations uniform across complex hierarchies through polymorphism and recursion; supports the Open/Closed Principle by allowing new component types to be introduced without breaking existing code.
- Cons: Can make the design overly general, making it difficult to restrict specific types of components within a particular container if stricter type constraints are needed.

#### 13. What is the Decorator design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A structural design pattern (also known as Wrapper) that lets you attach new behaviors to objects dynamically by placing them inside special wrapper objects that contain the behaviors. It provides a flexible alternative to subclassing for extending functionality without altering existing code or affecting other objects from the same class.

Key Components & Structure:
- Component: Declares the common interface for both wrappers and wrapped objects.
- Concrete Component: Defines the basic behavior, which can be altered or extended by decorators.
- Base Decorator: Has a field for referencing a wrapped object. The field’s type is declared as the component interface to hold both concrete components and decorators.
- Concrete Decorators: Define extra behaviors that can be added to components dynamically, executing code either before or after passing requests to the target.

Concrete Code Example / Mechanism:
The wrapper implements the same interface as the target and delegates requests to it, while altering or extending the result. Business logic can be structured into layers, allowing client code to treat decorated and undecorated objects identically.

Pros, Cons & Trade-offs:
- Pros: Extend an object’s behavior without making new subclasses; add or remove responsibilities at runtime; combine several behaviors by wrapping an object into multiple decorators; follows the Single Responsibility Principle by dividing monolithic classes into smaller ones.
- Cons: Hard to remove a specific wrapper from a stack of wrappers; hard to implement decorators such that behavior does not depend on the order in the decorator stack; initial configuration code of layered wrappers can look complex; can lead to a high number of small wrapper classes and complicated debugging.

#### 14. What is the Facade design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A structural design pattern that provides a simplified, front-facing interface to a complex subsystem, library, or framework, masking its internal complexities and improving readability and usability.

Key Components & Structure:
1) Facade: Directs client requests to appropriate parts of the subsystem, coordinates moving parts, and knows where to direct calls. Multiple facades can be used to prevent a single facade from becoming bloated or polluting a single entry point with unrelated features.
2) Complex Subsystem: Dozens of interrelated objects and independent classes whose initialization order, dependencies, and complex data formats are hidden by the facade.
3) Additional Facades: Used to structure a subsystem into layers by creating entry points to each level, or to separate unrelated features.

Concrete Code Example / Use Case:
- Wrapping a complex set of legacy audio/video conversion classes (e.g., codecs, bitrates, audio/video mixers) into a single 'VideoConverter' class with a simple 'convert(filename, format)' method.
- Use when you need a limited but straightforward interface to a complex subsystem, or when you want to structure a subsystem into layers to reduce inter-subsystem coupling.

Pros, Cons & Trade-offs:
- Pros: Isolates client code from the complexity of a subsystem, reduces coupling, and improves readability and usability.
- Cons: A facade can easily evolve into a 'God Object' that is tightly coupled to all classes of an application if not carefully managed.

#### 15. What is the Factory Method design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A creational design pattern that defines an interface for creating an object, but lets subclasses or separate methods decide which class to instantiate. It acts as an alternative to constructors—especially when constructors lack expressiveness—allowing a class to defer instantiation to subclasses. It also can be used to save system resources by reusing existing objects (via caching or pooling) instead of rebuilding them each time.

Key Components & Structure:
1) Product: Interface for objects the factory method creates.
2) Concrete Products: Different implementations of the Product interface.
3) Creator: Abstract class declaring the factory method (can also serve as a specialization/step within a Template Method pattern).
4) Concrete Creators: Override the factory method to return instances of Concrete Products.

Concrete Code Example / Use Case:
A Logistics application with a 'Transport' interface and 'RoadLogistics' vs. 'SeaLogistics' creators that instantiate 'Truck' or 'Ship' products respectively. Use it when you don't know beforehand the exact types and dependencies of the objects your code should work with, or when you want to provide users of your library/framework a way to extend its internal components.

Pros, Cons & Trade-offs:
- Pros: Avoids tight coupling between creators and concrete products; adheres to the Single Responsibility Principle (creation code in one place) and the Open/Closed Principle (easily introduce new product types without breaking client code).
- Cons: Code can become more complicated and filled with boilerplate due to the introduction of many new subclasses.

#### 16. What is the Flyweight design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all data in each object.

Key Components & Structure:
- Flyweight: Contains the intrinsic state (invariant, context-independent data) that can be shared across multiple contexts.
- Context / Extrinsic State: Contains the unique, mutable state that cannot be shared and is either passed to flyweight methods or computed when needed.
- Flyweight Factory: Manages a pool of existing flyweights, ensuring they are shared properly and created only when necessary.

Concrete Code Example / Use Case:
- Text Rendering: Instead of allocating font, style, and glyph data for every single character instance on a screen, each character object stores only its extrinsic state (such as coordinates in the document), while the intrinsic heavy font and character data are shared via Flyweight instances.

Pros, Cons & Trade-offs:
- Pros: Dramatically reduces memory footprint and saves massive amounts of RAM when the application has a high volume of similar objects.
- Cons / Trade-offs: Trades RAM over CPU cycles when recalculating or passing extrinsic state, and increases code complexity.

#### 17. What is the Interpreter design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent:
The Interpreter design pattern is a behavioral design pattern that specifies how to evaluate sentences in a language. It is used when you need to define a grammatical representation for a language and provide an interpreter to deal with the sentences in that grammar.

Key Components & Structure:
- Abstract Expression: Declares an abstract 'Interpret' operation that is common to all nodes in the abstract syntax tree (AST).
- Terminal Expression: Implements the 'Interpret' operation associated with terminal symbols in the grammar. An instance is required for every terminal in a sentence.
- Non-terminal Expression: Implements 'Interpret' for the non-terminal symbols in the grammar. Typically maintains child expressions and recursively calls interpret on them.
- Context: Contains information that's global to the interpreter, which expressions may read or modify during evaluation.
- Client: Builds or is provided with the abstract syntax tree representing a particular sentence in the language, then invokes the 'Interpret' operation.

Concrete Code Example / Use Case:
Consider evaluating a boolean expression like `(A and B) or (not C)`:

```python
from abc import ABC, abstractmethod

# Context
class Context:
    def __init__(self):
        self.variables = {}
    def set(self, name, value):
        self.variables[name] = value
    def get(self, name):
        return self.variables[name]

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> bool:
        pass

# Terminal Expression
class TerminalExpression(Expression):
    def __init__(self, name):
        self.name = name
    def interpret(self, context: Context) -> bool:
        return context.get(self.name)

# Non-terminal Expression (AND)
class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    def interpret(self, context: Context) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Non-terminal Expression (NOT)
class NotExpression(Expression):
    def __init__(self, expr):
        self.expr = expr
    def interpret(self, context: Context) -> bool:
        return not self.expr.interpret(context)

# Client Usage
context = Context()
context.set('A', True)
context.set('B', False)

# Represents expression: A and B
expression = AndExpression(TerminalExpression('A'), TerminalExpression('B'))
print(expression.interpret(context)) # Output: False
```

Pros, Cons & Trade-offs:
- Pros: 
  - Easy to change and extend the grammar, as classes represent each rule.
  - Implementing simple languages, configuration parsers, or rule engines becomes straightforward.
- Cons:
  - Complex maintenance for large grammars; you must create a class for every grammar rule, leading to a class explosion.
  - Performance overhead due to deep recursive tree traversal and object instantiation.
  - Hard to maintain grammars with many non-terminals; consider parser generators (like ANTLR) or compiler frameworks for complex languages.

#### 18. What is the Iterator design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A behavioral design pattern that allows sequential traversal of elements in an aggregate object or complex data structure (such as lists, stacks, trees, or graphs) without exposing its underlying internal representation.

Key Components & Structure:
- Iterator Interface: Declares operations required for traversing elements (e.g., `hasNext()`, `next()`).
- Concrete Iterator: Implements specific traversal algorithms and keeps track of the current position in the traversal.
- Collection / Aggregate Interface: Declares methods for obtaining a compatible iterator.
- Concrete Collection: Implements the collection interface and returns a new instance of a concrete iterator upon client request.

Concrete Code Example / Use Case:
- Use when a collection has a complex data structure under the hood, but you want to hide its complexity from clients for security, decoupling, or convenience.
- Use when you need to provide a uniform traversal interface across different types of data structures, or when your app needs multiple simultaneous/parallel traversals over the same collection.
- Example: Client code interacts with an abstract `Iterator` to loop through items without knowing if the underlying structure is a dynamic array, a linked list, or a tree.

Pros, Cons & Trade-offs:
- Pros: Follows the Single Responsibility Principle (extracts bulky traversal algorithms) and Open/Closed Principle (allows new collections and iterators without breaking existing code). Simplifies collection interfaces and enables multiple concurrent or delayed iterations over the same collection.
- Cons: Can introduce unnecessary class overhead and added complexity for simple collections where direct indexing or a basic loop suffices. May be less efficient than direct iteration on specialized data structures.

#### 19. What is the Mediator design pattern, how does it work, and when should it be used?
**Answer:**
Type: Behavioral

Core Intent & Problem Solved:
The Mediator design pattern reduces chaotic, tightly-coupled dependencies between objects by restricting direct communication and forcing them to collaborate exclusively via a central mediator object. It prevents objects from referring to each other explicitly, promotes loose coupling, simplifies object protocols, and allows you to vary their interactions independently. It also aligns with the Single Responsibility Principle (by centralizing communication) and the Open/Closed Principle (by allowing new mediators or components to be introduced easily).

Key Components & Structure:
- Mediator Interface: Declares methods of communication with components (colleagues), usually including a notification or event-routing method.
- Concrete Mediators: Encapsulate relations, coordination logic, and complex communication rules between various components.
- Colleague Components: Various classes containing specific business logic that must remain unaware of other components. If something important happens, they only notify the mediator rather than talking directly to peers.

Concrete Code Example / Use Case:
A classic use case is a complex UI form (e.g., a registration or settings dialog) where changing one element—such as checking a 'Terms and Conditions' checkbox or selecting a specific dropdown—affects other elements, like enabling a submit button or showing an input field. Instead of checkboxes, text fields, and buttons knowing about each other, they communicate only through a DialogMediator.

Pros, Cons & Trade-offs:
- Pros: Reduces coupling between colleagues; centralizes control and communication logic; simplifies object protocols; increases reusability of individual components.
- Cons / Risks: The Mediator itself can evolve into a monolithic 'God Object' or maintenance bottleneck over time, becoming overly complex and tightly coupled to all underlying components.

When to Use:
- When classes are tightly coupled to many other classes, making system changes difficult and error-prone.
- When components cannot be reused across different contexts because they depend heavily on other components.
- When you find yourself creating subclass variations just to handle slight differences in how objects interact.

#### 20. What is the Memento design pattern, how does it work, and when should it be used?
**Answer:**
Type: Behavioral

Definition & Core Intent: The Memento design pattern lets you save and restore the previous internal state of an object (the originator) without revealing the details of its implementation, thereby preserving strict encapsulation boundaries. It is primarily used for temporary storage, implementing undo/redo functionality, transaction rollbacks, and taking state snapshots.

Key Components & Mechanism:
- Originator: Produces snapshots of its own internal state (including private fields) and can restore its state from mementos when needed. The originator is responsible for creating the snapshot itself.
- Memento: A value object that acts as an immutable snapshot of the originator’s state, usually passing data only once via the constructor. No other object can read the snapshot directly, keeping state data secure.
- Caretaker: Responsible for keeping track of the originator's history (often in a history stack) and storing mementos safely without examining or modifying their contents, knowing only when and why to capture or restore state.

Structure Variants:
1. Nested Classes Structure: Memento is nested inside the Originator, allowing the Originator to access private fields and methods of the Memento directly.
2. Intermediate Interface Structure: Restricts access to Memento's fields using an intermediary interface for Caretakers, while Originators access the full Memento class directly.
3. Stricter Encapsulation Structure: Supports multiple originators/mementos, restricts Caretakers from changing stored state, makes Caretakers independent of the originator, and links each Memento directly to its creating Originator.

Concrete Use Cases:
- Implementing undo/redo mechanisms in text editors, graphic design tools, or games.
- Managing transactions where operations must be rolled back on error.

Pros, Cons & Trade-offs:
- Pros: Preserves encapsulation boundaries; simplifies the originator's code by delegating state history storage to the caretaker; provides a clean way to handle rollbacks.
- Cons: Can consume significant RAM/memory if originators create mementos frequently or if state objects are large; caretakers must manage lifecycle costs to destroy obsolete mementos; dynamic languages (PHP, Python, JS) may not strictly guarantee state immutability inside the memento.

#### 21. What is the Observer design pattern, how does it work, and when should it be used?
**Answer:**
Type: Behavioral

Core Intent & Problem Solved:
The Observer pattern is a behavioral design pattern that establishes a one-to-many dependency between objects (a Publisher/Subject and multiple Subscribers/Observers). It defines a subscription mechanism so that when the subject changes its state, all its dependents are automatically notified and updated. This enables decoupled event-driven architectures, Model-View-Controller (MVC) components, and reactive programming.

Key Components & Structure:
- Subject (Publisher / Observable): Maintains a list of subscribers/observers, provides interface methods to attach, detach, and notify them, and issues events of interest upon state changes.
- Observer (Subscriber) Interface: Declares the uniform notification method (e.g., update) for objects that should be alerted.
- Concrete Subjects & Observers: Implement the specific business logic and perform actions in response to notifications, often consuming context data passed during the update.

Concrete Code Example / Use Case:
- Use Case: Event handling systems, UI component updates where user actions need to trigger multiple listeners, or when changes to one object's state require updating other objects whose exact set is unknown beforehand or changes dynamically at runtime.
- Example Concept: A data model (Subject) holding user preferences notifies multiple UI widgets (Observers) to re-render whenever the preferences change, without the model needing hardcoded references to specific widgets.

Pros, Cons & Trade-offs:
- Pros:
  - Open/Closed Principle: Allows adding new subscriber or publisher types independently without modifying existing code.
  - Loose Coupling: Subjects and observers interact through abstract interfaces rather than concrete implementations.
  - Dynamic Relationships: Object subscriptions can be established and torn down at runtime.
- Cons:
  - Unpredictable Notification Order: Subscribers are often notified in a random or undefined sequence.
  - Memory Leaks: Can cause severe memory leaks (the "Lapsed Listener Problem") if observers fail to properly unregister themselves from the subject.
  - Update Cascades: Complex or circular dependencies can trigger unexpected cascades of updates and performance degradation.

#### 22. What is the Prototype design pattern, how does it work, and when should it be used?
**Answer:**
Type: Creational

Definition & Core Intent:
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying (cloning) this prototype instead of instantiating new objects from scratch via constructors. It lets you copy existing objects without making your client code dependent on their concrete classes.

Key Components & Structure:
- Prototype Interface: Declares the cloning method (typically a clone() method).
- Concrete Prototypes: Implement the cloning operation, handling deep or shallow copies of their internal state.
- Client / Registry: Creates new objects by asking a prototype to clone itself. Can maintain a registry or cache of pre-built prototypes for easy retrieval.

Concrete Code Example / Use Case:
- Costly or Complex Initialization: When object creation via 'new' is expensive (e.g., requires database calls, heavy file I/O, or complex computations).
- Configuration Presets & Reducing Subclassing: Avoiding a proliferation of subclasses that only differ in how they initialize their respective objects.
- Command History: Saving copies of Commands into history (such as undo/redo command stacks).

Pros, Cons & Trade-offs:
- Pros: Avoids subclassing creation bloat; allows adding and removing products at runtime; eliminates repeated initialization code; hides the complexities of creating concrete products.
- Cons: Cloning complex objects with circular references, managing deep vs. shallow copy nuances, or dealing with internal synchronization locks can be tricky to implement correctly.

#### 23. What is the Proxy design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A structural design pattern that provides a surrogate or placeholder for another object to control access, delay initialization, manage lifecycles, or add cross-cutting behaviors (like logging or caching) without altering the original object's code.

Key Components & Structure:
- Service Interface: Declares the interface common to both the RealSubject and the Proxy, ensuring they are interchangeable from the client's perspective.
- RealSubject (Service): The core class that provides the actual business logic and heavy computations.
- Proxy: Holds a reference to the RealSubject, implements the Service Interface, and intercepts client requests to perform pre- or post-processing.

Common Variations / Specialized Proxies:
- Virtual Proxy: Implements lazy initialization to delay the creation of heavyweight objects until absolutely needed.
- Protection Proxy: Enforces access control and security checks to ensure only authorized clients can use the service.
- Remote Proxy: Manages local representation and network communication for a service located on a remote server.
- Caching Proxy: Internally caches expensive operation results and manages cache lifecycle.
- Logging / Audit Proxy: Intercepts requests to keep a history, audit trail, or debug logs.
- Smart Reference Proxy: Handles fine-grained reference counting, resource releasing, or memory management for heavy objects.

Concrete Code Example Concept:
```csharp
public interface IImage {
    void Display();
}

public class RealImage : IImage {
    private string _filename;
    public RealImage(string filename) {
        _filename = filename;
        LoadFromDisk(_filename);
    }
    public void Display() => Console.WriteLine($"Displaying {_filename}");
    private void LoadFromDisk(string file) => Console.WriteLine($"Loading {file}");
}

public class ProxyImage : IImage {
    private RealImage _realImage;
    private string _filename;
    public ProxyImage(string filename) => _filename = filename;
    public void Display() {
        if (_realImage == null) {
            _realImage = new RealImage(_filename); // Lazy initialization
        }
        _realImage.Display();
    }
}
```

Pros, Cons & Trade-offs:
- Pros: Controls service access without modifying the service itself (Open/Closed Principle), enables lazy loading for performance optimization, handles remote communication transparently, and manages object lifecycles.
- Cons: Increases code complexity, introduces extra architectural indirection, and may cause response latency due to interception or network overhead.

#### 24. What is the SOLID design pattern, how does it work, and when should it be used?
**Answer:**
SOLID is an acronym for five foundational design principles in object-oriented programming (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion) aimed at making software designs more understandable, flexible, and maintainable.

Key Components & Structure:
1. Single Responsibility Principle (SRP): Every module, class, or function should have responsibility over a single part of the functionality, and that responsibility should be entirely encapsulated. A class should have only one reason to change.
2. Liskov Substitution Principle (LSP): If class S is a subtype of type T, objects of type T may be replaced with objects of type S without altering program correctness. Subclasses must honor pre-conditions, post-conditions, and invariants of the base class. (Classic violation: a `Square` inheriting from a `Rectangle` and breaking dimension assumptions).
3. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions (e.g., introducing interfaces to decouple layers).

Concrete Code Example / Use Case:
Applying DIP and LSP in C# / Java:
```csharp
public interface IMessageSender {
    void Send(string message);
}
public class EmailSender : IMessageSender {
    public void Send(string message) { /* Send email */ }
}
public class NotificationService {
    private readonly IMessageSender _sender;
    public NotificationService(IMessageSender sender) {
        _sender = sender;
    }
    public void Notify(string msg) { _sender.Send(msg); }
}
```

Pros, Cons & Trade-offs:
- Pros: Promotes loose coupling, robust polymorphism, predictable behavior, easier unit testing, and valid test suite reuse (parent test suites pass seamlessly on child classes).
- Cons & Trade-offs: Introduces stricter design constraints, increases the number of classes and interfaces, and can lead to over-engineering if applied prematurely to small, short-lived systems.

#### 25. What is the Singleton design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A creational design pattern that ensures a class has only one instance while providing a global point of access to that instance.

Key Components & Structure:
- Private Constructor: Hides the constructor from client code to prevent direct instantiation using the `new` keyword.
- Private Static Variable: Holds the single instance of the class.
- Public Static Factory Method (e.g., `getInstance()`): The sole mechanism for obtaining the object, often implementing lazy initialization and thread-safety mechanisms (such as Double-Checked Locking or synchronized blocks) to prevent race conditions in concurrent environments.

Concrete Code Example / Use Case:
- Use Cases: Managing shared resources such as database connection pools, configuration managers, caching layers, or logging services.
- Implementation Concept:
```java
public class Singleton {
    private static volatile Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

Pros, Cons & Trade-offs:
- Pros: Guarantees strict single-instance control, provides a controlled global access point, and supports lazy initialization.
- Cons: Violates the Single Responsibility Principle by controlling both its own instantiation and its core business logic; introduces hidden global state; makes unit testing extremely difficult due to tight coupling and the inability to easily mock dependencies; requires careful thread-safety management.

#### 26. What is the State design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: The State pattern is a behavioral design pattern that allows an object to alter its behavior when its internal state changes. It makes the object appear as if it changed its class.

Key Components & Structure:
- Context: Stores a reference to a concrete state object, delegating state-specific behavior and requests to it via a common state interface. It can also manage state transitions.
- State Interface: Declares state-specific methods that mirror the operations allowed on the context.
- Concrete States: Subclasses that provide specific implementations for the state-specific methods. They can also directly trigger transitions to the next state by updating the context's reference.

Mechanism:
- Replaces massive conditional statements (switch/if-else blocks) that check object fields with polymorphism.
- Extracts state-specific logic into separate classes, cleaning up temporary fields and helper methods from the main context.
- Hierarchies of state classes can be composed or inherit from an abstract base class to reduce code duplication.

Use Case:
- Managing object workflows or lifecycles, such as document states (Draft, Moderated, Published) or connection states (Connected, Disconnected, Connecting), where behavior heavily depends on the current status.
- Classes polluted with massive conditionals altering behavior based on field values.

Pros, Cons & Trade-offs:
- Pros: Organizes code related to particular states into separate classes (adhering to the Single Responsibility Principle); makes state transitions explicit; allows adding new states without modifying existing code (Open/Closed Principle); simplifies the context by removing bulky conditional logic.
- Cons: Can be an overengineering overkill if a state machine has only a few states or rarely changes.

#### 27. What is the Strategy design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent:
A behavioral design pattern that defines a family of algorithms, encapsulates each one into a separate class, and makes them interchangeable. It lets the algorithm vary independently from clients that use it.

Key Components & Structure:
- Context: Maintains a reference to a concrete strategy and communicates with it solely through the strategy interface. It receives runtime instructions on which algorithm to use (often injected via constructor).
- Strategy Interface: Common to all concrete strategies, declaring the execution method used by the context.
- Concrete Strategies: Implement different variations of the algorithm.

Concrete Code Example / Use Case:
Useful for dynamically swapping how an operation or set of operations is performed at runtime—such as switching between different payment processing algorithms (e.g., CreditCardStrategy, PayPalStrategy) or sorting techniques depending on user input or environment configuration.

Pros, Cons & Trade-offs:
- Pros: Allows swapping algorithms at runtime, isolates algorithm implementation details, replaces rigid inheritance with flexible composition, and strictly adheres to the Open/Closed Principle.
- Cons: Can be an overkill if there are only a few rare, stable algorithms; clients must be aware of concrete strategy differences to choose the correct one; modern languages with functional programming support can often achieve the same behavior using lambda expressions or anonymous functions without full class boilerplates.

#### 28. What is the Visitor design pattern, how does it work, and when should it be used?
**Answer:**
Definition & Core Intent: A behavioral design pattern that lets you separate algorithms from the objects on which they operate. It represents an operation to be performed on the elements of an object structure without changing the classes of those elements, allowing you to add new operations to existing object structures without modifying them (following the Open/Closed Principle).

Key Components & Structure:
- Visitor Interface: Declares a set of visiting methods for each concrete element class.
- Concrete Visitors: Implements several versions of the same algorithm, tailored for different concrete element classes.
- Element Interface: Declares an accept method that takes a visitor as an argument.
- Concrete Elements: Implements the accept method by calling the visitor's visit method corresponding to its own class.

Mechanism (Double Dispatch): It achieves this through 'double dispatch', where the operation executed depends on both the type of the visitor and the type of the element.

Concrete Code Example / Use Case:
- Useful when performing distinct and unrelated operations on a complex heterogeneous object structure (like an Abstract Syntax Tree in compilers, cleaning up business logic, or extracting auxiliary behaviors that only make sense in some classes of a hierarchy).
- Example concept: A ReportGenerator visitor or ExportToXML visitor traverses a document structure containing Paragraph and Image elements, executing specific logic per element type without modifying the element classes.

Pros, Cons & Trade-offs:
- Pros: Excellent for executing operations across heterogeneous object hierarchies, making it easy to add new behaviors, and gathering related operations together in one class.
- Cons: Breaks encapsulation by requiring elements to expose their internal state via public getters/methods to the visitor, and makes it hard to add new Concrete Element classes because every visitor implementation must be updated to handle the new element type.

#### 29. When should you NOT strictly apply General OOP Concepts, and what are the trade-offs or alternatives?
**Answer:**
Definition & Core Intent: While General OOP Concepts provide robust guidelines, strict adherence in every scenario can lead to anti-patterns like over-engineering, speculative generalization (violating YAGNI), and architectural bloat.

Key Scenarios & Anti-patterns:
- Over-Abstraction & Excessive Boilerplate: Creating rigid hierarchies, deep inheritance trees, or abstract service locators where simple procedural scripts or flat data structures would suffice (e.g., small scripts, quick prototypes, or performance-critical micro-optimizations).
- Rule of Least Power vs Capability: Choosing an overly constrained tool or language that ends up forcing complex workarounds.
- Premature Optimization & Design Pattern Abuse: Applying complex enterprise patterns (like dynamic Service Locators instead of straightforward Dependency Injection) before actual requirements justify them.

Trade-offs / Pros & Cons:
- Pros of pragmatic deviation: Faster initial delivery, reduced cognitive load for simple tasks, and better performance where runtime dispatch and indirection are minimized.
- Cons: Technical debt, reduced scalability, and harder refactoring later if simplicity turns into unstructured spaghetti code.

#### 30. When should you NOT use the Chain of Responsibility pattern, and what are the alternatives?
**Answer:**
Non-Use Scenarios & Anti-patterns:
- Do not use Chain of Responsibility when every request is guaranteed to be handled by a specific known component, where a direct point-to-point method invocation or Mediator pattern is simpler and more transparent.
- Avoid it when performance is hyper-critical and the traversal overhead of a deep chain introduces unacceptable latency.
- Avoid when debugging and execution traceability are primary concerns and the dynamic routing makes log tracing overly convoluted without proper middleware wrappers.

Alternatives:
- Strategy Pattern: Use when a single, specific algorithm/handler needs to be chosen for a given context directly by the client, rather than letting multiple objects dynamically evaluate the request.
- Mediator Pattern: Use when communication between components is complex and centralized control is preferred over a decentralized chain.

#### 31. When should you NOT use the Factory Method pattern, and how does it compare in the evolution of creational patterns?
**Answer:**
When to Avoid Factory Method:
1) Simple Object Creation: Where a basic `new` operator suffices without configuration complexity.
2) No Subclass Variability Required: When object types are completely static and known.
3) Performance-Critical Situations: Where inheritance hierarchies introduce unwanted overhead or indirection.
4) Small, Simple Applications & Limited Future Extension Anticipated.
5) No Need for Encapsulated Creation Logic.
Overusing Factory Method in these scenarios leads to unnecessary boilerplate and architectural complexity.

Evolution Path:
- Systems often start with Factory Method because it is less complicated and easily customizable via subclasses.
- Over time, systems may evolve toward Abstract Factory (producing families of related objects), Prototype (cloning existing instances without strict subclasses), or Builder when greater flexibility or complex multi-step construction is needed.
- Abstract Factory can be implemented on top of sets of Factory Methods or using Prototype.

#### 32. When should you NOT use the Proxy pattern, and how does it compare to the Decorator and Adapter patterns?
**Answer:**
When NOT to use Proxy:
- When direct access to the object is simple, performant, and requires no security, caching, or lazy loading; adding a proxy introduces unnecessary indirection and maintenance overhead.
- When the performance penalty of request interception outweighs the architectural benefits.

Pattern Comparisons:
- Proxy vs. Decorator: Both share a similar structural composition (wrapping an object and implementing the same interface). However, their intent differs. A Proxy controls access to the target object and manages its lifecycle or location transparently. A Decorator enhances or adds behaviors (responsibilities) to the object, often stacking multiple decorators dynamically.
- Proxy vs. Adapter: An Adapter provides a *different* interface to wrap an existing object to make it compatible with a client expecting a specific interface. A Proxy provides the *same* interface as the underlying object.

#### 33. When should you avoid the Singleton design pattern, and what are its major architectural anti-patterns?
**Answer:**
Definition & Context: While Singleton provides a convenient global access point, overusing it introduces severe architectural drawbacks.

Architectural Trade-offs & Anti-Patterns:
- Global State Hazard: Singletons introduce global state into an application, making the behavior of components non-deterministic and heavily dependent on execution order.
- Testing Bottlenecks: Because Singleton instances are globally accessible and often self-initialized, unit testing becomes challenging. Mocking a Singleton for isolated testing typically requires complex dependency injection frameworks or bytecode manipulation.
- SOLID Violations: It violates the Single Responsibility Principle (SRP) by managing its own creation logic alongside application logic, and often violates the Dependency Inversion Principle (DIP) when high-level modules directly call a concrete Singleton rather than depending on abstractions.

Alternatives: In modern software architecture (such as when using Dependency Injection containers), passing dependencies explicitly via constructors is heavily preferred over relying on Singletons, as it preserves decoupling, testability, and architectural flexibility.


## 📂 Category: OOP & Code Smells (1 cards)

### 🔴 Senior Level

#### 1. What is a code smell, how do smells like 'Feature Envy' and 'Infeasible Code' manifest, and what is the economic and architectural justification for refactoring?
**Answer:**
1. Core Definition & Fundamental Concept: A code smell is a surface-level indicator that usually points to a deeper structural problem in the system. 
- Feature Envy occurs when a method in one class excessively invokes data or methods of another class, violating encapsulation.
- Infeasible (unreachable) code represents paths that can never execute, often indicating dead logic or overly complex conditionals, which are severely prohibited in safety-critical systems (e.g., avionics).

2. Real-world Code Example or Architecture Pattern:
// Feature Envy Example
class Invoice {
    private double subtotal;
    private double taxRate;
    public double getSubtotal() { return subtotal; }
    public double getTaxRate() { return taxRate; }
}

class InvoicePrinter {
    // Feature Envy: methods heavily rely on Invoice getters rather than its own data
    public void printTotal(Invoice inv) {
        double total = inv.getSubtotal() * (1.0 + inv.getTaxRate());
        System.out.println(total);
    }
}
// Resolution: Move the total calculation logic directly into the Invoice domain model (Tell, Don't Ask principle).

3. Trade-offs / Best Practices / How to avoid anti-patterns:
- Avoid justifying refactoring based purely on abstract moral principles ('clean code' or aesthetics). Refactoring is an economic necessity: it is performed because poorly structured code slows down feature delivery and increases bug rates. 
- Balance preemptive refactoring with business value using techniques like the Boy Scout Rule ('leave the campground cleaner than you found it').


## 📂 Category: OOP & Composition vs Inheritance (5 cards)

### 🔴 Senior Level

#### 1. How do Composition and Inheritance differ in managing object behavior, and how do they impact system coupling and architectural maintainability?
**Answer:**
1. Core Definition & Fundamental Concept:
- Inheritance (Is-A relationship) relies on class-based hierarchies where a subclass inherits state and behavior from a superclass, promoting code reuse at the cost of rigid compile-time coupling.
- Composition (Has-A relationship) delegates responsibilities by assembling objects together at runtime through interfaces, adhering to the principle of "favor object composition over class inheritance."

2. Real-world Code Example or Architecture Pattern:
- Inheritance Anti-Pattern: `class JetFuelEngine extends Engine` leading to a rigid taxonomy when trying to handle hybrid variants.
- Composition Pattern (Strategy / Dependency Injection):
```csharp
public interface IEngine {
    void Start();
}

public class Car {
    private readonly IEngine _engine;
    public Car(IEngine engine) {
        _engine = engine;
    }
    public void Drive() { _engine.Start(); }
}
```

3. Trade-offs / Best Practices / How to Avoid Anti-Patterns:
- Trade-offs: Inheritance creates tight coupling, breaks encapsulation (the fragile base class problem), and scales poorly with multidimensional variation. Composition increases object granularity and slight boilerplate, but yields extreme flexibility, runtime adaptability, and loosely coupled modules.
- Best Practices: Strictly use inheritance only for true polymorphic Is-A hierarchies (Liskov Substitution Principle). Use composition (with interfaces) for feature reuse, behavior modification, and to drastically reduce systemic coupling (such as preventing 'Shotgun Surgery' and adhering to the Law of Demeter).

#### 2. What are the core differences between Composition and Inheritance, and how do they impact system coupling and maintainability in Object-Oriented Design?
**Answer:**
Core Definition: Inheritance ("is-a") creates a tight, compile-time coupling between a parent class and its subclasses, making behavior modification difficult and vulnerable to the Fragile Base Class problem. Composition ("has-a") relies on injecting interfaces or behavioral objects, achieving loose coupling and high flexibility.

Architecture & Code Example:
Instead of inheriting behavior:
class Engine { void start() { /* ... */ } }
class Car extends Engine { } // Tight coupling, rigid hierarchy

Use composition via interfaces:
interface Engine { void start(); }
class V8Engine implements Engine { public void start() { /* ... */ } }
class Car {
    private final Engine engine;
    public Car(Engine engine) { this.engine = engine; }
    public void drive() { engine.start(); }
}

Trade-offs & Best Practices:
- Prefer Composition over Inheritance (GoF principle) to avoid deep, inflexible hierarchies and violation of the Liskov Substitution Principle (LSP).
- Keep components loosely coupled by adhering to the Law of Demeter and using dependency injection.
- Avoid anti-patterns like Singletons and tight concrete instantiations that harden coupling and break testability.

#### 3. What are the fundamental trade-offs between Composition and Inheritance regarding coupling, and how do design patterns and architectural principles (like SOLID and GRASP) address them?
**Answer:**
1. Core Definition & Fundamental Concept:
Inheritance (IS-A relationship) promotes code reuse via subclassing, but introduces tight, white-box coupling where subclasses depend heavily on the internal implementation details of their superclasses. Composition (HAS-A/USES-A relationship) builds complex types by assembling simpler, loosely coupled components via interfaces or delegation (black-box reuse).

2. Real-world Code Example or Architecture Pattern:
Instead of creating a rigid inheritance hierarchy like:
```csharp
class Bird { virtual void Fly(); }
class Penguin : Bird { override void Fly() { throw new NotSupportedException(); } // Violates LSP }
```
Use composition via interfaces to achieve loose coupling and adhere to the Liskov Substitution Principle (LSP) and Interface Segregation Principle (ISP):
```csharp
interface IFlyable { void Fly(); }
class Bird : IFlyable { public void Fly() { /* ... */ } }
class Penguin { /* No Fly behavior, no invalid overrides */ }
```
Patterns like Strategy, Observer, and Chain of Responsibility further decouple senders from receivers and avoid rigid class hierarchies.

3. Trade-offs / Best Practices / Anti-patterns:
- Anti-pattern: The 'Fragile Base Class' problem, where modifying a superclass inadvertently breaks subclasses due to tight coupling. Deep inheritance trees also violate the 'Favor composition over inheritance' principle (GoF).
- Trade-off: Composition requires writing more boilerplate delegation code and managing wiring, but yields high modularity, testability, and adherence to DRY and Single Responsibility Principles (SRP).
- Best Practice: Default to composition for behavior reuse. Reserve inheritance strictly for true polymorphic subtyping where substitutability (LSP) is fully guaranteed.

#### 4. What is the core difference between Composition and Inheritance in terms of coupling, and how does the Composite pattern leverage composition to solve part-whole hierarchies?
**Answer:**
1. Core Definition & Fundamental Concept:
- Inheritance (White-box reuse): Subclasses are tightly coupled to superclass implementation details. Changes to the parent class easily break child classes (Fragile Base Class problem). Promotes a strict 'is-a' relationship.
- Composition (Black-box reuse): Objects contain instances of other classes to delegate behavior. Promotes a flexible 'has-a' or 'uses-a' relationship based on interfaces, ensuring loose coupling.

2. Architecture Pattern (Composite Pattern):
The Composite pattern is a structural design pattern that composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects (Leaves) and compositions of objects (Composites) uniformly through a common interface.
Example:
```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children: list[Component] = []

    def add(self, component: Component):
        self._children.append(component)

    def operation(self) -> str:
        results = [child.operation() for child in self._children]
        return f"Branch({'+'.join(results)})"
```

3. Trade-offs & Best Practices:
- Prefer Composition over Inheritance (GoF principle) to avoid deep, rigid hierarchies and high coupling.
- Use Inheritance strictly for true polymorphism and shared core contracts, not merely for code reuse.
- Anti-pattern to avoid: Deep inheritance trees that violate the Liskov Substitution Principle (LSP).

#### 5. What is the difference between Coupling and Cohesion in software design, and why is high cohesion paired with low coupling considered a hallmark of clean architecture?
**Answer:**
Core Definition & Fundamental Concept:
- Coupling is the degree of interdependence between different modules or classes (how much they know about each other). High coupling means changes ripple across the system; low coupling means modules are independent.
- Cohesion is the degree to which elements within a single module or class belong together, focusing on a single, well-defined responsibility (e.g., Single Responsibility Principle).

Real-world Code Example or Architecture Pattern:
- Low coupling / High cohesion is exemplified by the Mediator pattern or Dependency Inversion Principle (DIP). Instead of class A directly instantiating and depending heavily on concrete class B (high coupling), class A depends on an abstraction (interface), and a DI container injects the dependency at the composition root.

Trade-offs / Best Practices / How to avoid anti-patterns:
- Avoid tight coupling via concrete inheritance hierarchies (which lock subclasses into rigid parent states and break encapsulation). Instead, favor object composition ('Has-a' over 'Is-a') to assemble behaviors dynamically, achieving low fan-out (depending on few external modules) and high fan-in (reusability across many clients).


## 📂 Category: OOP & Dependency Injection (1 cards)

### 🔴 Senior Level

#### 1. What is Inversion of Control (IoC) and Dependency Injection (DI), what are their core benefits, and how do you avoid related architectural anti-patterns?
**Answer:**
Core Definition: Inversion of Control is a design principle where the control of object creation and lifecycle is transferred from the application code to an external container or injector. Dependency Injection (DI) is a specific implementation of IoC where a client accepts its dependencies from an external source rather than instantiating them directly (e.g., using 'new' inside methods), decoupling the client from concrete implementations.

Benefits:
1. Enables isolated unit testing via mocking frameworks.
2. Allows dynamic configuration changes at runtime.

Code Example / Architecture Pattern:
Instead of a tight coupling like `class OrderService { private Database db = new MySQLDatabase(); }`, use constructor injection:
`class OrderService { private final Database db; public OrderService(Database db) { this.db = db; } }` managed by an IoC container (such as Spring, where the default bean scope is Singleton—one shared instance per container).

Trade-offs & Anti-Patterns:
- Anti-patterns to avoid: Direct instantiation (`new`), static methods/properties, and hidden dependencies.
- Trade-offs: Overuse of DI containers can lead to complex configuration graphs and runtime errors if not carefully managed. Ensure clear boundaries between object composition and business logic.


## 📂 Category: OOP & Domain-Driven Design (DDD) (6 cards)

### 🔴 Senior Level

#### 1. What are Entities, Value Objects, and Aggregates in Domain-Driven Design (DDD), and how are they implemented while avoiding common anti-patterns?
**Answer:**
Core Definition: DDD models complex business domains through a Ubiquitous Language. An Entity has a unique thread of identity that persists across states (e.g., User ID). A Value Object is defined entirely by its immutable attributes (e.g., Money, Address). An Aggregate is a cluster of associated entities and value objects treated as a unit for data changes, bounded by an Aggregate Root.

Code Example (Aggregate Root enforcing invariants):
public class Order {
    private OrderId id;
    private List<OrderItem> items;
    private OrderStatus status;

    public void addItem(Product product, int quantity) {
        if (status != OrderStatus.DRAFT) throw new IllegalStateException("Cannot modify non-draft order");
        items.add(new OrderItem(product.getId(), product.getPrice(), quantity));
    }
}

Trade-offs & Best Practices:
- Best Practice: Always modify state strictly through Aggregate Roots to maintain transactional consistency and boundary invariants.
- Anti-pattern: Creating overly large aggregates containing entire object graphs, leading to database contention, performance bottlenecks, and memory overhead. Keep aggregates small and reference other aggregates strictly by ID.

#### 2. What are the core building blocks of Domain-Driven Design (DDD), and how do Entities, Value Objects, and Aggregates collaborate to maintain domain invariants?
**Answer:**
Core Definition: Domain-Driven Design (DDD) aligns software implementation with a rich organizational Domain Model. Its tactical patterns include Entities (objects defined by a unique identity), Value Objects (immutable objects defined entirely by their attributes), and Aggregates (clusters of associated objects treated as a unit for data changes with a single Aggregate Root).

Architecture & Code Example:
```csharp
public class OrderId : ValueObject {
    public Guid Value { get; }
    public OrderId(Guid value) => Value = value;
    protected override IEnumerable<object> GetEqualityComponents() { yield return Value; }
}

public class Order : AggregateRoot<OrderId> {
    private readonly List<OrderItem> _items = new();
    public IReadOnlyCollection<OrderItem> Items => _items.AsReadOnly();
    public OrderStatus Status { get; private set; }

    public void AddItem(ProductId productId, int quantity, Money price) {
        if (Status != OrderStatus.Draft) throw new InvalidOperationException("Cannot modify submitted order.");
        _items.Add(new OrderItem(productId, quantity, price));
    }
}
```

Trade-offs & Best Practices:
- Best Practice: Always enforce business invariants inside the Aggregate Root, never expose internal collections directly, and keep aggregates small to minimize concurrency conflicts.
- Anti-Pattern: Making aggregates too large (e.g., placing an entire system graph into one aggregate) or letting database concerns leak into domain entities.

#### 3. What are the core components and tactical patterns of Domain-Driven Design (DDD), and how do you structure them to isolate business logic from infrastructure?
**Answer:**
Domain-Driven Design (DDD) is an approach to software development that focuses on modeling software to match a domain according to the input from domain experts. 

1. Core Components & Tactical Patterns:
- Entities: Objects with a distinct identity that runs through time and different states (e.g., User).
- Value Objects: Immutable objects defined only by their attributes, lacking conceptual identity (e.g., Money, Address).
- Aggregates: Clusters of associated entities and value objects treated as a unit for data changes, bounded by a root entity (Aggregate Root) that enforces consistency invariants.
- Repositories: Interfaces abstracting persistence, providing collection-like access to aggregates.
- Services: Encapsulate domain logic that doesn't naturally fit within a single Entity or Value Object.

2. Architecture & Code Example:
Entities and Use Cases must be plain objects with zero framework or database dependencies. 

```python
# Value Object
class Money:
    def __init__(self, amount: float, currency: str):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount
        self.currency = currency

# Aggregate Root
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self._items = []
        self._is_completed = False

    def add_item(self, product_name: str, price: Money):
        if self._is_completed:
            raise Exception("Cannot modify completed order")
        self._items.append((product_name, price))

    def complete(self):
        if not self._items:
            raise Exception("Cannot complete an empty order")
        self._is_completed = True
```

3. Trade-offs & Best Practices:
- Anti-pattern: Anemic Domain Models (where entities are mere data structures with getters/setters and business logic leaks into service layers). Ensure rich domain models where entities encapsulate behavior.
- Trade-off: DDD adds significant initial complexity and requires deep domain collaboration; use it only for complex, core business domains (Bounded Contexts), preferring CRUD or transaction scripts for simple support subdomains.

#### 4. What are the core principles of Domain-Driven Design (DDD) Bounded Contexts, and how do you design them effectively?
**Answer:**
Core Definition: A Bounded Context is a central pattern in DDD that explicitly defines the applicability of a domain model. It ensures that every Ubiquitous Language term has an unambiguous, singular meaning within its designated boundary, decoupling independent sub-domains.

Architecture Pattern & Anti-Patterns:
- DO NOT think in terms of shared data schemas or database tables.
- DO think about capabilities, business behaviors, and what actions/data the context provides to the wider system.
- Anti-pattern: Constructing a distributed monolith tightly coupled via shared database entities or chatty entity-reference calls.

Best Practices:
- Define contexts around business capabilities (e.g., Billing vs. Shipping).
- Establish explicit Context Mapping (e.g., Upstream/Downstream, Customer/Supplier, or Anti-Corruption Layer) to handle communication between different models safely.

#### 5. What is an Anemic Domain Model in Domain-Driven Design (DDD), why is it considered an anti-pattern, and how do you implement a Rich Domain Model instead?
**Answer:**
Core Definition & Fundamental Concept:
An Anemic Domain Model is a domain model where the objects (entities and value objects) contain state (properties) with getters and setters, but completely lack business behavior or domain logic. All business rules are extracted into procedural 'Domain Services' or 'Transaction Scripts'. This is considered a severe anti-pattern because it incurs the architectural and ORM-mapping complexity costs of a domain model without delivering the benefits of object-oriented encapsulation and polymorphic behavior.

Real-world Code Example:
[Anemic Approach - Anti-pattern]
class OrderService
  def complete_order(order)
    if order.items.empty?
      raise "Cannot complete empty order"
    end
    order.status = 'COMPLETED'
    order.save
  end
end

[Rich Domain Model Approach - DDD]
class Order
  attr_reader :status, :items

  def initialize(items)
    raise ArgumentError, "Order must have items" if items.empty?
    @items = items
    @status = :pending
  end

  def complete!
    raise DomainError, "Already completed" if @status == :completed
    @status = :completed
    raise DomainError, "Fulfillment failed" unless validate_inventory
  end

  private
  def validate_inventory
    # Encapsulated domain logic
    true
  end
end

Trade-offs / Best Practices / How to avoid anti-patterns:
- Best Practice: Keep invariants strictly protected inside Entities and Value Objects. Public setters should be prohibited; state changes should only happen through intent-revealing behavior methods (e.g., `complete!`, `allocate_funds`).
- Trade-off: Rich domain models require deeper domain understanding, careful handling of ORM configurations (e.g., mapping private fields or collections), and can complicate UI data-binding if not properly separated from DTOs.

#### 6. What is the responsibility of the Domain Layer in Domain-Driven Design (DDD) and how is it structured using tactical patterns?
**Answer:**
Core Definition: The Domain Layer (or Model Layer) represents business concepts, situations, and rules, explicitly controlling state reflective of business logic while delegating persistence and technical storage details to the Infrastructure Layer.

Architecture Pattern & Code Example:
It relies on tactical patterns such as Entities, Value Objects, and Aggregates. An Aggregate is a cluster of associated objects treated as a unit for data changes, bounded by a root entity:

```csharp
public class Order : AggregateRoot<OrderId>
{
    private readonly List<OrderLine> _orderLines = new();
    
    public OrderStatus Status { get; private set; }
    
    public void AddProduct(Product product, int quantity)
    {
        if (Status != OrderStatus.Draft)
            throw new InvalidOperationException("Cannot modify submitted order.");
            
        _orderLines.Add(new OrderLine(product.Id, product.Price, quantity));
    }
}
```

Trade-offs & Best Practices:
- Best Practice: Design small aggregates to minimize concurrency conflicts and transaction locks; reference other aggregates strictly by ID rather than direct object references.
- Anti-pattern: Anemic Domain Model, where business logic leaks out into transaction scripts or services while domain models are reduced to mere data containers with getters and setters.


## 📂 Category: OOP & OOP 4 Pillars (7 cards)

### 🟡 Mid Level

#### 1. What are the 4 Pillars of OOP and how do Abstraction and Encapsulation differ in purpose and enforcement?
**Answer:**
Core Definition: The 4 pillars of Object-Oriented Programming are Abstraction, Encapsulation, Inheritance, and Polymorphism.

- Abstraction helps manage complexity by hiding intricate implementation details and presenting a simplified high-level model ("You are allowed to look at an object at a high level").
- Encapsulation is the access control enforcer that restricts direct state mutation and shields internal data ("You aren't allowed to look at or alter an object's state directly").

Architecture & Code Pattern:
Achieved by keeping internal state private and exposing behaviors through public interfaces/abstractions:
```csharp
public interface IPaymentProcessor {
    void ProcessPayment(decimal amount);
}
public class StripeProcessor : IPaymentProcessor {
    private string ApiKey { get; set; }
    public void ProcessPayment(decimal amount) {
        ValidateConnection();
        // hidden complex logic
    }
    private void ValidateConnection() { /* ... */ }
}
```

Trade-offs & Best Practices:
- Avoid 'Anemic Domain Models' where objects act merely as data containers with getters/setters, defeating encapsulation.
- Favor composition over deep inheritance hierarchies to avoid fragility and the Diamond Inheritance problem. Always depend on abstractions rather than concrete implementations.


### 🔴 Senior Level

#### 1. What are the 4 Pillars of Object-Oriented Programming (Encapsulation, Abstraction, Inheritance, and Polymorphism), and how do they function together in robust architectural design?
**Answer:**
The 4 Pillars of OOP form the foundation of maintainable, scalable, and decoupled software design.

1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class) while restricting direct access. Promotes information hiding and protects internal state via invariants.
2. Abstraction: Hiding complex implementation details behind a simplified interface. Allows developers to focus on *what* an object does rather than *how*.
3. Inheritance: A mechanism allowing a class (subclass) to inherit fields and methods from another (superclass) to promote code reuse. Caveat: 'Inheritance breaks encapsulation' because subclasses are tightly coupled to superclass implementations. Best Practice: Favor object composition over class inheritance (Composition over Inheritance principle) and keep base class data private.
4. Polymorphism: The ability of different classes to respond to the same method call in unique ways. Achieved via static binding (method overloading) and dynamic binding/dispatch (runtime method resolution via interfaces or virtual methods).

Code Architecture Example:
```java
// Abstraction & Interface
public interface Notifier {
    void send(String message);
}

// Encapsulation & Polymorphism
public class EmailNotifier implements Notifier {
    private final String smtpServer; // Encapsulated internal state

    public EmailNotifier(String smtpServer) {
        this.smtpServer = smtpServer;
    }

    @Override
    public void send(String message) {
        // Implementation details hidden from caller
        System.out.println("Sending via " + smtpServer + ": " + message);
    }
}
```

Trade-offs & Anti-Patterns:
- Deep inheritance hierarchies cause brittle code, tight coupling, and violation of the Open-Closed Principle. Mitigate by using interfaces and abstract classes carefully.
- Overuse of public getters/setters breaks encapsulation, reducing objects to anemic data structures (Anemic Domain Model anti-pattern). Instead, enforce behavior-driven design inside domain models.

#### 2. What are the 4 Pillars of Object-Oriented Programming, and how do principles like encapsulation, abstraction, composition-over-inheritance, and minimized public interfaces apply in production architecture?
**Answer:**
1. Core Definition & Fundamental Concept:
The 4 Pillars of OOP are:
- Encapsulation: Bundling data and methods operating on that data within a single unit (class) and restricting direct access via access modifiers (e.g., private methods/attributes). This protects object integrity.
- Abstraction: Hiding complex implementation details behind a clean, simplified public interface, exposing only what is necessary.
- Inheritance: A mechanism for code reuse and establishing an 'is-a' hierarchy, though modern architecture heavily favors mixins or interface implementation.
- Polymorphism: The ability for different classes to respond to the same method call through a unified interface.

2. Real-world Code Example or Architecture Pattern:
Minimize public APIs and favor composition over deep inheritance. For instance, in an Active Record or domain model, use `attr_reader` for immutable fields and `attr_accessor` only when mutation is strictly required:
```ruby
class Student
  attr_reader :id
  attr_accessor :name, :grade

  def initialize(id: nil, name: '', grade: '')
    @id = id
    @name = name
    @grade = grade
  end
end
```

3. Trade-offs / Best Practices / Anti-patterns:
- Best Practice: Minimize public class members to enforce strict encapsulation, reduce inter-class coupling, and limit external modification vectors.
- Best Practice: Prefer composition over inheritance. Inheritance introduces rigid coupling and base-class fragility. Use composition (or mixins) when sharing behavior or data structures independently.
- Anti-pattern: Deep inheritance hierarchies or violating encapsulation by exposing mutable internal fields directly to external callers.

#### 3. What are the 4 Pillars of Object-Oriented Programming, and how do they enable clean architecture and dependency control?
**Answer:**
Core Definition: The 4 pillars are Encapsulation, Inheritance, Polymorphism, and Abstraction. 
1. Encapsulation: Hiding internal state behind strict public contracts (using getters/setters or private fields) to prevent exposing implementation details to child classes or consumers. If a subclass overrides a routine with an empty implementation, it indicates a violation of the Liskov Substitution Principle and a flawed base class interface (better resolved via composition).
2. Abstraction: Hiding complex implementation details behind clean interfaces (or Abstract Base Classes like Python's `abc` module), exposing only what is necessary.
3. Inheritance: Reusing code and forming type hierarchies, though over-reliance can cause rigid couplings. Favor composition over inheritance to prevent fragile base class problems.
4. Polymorphism: Allowing different classes to be treated through a common interface via dynamic dispatch.

Architecture & Dependency Control:
Through polymorphism, OOP grants absolute control over source code dependencies. This enables an architect to construct a plugin architecture where modules containing high-level domain policies remain entirely independent of low-level infrastructure details (Dependency Inversion Principle).

Best Practices & Anti-Patterns:
- Avoid 'God Classes' that break encapsulation by holding too much mutable state.
- Avoid empty method overrides in subclasses; instead, refactor via composition or the Strategy/Template Method patterns.

#### 4. What are the 4 main tenets (pillars) of Object-Oriented Programming (OOP) and how do they form a cohesive design strategy?
**Answer:**
Core Definition: The 4 pillars of OOP are Abstraction, Polymorphism, Inheritance, and Encapsulation (APIE).

1. Encapsulation: Hiding internal state and requiring all interaction to be performed through a consistent object interface, protecting invariants (e.g., private fields with public methods).
2. Abstraction: Focusing on the essential features of an entity while hiding unnecessary implementation details, often implemented via interfaces and abstract classes.
3. Inheritance: Mechanism for code reuse and hierarchical classification. However, best practice warns against deep inheritance hierarchies due to tight coupling.
4. Polymorphism: Ability of different types to be treated through the same interface via dynamic dispatch, enforcing control over indirect transfer of control.

Architecture & Code Pattern:
Instead of relying solely on deep inheritance trees (which limit orthogonal variation and create tight coupling), favor Composition and the Strategy/Decorator patterns to achieve runtime polymorphism and flexible decoupling.

Trade-offs & Anti-Patterns:
- Anti-pattern: God Objects and Anemic Domain Models that lack encapsulation.
- Best Practice: Depend on abstractions rather than concrete implementations (Dependency Inversion Principle) and enforce strict encapsulation boundaries to maintain predictable domain state changes.

#### 5. What are the 4 pillars of Object-Oriented Programming, and how do they combine with SOLID principles to achieve clean, maintainable architecture?
**Answer:**
1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class), hiding internal state (private fields) and exposing controlled behaviors (public APIs). This prevents invalid states and reduces coupling.
2. Abstraction: Hiding complex implementation details behind a simplified interface (abstract classes or interfaces). It allows systems to evolve without breaking consumers.
3. Inheritance: Mechanism where a class (child/subclass) derives properties and behaviors from another class (parent/superclass). Best Practice: Prefer composition over inheritance to avoid tight coupling and the fragile base class problem.
4. Polymorphism: The ability of different classes to respond to the same message/method call in unique ways (subtype polymorphism via interfaces/virtual methods).

Trade-offs & Best Practices:
- Avoid deep inheritance hierarchies; use interfaces and composition.
- Encapsulation violation (e.g., Anemic Domain Models with public getters/setters everywhere) leads to procedural code scattered across services.
- Apply the Open-Closed Principle (OCP) using polymorphism to ensure code is open for extension but closed for modification.

#### 6. What are the Core 4 Pillars of Object-Oriented Programming, and how do encapsulation, inheritance, polymorphism, and abstraction coordinate to achieve robust system design?
**Answer:**
1. Encapsulation: Bundling data and methods that operate on that data while hiding internal state. Purpose: Achieves changeability, protects component integrity, and reduces system complexity. Avoid anti-patterns like exposing raw mutable state.
2. Inheritance: Mechanism where a class acquires properties of another. Best practice: Prefer object composition over deep inheritance hierarchies. To solve issues like the Diamond Inheritance problem in C++, utilize virtual inheritance:
class A;
class B : virtual public A;
class C : virtual public A;
class D : public B, public C;
3. Polymorphism: Ability to take multiple forms. Runtime polymorphism relies on dynamic dispatch via virtual functions (vtables), whereas compile-time polymorphism leverages techniques like CRTP (Curiously Recurring Template Pattern) to eliminate dynamic dispatch overhead.
4. Abstraction: Hiding complex implementation details behind a clean interface. Component abstraction is measured as $A = Na / Nc$ (ratio of abstract classes/interfaces to total classes).
Trade-offs/Best Practices: Adhere strictly to the Liskov Substitution Principle (LSP) for valid behavioral subtyping and the Dependency Inversion Principle (DIP) to decouple high-level and low-level modules.


## 📂 Category: OOP & Refactoring Patterns (2 cards)

### 🔴 Senior Level

#### 1. What are the core principles, practices, and architectural strategies for executing safe code and database refactoring?
**Answer:**
Core Definition:
Refactoring is the process of altering the internal structure of software to improve readability and reduce modification costs without altering its observable behavior. It is never a dedicated Agile user story, architecture phase, or separate release cycle; rather, it is continuous and opportunistic.

Key Practices & Rules:
1. The 'Two Hats' Metaphor (Kent Beck): Explicitly separate adding functionality (writing new tests/features) from refactoring (restructuring code without adding features).
2. Small, Incremental Steps: Execute very small changes so mistakes are instantly isolated. A solid suite of automated, self-checking tests must always be in place before beginning.
3. The Boy Scout Rule: Leave the codebase cleaner than you found it through small, continuous improvements.

Database vs. Code Refactoring:
Unlike pure application code refactoring which occurs in real-time, database refactoring often spans multiple production deployments to prevent downtime and data loss (e.g., adding a new column, dual-writing to old and new columns, migrating readers, and finally dropping the legacy column).

Trade-offs & Anti-Patterns:
- Avoid refactoring code you do not need to touch or when a complete rewrite is cheaper.
- Dependency Injection can hinder IDE reference tracking and safe refactoring due to indirect wiring.
- Neglecting refactoring leads to technical debt, declining velocity slopes, and fear of breaking legacy code.

#### 2. What is the strategic role of continuous, opportunistic refactoring, and how do self-testing code and CI synergize to support it?
**Answer:**
Core Definition & Fundamental Concept:
Refactoring is the disciplined process of restructuring existing computer code—changing the internal structure without altering its external behavior—to improve readability and reduce complexity. Planned refactoring to pay down neglected technical debt should be rare; instead, refactoring should be continuous and opportunistic (the day-to-day habit of improving code as you work). Taking tiny steps during refactoring prevents regression bugs and eliminates time wasted in heavy debugging.

Real-world Code Example or Architecture Pattern:
A strong synergy exists among Self-Testing Code, Continuous Integration (CI), and Refactoring. Automated tests act as a continuous safety net that fails fast if a structural change breaks functionality. CI complements this by enabling developers to frequently and safely merge and share their micro-refactored code without painful merge conflicts or destabilizing the team's shared codebase.

Trade-offs / Best Practices / How to avoid anti-patterns:
- Best Practice: Always run your test suite before making any structural change and execute it after every tiny step.
- Anti-pattern: Big-bang refactoring without tests or CI, which leads to massive integration hell, extended downtime, and untraceable regressions.


## 📂 Category: Software Design Patterns & Object-Oriented Design (1 cards)

### 🟡 Mid Level

#### 1. What is the Chain of Responsibility design pattern, how does it work, and when should it be used?
**Answer:**
Core Intent & Problem Solved:
A behavioral design pattern that avoids coupling the sender of a request to its receiver by giving multiple objects a chance to handle the request. It chains the receiving objects together and passes the request along the chain until an object handles it or the chain ends. It also relates to the Command pattern, where handlers can be implemented as commands to execute operations over a context object.

Key Components & Structure:
- Handler: An interface defining a method for handling requests and typically a method for setting/getting the next handler in the chain.
- Concrete Handlers: Classes that implement the Handler interface. Upon receiving a request, each concrete handler decides either to process the request or to pass it along to the next handler in the chain. Acts essentially as an object-oriented linked list with recursive traversal.
- Client: Initiates the request to any handler in the chain without needing to know which specific object will ultimately process it.

Use Case / Triggers:
- When your program is expected to process different kinds of requests in various ways, but the exact types of requests and their sequences are unknown beforehand.
- When the set of handlers and their dynamic execution order are supposed to change at runtime.
- When multiple objects may handle a request and the exact handler isn't known a priori.
- When you want to execute several handlers in a particular order, adhering to the Single Responsibility Principle.

Pros, Cons & Trade-offs:
- Pros: Reduces coupling between the sender and receiver, gives you precise control over the order of request handling, adheres to the Single Responsibility Principle (splitting classes that invoke operations from classes that perform them), and adheres to the Open/Closed Principle (introducing new handlers without breaking existing code).
- Cons: Potential request drop-through or drops if no handler explicitly terminates or processes the chain; debugging and tracing can be difficult due to the dynamic runtime execution path.

