ULTRA THINK

DON'T EDIT SOURCE SUBJECT TEST (IMPORTANT, ULTRA THINK).
Update or create a java unit test for the following code and ensure complete coverage of the code to reach 100% coverage. If there are updates to unit tests to improve coverage, do not create a new unit test file; update the existing unit test file instead. Mocking must be used if there are function calls using org.mockito.MockedStatic or stubber org.mockito and using @ExtendWith(MockitoExtension.class). If you need to create mocking and encounter a reference from instance creation like `new ClassName()`, don’t create mocking, as this cannot be mocked. Make sure all fields, functions, etc. are properly mocked to avoid getting a errors (such as NullPointerException, etc).
**IMPORTANT, ULTRA THINK ON THIS** After update or create a java unit test, please run the unit test, current coverage and uncoverage tests. Update the unit test to cover the uncovered tests to achieve 100% coverage.
If any functions, fields, or other elements have not been mocked yet, be sure to create the required mocks first.
If there is uncovered test like `public class ClassName {`.  This is a class declaration, which is not directly executable and cannot be covered by tests. However, SonarQube may sometimes report such lines as uncovered if there are no explicit usages (e.g., no constructor called. Completed covered using Private constructor to prevent instantiation. 

When shoud you use mock or spy? If you want to be safe and avoid calling external services and just want to test the logic inside of the unit, then use mock. If you want to call external service and perform calling of real dependency, or simply say, you want to run the program as it is and just stub specific methods, then use spy.
When to Use Mock:
Ideal for isolating the unit under test without executing real code. Useful when the object has external dependencies (e.g., database calls, API requests). Best suited for testing interactions rather than actual method execution.
When to Use Spy:
Allows testing real behavior while mocking specific methods. Useful when only certain methods need to be overridden, while others retain their actual implementation. Helps verify interactions, such as tracking calls to real methods like add().