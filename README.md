#### Aryan Sharma (ash288)

print coverage:

This is a common function that i have used for both of the funcitons to check the coverages! :)
![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/3167bc03-2dcb-4506-aa6b-0ba7d4564b61)


##### 1.django/http/request.py -> get_signed_cookie() 

I used dictionaries to monitor and and update the coverage status of the conditional branches as the program executed:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/3cc33e45-1749-4836-86b3-0c98cc7ebf3d)

The get signed cookies had 4 branches in that it could go to which were the if and the elses of all the try blocks and I added flags to determine whether they had been executed or not:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/2e9aa9d9-b0a8-4ed7-bdee-a5bf7eb9285f)

As is observable, each of the flags get triggered if the branch is executed. I have also created a print_coverage() function to print the coverage information to the console. Once that was completed, I ran the following command to the console:


`coverage run ./runtests.py --settings=test_sqlite signed_cookies_tests`

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/5134c5c1-dac1-4c6a-b88e-6f688bb75109)
>

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/cf8a989a-9b7d-48b2-b82a-6f0e749ef43f)

This shows that out of the 4 paths, 2 paths are being covered and the other 2 branches are not being executed. at the moment only branch 3 and 4 are being reached.

To measure branch coverage, the following formula is used:

`number of executed branches / total number of branches x 100`

For this function, the number of executed branches is 2 and the total number of branches is 4. Following this:

`2 / 4 x 100 = 50%`

So the current total branch coverage is 50% . Using this coverage instrumentation, it is now possible to determine the sections of the function that need enhanced testing to increase branch coverage.

The link to the relevant commit regarding the instrumented code used to make the coverage measurements can be found below:

[Relevant commit](https://github.com/Aryansharma28/django_SEP/commit/67e9e3f7e2c24ab9b9cd9241162dc609f4f4b5a0#diff-c16850633accaf26c845d9ad94325d4fd296af7fdf63d79836cb55b69d2cd75c)

##### 2. django/contrib/auth/tokens.py
The data structure I chose to hold the coverage information about the conditional branches was a dictionary, which is visible here:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/cab62908-9ce7-4398-898f-5d4c461f17c9)

The function at hand had 8 main branches, for each of which I added flags to determine whether they had been executed or not:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/d13df04f-d7e5-47bb-b282-f801db7782e1)

As is observable, each of the flags get triggered if the branch is executed. I have once again, created a print_coverage() function like above to print the coverage information to the console . Once that was completed, I ran the following command to the console:

'coverage run ./runtests.py --settings=test_sqlite auth_tests'

![Screenshot 2024-06-27 210508](https://github.com/Aryansharma28/django_SEP/assets/89016404/57ff8ba6-824d-4086-9f26-1ac0e3378741)

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/a4ab7d24-97a7-4559-8a2b-2cdb4e08ae40)

Each of these represents one of the 8 branches, and showcases whether they are being executed or not. At the moment the only branch that is not being reached is that of branch 2 and branch 3, that is, the branch where it is tested if the loader that was fetched from the template backend has a 'get_dirs' method or not. 

To measure branch coverage, the following formula is used:

`number of executed branches / total number of branches x 100`

For this function, the number of executed branches is 6 and the total number of branches is 8. Following this:

`6 / 8 x 100 = 75%`

So the current total branch coverage is 75%. Using this coverage instrumentation, it is now possible to determine the sections of the function that need enhanced testing to increase branch coverage.

The link to the relevant commit regarding the instrumented code used to make the coverage measurements can be found below:

[Relevant commit](https://github.com/Aryansharma28/django_SEP/commit/67e9e3f7e2c24ab9b9cd9241162dc609f4f4b5a0#diff-b93dda4cd6422ff34822c0dcb5f4d89f4c9634093c4220f9acd267535b007be4)


###Coverage improvement

###Aryan Sharma(ash288)

#####1.C:\Users\aryan\Desktop\sep\django\tests\signed_cookies_tests\tests.py

Previously the the function had a 50% branch coverage and now we have got it to 100% coverage.Once I had identified which branches required further testing to achieve this, and implemented it as demonstrated in the link provided above, I ran the command again:
   
`coverage run ./runtests.py --settings=test_sqlite signed_cookies_tests`

![Screenshot 2024-06-27 214006](https://github.com/Aryansharma28/django_SEP/assets/89016404/b18fd90d-ce34-4e23-9fe4-e7194753bddf)

For this function, my aim was to reach 100% coverage. Once I had identified which branch required further testing to achieve this, and implemented it as demonstrated in the link provided above, I ran the coverage tool again:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/86708a21-e4bb-43ee-bff4-26d129739d6c)

To acheieve 100% coverage. we first create a Django HttpRequest object to simulate a web request. We then test two scenarios for the get_signed_cookie method: one where we provide a default value for a non-existent cookie, and another where we don't provide a default. For the first scenario, we verify that the method returns the provided default value when the cookie doesn't exist. For the second scenario, we check that the method raises a KeyError when no default is provided and the cookie is missing. These tests ensure that the get_signed_cookie method handles missing cookies correctly, either by returning a default value or raising an exception as appropriate.

[<link relevant commit>](https://github.com/Aryansharma28/django_SEP/commit/67e9e3f7e2c24ab9b9cd9241162dc609f4f4b5a0#diff-f0e5c460b951110bdc3b7967ed2a4c924ae8f093affc27cdd581939d18988725)
 
#####2.\tests\auth_tests\test_tokens.py --> test_check_token_exceptions()

Previously the the function had a 80% branch coverage and now we have got it to 100% coverage.Once I had identified which branches required further testing to achieve this, and implemented it as demonstrated in the link provided above, I ran the command again:

coverage run ./runtests.py --settings=test_sqlite auth_tests

From this, here are the new coverage results:

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/e3082948-e778-489e-bf5a-1f43ce0a23a2)

The branch coverage has improved to 100%. This test function verifies the check_token method's ability to handle invalid tokens. It creates a test user and checks four scenarios: tokens without hyphens, with multiple hyphens, with invalid characters, and with valid format but invalid content. By asserting all cases return False, it ensures the method correctly rejects various types of invalid input, crucial for password reset security. after rerunning the coverage we can see that all the branches are now covered

![image](https://github.com/Aryansharma28/django_SEP/assets/89016404/0477bf6f-e432-4647-bca1-65dc8429bf8a)

[Commit to view tests](https://github.com/Aryansharma28/django_SEP/commit/67e9e3f7e2c24ab9b9cd9241162dc609f4f4b5a0#diff-bc4d1f01b0cb354b10be00c5737ffaeca369fc62b0c691f0c01514eac98e8458)

## Statement of individual contributions

### Aryan Sharma (ash288)
- Increased the coverage of both functions 100% by enhancing the test cases to ensure higher branch coverage
- actively participated in group discussions and attempted to add as much value to the team as possible.
- Researched and learnt a lot and shared a lot of knowledge regarding this assignment!
- Aided in completeing the report









