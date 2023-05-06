<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Neil Patel (np656)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 9:42:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/np656" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236589812-b9d716f2-5e73-42ca-92f8-c4693ac85971.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transfer page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236589837-5f02d7ca-b045-41bf-9717-0b4566a77622.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing dropdown in transfer page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236589867-3a60bdba-133d-4aa3-8bb5-739a869a28a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure transfering money more than what account holds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236589901-831f348e-dc22-4c59-9342-67121f1bc8a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cannot transfer money to same account pt1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236589930-4449382f-2591-4ba9-82d2-f2e58cde57bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cannot transfer money to same account pt2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590008-733920fb-4ca9-4869-a923-6e62eed79e17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cannot transfer negative money<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590089-4dc0882d-041c-4c84-a740-96930decac7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing successfull transfer in db, last 2 transactions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590130-7dee7a75-9929-4014-8bf4-88834a2ffa90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Accounts table showing both affected accounts: hero and person<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590801-1b560400-d3aa-44f1-8afe-1fc1a981f085.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sucessfull transfer in accounts page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p>In a brief steps, the transfer page by first the user selecting which<br>accounts they want to transfer money between in the form dropdown menu, then<br>the page checks if the accounts are not the same. When a sucessufull<br>goes through, the money is subtracted from the sender and added to the<br>reciever. The database gets updated while the transactions finshed showing in the transaction<br>history and the updated funds in the accounts table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/46">https://github.com/neilpatel13/IS601-004/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/accounts/transfer/">https://np656-is601-prod.herokuapp.com/accounts/transfer/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590130-7dee7a75-9929-4014-8bf4-88834a2ffa90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the Accounts table showing both affected accounts: hero and person<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236590846-2290da62-66c8-492e-94b3-598dffc21da0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>having deposit filter on<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>Pagination is used to create sorts and filters for users to use to<br>see different types of transactions in the transaction history. Some filters of type<br>of account, date of transfer.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/46">https://github.com/neilpatel13/IS601-004/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/accounts/details/374509707684?from_date=&to_date=&type=deposit">https://np656-is601-prod.herokuapp.com/accounts/details/374509707684?from_date=&to_date=&type=deposit</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/46">https://github.com/neilpatel13/IS601-004/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236591000-1ff756c1-7a27-4c58-a4b6-3641f67c7854.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transfer to different user account<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236591072-30581d9a-16c1-4e60-a149-c2fe0054c403.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>fail transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236591056-6cfbe113-fe15-435b-b7bf-b23b3a2592db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>negative money transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236591072-30581d9a-16c1-4e60-a149-c2fe0054c403.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>fail transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/46">https://github.com/neilpatel13/IS601-004/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/accounts/transfer/">https://np656-is601-prod.herokuapp.com/accounts/transfer/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Overall this milestone was harder than milestone 2, but still enjoyable. The hardest<br>part to this milestone was figuring out how to check accounts of the<br>same user and accounts of different users. I was unable to figure out<br>how to check accounts between different users, but I was able to figure<br>out how to check accounts. Like Milestone 2, the least troublesome parts for<br>me was dealing with the sql queries from the experience I had with<br>them in ms2 and miniproject 3. Another point where I struggles with was<br>designing the template, I wasn&#39;t sure if the trasnfer accounts had to be<br>one page with both transfers options or two seperate pages, but i decided<br>to try implementing jinja into my template page to hold both transfer option.<br>Resources that helped use jinja in a html file was stack overflow.<div>LINKS:&nbsp;<a href="https://cs50.stackexchange.com/questions/41927/jinja-code-not-working-inside-html-file">https://cs50.stackexchange.com/questions/41927/jinja-code-not-working-inside-html-file</a></div><div><a href="https://stackoverflow.com/questions/tagged/jinja2">https://stackoverflow.com/questions/tagged/jinja2</a><br></div><div><br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-3-bank-project/grade/np656" target="_blank">Grading</a></td></tr></table>