# *0x06. Regular expression*

`Regex`   `DevOps`

By: Sylvain Kalache

## *Concepts:*

For this project, we expect you to look at this concept:

- [Regular Expression](https://intranet.alxswe.com/concepts/29)

## *Resources:*

Read or watch:

- [Regular expressions - basics](https://fr.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://fr.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com)

## *Tasks:*

#### [0. Simply matching School](0-simply_match_school.rb)

<img width="969" alt="ec65557f0da1fbfbff6659413885e4d4822f5b1d" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/4cbb52a6-83e3-475d-a8f3-8216b5270c27">

Requirements:

- The regular expression must match `School`
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

    
#### [1. Repetition Token #0](1-repetition_token_0.rb)

<img width="959" alt="e7db3c377d46453588fc84f3a975661d142fee91" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/c7ab44e8-35ae-4337-81a4-750a6238fb7a">

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

#### [2. Repetition Token #1](2-repetition_token_1.rb)

<img width="967" alt="c59ff11db195d5cf17d1790a5141ae2f234786d2" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/acc82852-f00b-4780-a21b-fd03ddb31326">

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

#### [3. Repetition Token #2](3-repetition_token_2.rb)

<img width="974" alt="3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/e90eb29a-2e4d-4fee-953f-c2c782dafdd9">

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
    
#### [4. Repetition Token #3](4-repetition_token_3.rb)

<img width="956" alt="f8dbcb9cf5ae569a8645027dc46e81cb372ce28e" src="https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/0c5d217a-6f94-43cc-9f6a-8db701af08a1">

Requirements:

- Find the regular expression that will match the above cases
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Your regex should not contain square brackets

#### [5. Not quite HBTN yet](5-beginning_and_end.rb)

Requirements:

- The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
 
#### [6. Call me maybe](6-phone_number.rb)

This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.

Requirement:

- The regular expression must match a 10 digit phone number


#### [7. OMG WHY ARE YOU SHOUTING?](7-OMG_WHY_ARE_YOU_SHOUTING.rb)

![image](https://intranet.alxswe.com/images/contents/sysadmin/projects/78/shouting.jpg)

Requirement:

- The regular expression must be only matching: capital letters



#### [8. Textme](100-textme.rb)

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

- Your script should output: `[SENDER]`,`[RECEIVER]`,`[FLAGS]`
   - The sender phone number or name (including country code if present)
   - The receiver phone number or name (including country code if present)
   - The flags that were used

