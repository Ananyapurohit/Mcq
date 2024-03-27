questions = ("What is encapsulation in OOP?: ",
             "Which OOP concept allows a class to have multiple methods with the same name but different parameters?: ",
             "Which OOP concept allows a class to inherit properties and behaviors from more than one class?: ",
             "Which of the following is NOT a principle of OOP?: ",
             "What is the main advantage of using interfaces in OOP? ",
             "Inheritance in OOP is used for: ",
             "What is a constructor in OOP?: ",
             "In OOP, what is a class?: ",
             "Which OOP principle suggests that a derived class should be able to substitute its base class without affecting the program's correctness?: ",
             "What is the purpose of the 'new' keyword in OOP languages like Java or C#?: ",
             "What is the purpose of the 'interface' in OOP?: ",
             "In OOP, what does the term 'composition' refer to?: ",
             "What is the purpose of the 'static' keyword in OOP languages like Java?: ",
             "What is the purpose of the 'try-catch' block in exception handling in OOP languages?: ",
             "Which OOP concept allows a class to have more than one method having the same name, same parameters, and different return types?: ",
             "What is the concept of 'method overloading' in OOP?: ",
             "In the context of OOP, what is a 'covariant return type'?: ",
             "What is the purpose of the 'friend' keyword in C++ in the context of OOP?: ",
             "What is the significance of the 'virtual' keyword in C++ in the context of OOP?: ",
             "What is the purpose of the 'sealed' keyword in C# in the context of OOP?: ",
             "In C++, what is the role of a destructor in the context of OOP?: ",
             "What is the concept of 'covariance' in the context of OOP, and how is it related to type compatibility?: ",
             "In C++, what is the purpose of the 'const' keyword when used in method declarations?: ",
             "What is the difference between shallow copy and deep copy in the context of object-oriented programming?: ",
             "What is the purpose of the 'super' keyword in Python in the context of OOP?: ",
             "What is the role of the 'interface' keyword in C# in the context of OOP?: ",
             "What is the role of the 'throw' keyword in Java in the context of OOP?: ",
             "In C#, what is the significance of the 'protected' access modifier in the context of OOP?: ",
             "Consider the concept of 'template classes' in C++. What are they, and how do they contribute to generic programming in OOP?: ",
             "In C#, what is the purpose of the 'base' keyword in the context of OOP?: ",
             "Consider the concept of 'delegates' in C#. What are they, and how do they contribute to event-driven programming in OOP?: ",
             "In Python, what is the purpose of the 'init' method in a class, and how does it relate to constructors in other OOP languages?: ",
             "What is the concept of 'method overriding' in OOP, and how does it contribute to polymorphism?: ",
             "What is the role of the 'this' keyword in OOP languages like C# or Java?: ",
             "In the context of OOP and modern design patterns, what does 'Dependency Injection' refer to?: ",
             "What is the purpose of the 'async' and 'await' keywords in modern OOP languages like C# and Python?: ",
             "In modern OOP development, what is the primary goal of using the 'Immutable Objects' pattern?: ",
             "What does the term 'IoC Container' stand for in the context of modern OOP frameworks?: ",
             "In the context of modern OOP and SOLID principles, what does the 'S' in SOLID stand for?: ",
             "What is the primary purpose of the 'Builder Pattern' in modern OOP design?: ",
             "In modern OOP languages like Python, what is the purpose of the 'dataclass' decorator?: ",
             "In modern OOP, what is the significance of the 'Decorator Pattern'?: ",
             "What does the term 'Microservices' refer to in the context of modern software architecture and OOP?: ",
             "In modern OOP, what is the role of the 'Mixin' pattern?: ",
             "What is the primary goal of the 'Domain-Driven Design (DDD)' approach in modern OOP practices?: ",
             "What is the primary purpose of the 'CQRS (Command Query Responsibility Segregation)' pattern in modern OOP architectures?: ",
             "In modern OOP, what is the primary goal of the 'Functional Programming' paradigm?: ",
             "What is the significance of the 'Fluent Interface' pattern in modern OOP design?: ",
             "What is the purpose of the 'JWT (JSON Web Token)' in modern OOP applications, particularly in web development?: ",
             "What does the term 'Agile Development' refer to in the context of modern software development and OOP?: ")

options = (("A. Combining different data types", "B. Bundling data and methods that operate on the data", "C. Creating instances of a class", "D. Using inheritance to extend functionality"),
           ("A. Inheritance", "B. Polymorphism", "C. Abstraction", "D. Encapsulation"),
           ("A. Multiple inheritance", "B. Multilevel inheritance", "C. Hierarchical inheritance", "D. Single inheritance"),
           ("A. Inheritance", "B. Polymorphism", "C. Synchronization", "D. Encapsulation"),
           ("A. Implementing multiple inheritances", "B. Providing a way to achieve multiple polymorphism", "C. Restricting access to class members", "D. Enforcing a contract for classes that implement the interface"),
           ("A. Combining two unrelated classes", "B. Creating a new class with the same attributes and behaviors of an existing class", "C. Accessing private members of a class", "D. Implementing interfaces"),
           ("A. A method used to destroy objects", "B. A method with the same name as the class used to initialize object's state", "C. A method used to access static members", "D. A method used for polymorphism"),
           ("A. An object", "B. A blueprint for creating objects", "C. A method", "D. A variable"),
           ("A. Encapsulation", "B. Polymorphism", "C. Liskov Substitution Principle", "D. Abstraction"),
           ("A. Creating a new class instance", "B. Allocating memory for an object" , "C. Declaring a new method", "D. Accessing static members"),
           ("A. Defining a set of methods that must be implemented by a class", "B. Creating a new instance of a class", "C. Accessing static members of a class", "D. Providing a way to achieve multiple inheritance"),
           ("A. Combining multiple classes into a single class", "B. Creating objects within objects", "C. Implementing multiple interfaces", "D. Using static methods"),
           ("A. Declaring a constant variable", "B. Allocating memory for an object", "C. Indicating that a method belongs to the class rather than an instance", "D. Creating an immutable class"),
           ("A. To declare a new exception", "B. To handle runtime errors and exceptions", "C. To define a custom exception class", "D. To check if an exception has occurred"),
           ("A. Overloading", "B. Overriding", "C. Polymorphism", "D. Abstraction"),
           ("A. Defining multiple methods with the same name but in different classes.", "B. Defining multiple methods with the same name but with different parameters in the same class.", "C. Overriding a method in a subclass to provide a different implementation.", "D. Restricting access to certain methods in a class."),
           ("A. A return type that is dependent on the parameters passed to the method.", "B. A return type that is the same or a subtype of the declared return type in the superclass method.", "C. A return type that is the opposite of the declared return type in the superclass method.", "D. A return type that is independent of the class hierarchy."),
           ("A. It allows a function or class to access private and protected members of another class.", "B. It designates a class as a singleton.", "C. It denotes a function as a friend to the garbage collector.", "D. It specifies that a class cannot be inherited."),
           ("A. It denotes a class as abstract.", "B. It designates a method as a candidate for overloading.", "C. It indicates that a method can be overridden in a derived class.", "D. It marks a method as static."), 
           ("A. It prevents a class from being instantiated.", "B. It restricts inheritance, ensuring that no other class can derive from the sealed class.", "C. It specifies that a method cannot be overridden in a derived class.", "D. It marks a class as a singleton."),
           ("A. It is used to create objects of a class.", "B. It is responsible for cleaning up resources and releasing memory when an object goes out of scope or is explicitly deleted.", "C. It is a special method used to initialize an object before its first use.", "D. It is used for overloading operators in a class."),
           ("A. Covariance allows the assignment of a derived class object to a base class reference or pointer, ensuring type compatibility.", "B. Covariance is the opposite of contravariance and only allows assignment of a base class object to a derived class reference or pointer.", "C. Covariance is unrelated to type compatibility in OOP.", "D. Covariance allows the assignment of objects between unrelated classes, breaking type compatibility."),
           ("A. It indicates that the method cannot be overridden in a derived class.", "B. It specifies that the method does not modify the state of the object, allowing it to be called on const objects.", "C. It is used to define constant variables within the method.", "D. It marks a method as static."),
           ("A. Shallow copy duplicates only the references, while deep copy duplicates both the references and the objects themselves.", "B. Shallow copy duplicates the objects, while deep copy duplicates only the references.", "C. Shallow copy and deep copy are interchangeable terms.", "D. Shallow copy and deep copy are only applicable in functional programming languages."),
           ("A. It refers to the superclass and is used to call its methods or constructors.", "B. It denotes a static method.", "C. It is used to initialize instance variables.", "D. It specifies that a class cannot be inherited."),
           ("A. It denotes a class as an interface.", "B. It is used to declare constant variables.", "C. It designates a method as an interface.", "D. It declares an interface, providing a contract for implementing classes."),
           ("A. It is used to declare a new exception.", "B. It indicates the end of a try-catch block.", "C. It denotes a class as throwable.", "D. It is used for method overloading."),
           ("A. It allows access only within the same class.", "B. It allows access within the same class and its derived classes.", "C. It allows access only within the same assembly.", "D. It restricts access to the class."),
           ("A. Template classes allow creating classes with generic types, contributing to code reusability and flexibility in data types.", "B. Template classes are not supported in C++.", "C. Template classes are classes with static methods only.", "D. Template classes are synonymous with abstract classes."),
           ("A. It is used to declare a base class.", "B. It refers to the current object instance.", "C. It is used for exception handling.", "D. It refers to the superclass in a derived class and is used to access its members."),
           ("A. Delegates are not applicable in C#.", "B. Delegates allow representing and passing methods as objects, contributing to event-driven programming by providing a mechanism for callbacks.", "C. Delegates are used for operator overloading.", "D. Delegates are only used for defining constant variables."),
           ("A. The 'init' method is used for creating instances of a class and is equivalent to a constructor in other languages.", "B. The 'init' method is used for destructing instances of a class.", "C. The 'init' method is deprecated in Python.", "D. The 'init' method is not related to OOP."),
           ("A. Method overriding allows a derived class to provide a new implementation for a method defined in its base class, contributing to polymorphism by enabling dynamic method resolution.", "B. Method overriding is not supported in OOP.", "C. Method overriding and method overloading are interchangeable terms.", "D. Method overriding is used to hide the implementation details of a class."),
           ("A. It refers to the current object instance and is used to distinguish instance variables from local variables with the same name.", "B. It denotes a static method.", "C. It is used for exception handling.", "D. It marks a method as final and prevents overriding."),
           ("A. Injecting dependencies through setter methods.", "B. Injecting dependencies through constructor parameters.", "C. A mechanism to automatically resolve dependencies at runtime.", "D. A technique to eliminate dependencies altogether."),
           ("A. They are used for operator overloading.", "B. They are used to create instances of a class.", "C. They facilitate asynchronous programming by allowing non-blocking execution of tasks.", "D. They are part of the 'const correctness' feature."),
           ("A. To create objects that can be modified after instantiation.", "B. To optimize memory usage in objects.", "C. To improve thread safety and eliminate the need for synchronization.", "D. To allow dynamic method resolution."),
           ("A. Interface of Classes Container", "B. Inheritance over Composition Container", "C. Instance of Class Container", "D. Inversion of Control Container"),
           ("A. Singleton Responsibility", "B. Single Responsibility", "C. Solidarity", "D. Secure Responsibility"),
           ("A. To build user interfaces.", "B. To facilitate the construction of complex objects by separating the construction process from the actual representation.", "C. To build database queries.", "D. To create instances of a class."),
           ("A. It marks a class as a data structure.", "B. It is used for operator overloading.", "C. It is part of the 'const correctness' feature.", "D. It allows the automatic generation of special methods, such as init and repr, based on class attributes."),
           ("A. It is used for operator overloading.", "B. It allows adding new functionalities to objects dynamically by placing them inside special wrapper classes.", "C. It is used for creating instances of a class.", "D. It is part of the 'const correctness' feature."),
           ("A. Extremely small classes in an object-oriented system.", "B. A software architectural style that structures an application as a collection of loosely coupled services.", "C. A set of tiny functions within a class.", "D. Micro-level encapsulation in classes."),
           ("A. It allows the inclusion of multiple classes in a single class to provide a combination of behaviors.", "B. It is part of the 'const correctness' feature.", "C. It is used for creating instances of a class.", "D. It denotes a method as a mixin."),
           ("A. To create abstract classes.", "B. To focus on the design of the business domain rather than technical details.", "C. To design classes based on implementation details.", "D. To optimize memory usage in objects."),
           ("A. To create instances of a class.", "B. To separate the concerns of handling commands from handling queries in the application.", "C. To optimize memory usage in objects.", "D. To achieve single responsibility in classes."),
           ("A. To create instances of a class.", "B. To optimize memory usage in objects.", "C. To treat computation as the evaluation of mathematical functions and avoid changing-state and mutable data.", "D. To achieve single responsibility in classes."),
           ("A. It marks a class as a fluent interface.", "B. It allows creating instances of a class.", "C. It is used for operator overloading.", "D. It enables method chaining to create a more readable and concise code structure."),
           ("A. To create instances of a class.", "B. To optimize memory usage in objects.", "C. To securely transmit information between parties as a JSON object.", "D. To achieve single responsibility in classes."),
           ("A. A programming paradigm.", "B. A set of practices for iterative and incremental software development.", "C. A design pattern.", "D. A class hierarchy.")
           
)

answers = ("B", "B", "A", "C", "D", "B", "B", "B", "C", "B", "A", "B", "C", "B", "A", "B", "B", "A", "C", "B", "B", "A", "B", "A", "A", "D", "A", "B", "A", "D", "B", "A", "A", "A", "B", "C", "C", "D", "B", "B", "A", "B", "B", "A", "B", "B", "C", "D", "C", "B")    
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")