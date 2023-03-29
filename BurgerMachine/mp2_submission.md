<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Neil Patel (np656)</td></tr>
<tr><td> <em>Generated: </em> 3/28/2023 11:34:12 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/np656" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228417837-b2708732-bb44-4e94-96b4-e749006d0e13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code of calculate_cost()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228417905-b7dedeb0-cebe-4a29-a1ca-4722d01cac11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing correct format output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>This code calculates the total cost of a burger based on the cost<br>of each item in the &quot;inprogress_burger&quot; list. The sum() function is used to<br>add up the costs of each item, and the result is formatted as<br>a string with two decimal places. Finally, the total cost is returned as<br>a float value. The most important part of the code is getting the<br>sum of the ingredients. I solved this problem by creating a for loop<br>that goes through every item in&nbsp;<span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>color: rgb(156, 220, 254);">self</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">.</span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;<br>color: rgb(156, 220, 254);">inprogress_burger </span>and getting the sum in the sum(). In the<br>print statement &quot;<span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(220, 220,<br>170);">print</span><span style="background-color: rgb(30, 30, 30); color: rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; white-space: pre;">(</span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(86, 156,<br>214);">f</span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(206, 145, 120);">&quot;Total cost<br>of burger: $</span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(86, 156,<br>214);">{</span><span style="font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(156, 220, 254);">total_cost</span><span style="font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre; color: rgb(86, 156, 214);">:.2f}</span><span style="font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre; color: rgb(206, 145, 120);">&quot;</span><span style="background-color: rgb(30, 30, 30); color:<br>rgb(212, 212, 212); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">)</span>&quot;, the hardest part<br>was getting the formating. My problem was that I forget how the formating<br>worked. But i was able to solve it. The solution was calling the<br>sum of the cost from the for loop, then using the formating :.2f,<br>which calls the output to be a float that shows the first 2<br>decimal places.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418061-10a0e95c-a8a5-4d5c-91ef-e4f6aa3880d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>exceptions part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418093-1684f549-1ae1-4d97-98ba-a77e2eabcde6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>exceptions part 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;OutOfStockException: This exception raises when the quantity of an ingredient runs out, resulting<br>in being unable to ask for it when ordering.&nbsp;<div>NeedsCleaningException: This exception is raised<br>when there has been many orders done and the burger machine needs to<br>be clean.</div><div>InvalidChoiceException: This exception is raised when a user makes an invalid choice<br>or selection when ordering.</div><div>ExceededRemainingChoicesException: This exception is raised when the user exceeds the<br>remaining choices or limit, such as selecting more ingredients than available.</div><div>InvalidPaymentException: This exception<br>is raised when a payment method or transaction is invalid or cannot be<br>processed.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418183-2eb0a8f9-1f80-43de-b1ab-085dc0e7a075.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418245-3165da1c-784d-4399-a2da-5aa6a24aad98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418307-3cab25f1-8574-431e-a970-16282ab68799.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases part 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418356-98fba457-805c-476a-972c-49fcd4f1ad82.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test cases part 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418420-71d5e547-5ece-4ecf-9f0e-ed209c6f8458.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of all test cases working<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test 1:This test was to test that an invalid stage exception will occur<br>when trying to order toppings/patty <div style="line-height: 19px;"><div>before choosing the bun first</div><div><br></div></div><div>Test 2:This<br>test was to test when adding patties to the order, an out of<br>stock exception will rise when<br></div><div style="line-height: 19px;"><div>there is no more stock of a<br>patty</div><div><br></div></div><div>Test 3:test was to test when adding toppings to the order, an out<br>of stock exception will rise when<br></div><div style="line-height: 19px;"><div>there is no more stock of<br>a topping</div><div><br></div></div><div>Test 4:This test was to test the ordering of any 3 patties<br>in any order and giving a exceeded remaining choices<br></div><div style="line-height: 19px;"><div>exception when trying<br>to add a 4th patty</div><div><br></div></div><div>Test 5:This test was to test that when ordering<br>burger, if a person order more toppings then they<br></div><div style="line-height: 19px;"><div>are allowed to,<br>an exceed remaing choices error will occur</div><div><br></div></div><div>Test 6:This test was to test when<br>ordering a burger, if the correct payment to the price of the burger<br>is made, no<br></div><div style="line-height: 19px;"><div>error will occur</div><div><br></div></div><div>Test 7:This test was to test that<br>when multiple people order burgers, the machine will track the total sales of<br></div>&lt;div<br>style=&quot;line-height: 19px;&quot;&gt;<div>all the brugers</div><div><br></div></div><div>Test 8:This test was to test that when ordering multiple<br>burgers, the machine will track the total amoount of burgers made</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/24">https://github.com/neilpatel13/IS601-004/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Overall this project was pretty solid, I think doing this problem helped gave<br>me a better understanding of formating and uses exceptions. The biggest issue I<br>faced was understanding how to use the object&#39;s data type to create the<br>exception. One problem I did face was that because I didn&#39;t take the<br>time to read through the entire base code, i had to trouble trying<br>to create some of the exceptions, but after taking time to understand the<br>base code, it helped make the problems easier. While I did face some<br>issues, I was able to navigate them.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228417698-2c45a694-c453-476b-99f9-1ec376064d8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfull run through of the machine, ordering a burger correctly then quitting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/228418781-bf6f9117-6eb2-47c2-b047-d3f0d1e9ab6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ordering multiple burgers<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-2-burgers/grade/np656" target="_blank">Grading</a></td></tr></table>