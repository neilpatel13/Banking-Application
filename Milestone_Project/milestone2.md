<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Bank Project</td></tr>
<tr><td> <em>Student: </em> Neil Patel (np656)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 4:24:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/np656" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Create Accounts table and setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot from the db of the system user (Users table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236511481-161e97b1-818b-471c-b3eb-d8ef50b9f796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot from the db of the world account (Accounts table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236511557-f89c91e0-0e59-4247-8e94-35ae3fd9eb0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Account Table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain the purpose and usage of these two entries and how they relate</td></tr>
<tr><td> <em>Response:</em> <div><p style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0;<br>--tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position:<br>; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ;<br>--tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent;<br>--tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; margin-bottom: 1.25em;">The users and accounts table are needed for transactions<br>because they store information about the users who own the accounts and the<br>accounts themselves. When a transaction takes place, money is moved from one account<br>to another. The system needs to know&nbsp; the account numbers and balances of<br>both the sender and the receiver in order to complete this transfer. The<br>accounts table contains a record for this information. In order to impose security<br>and access rules, the system also requires knowledge of the user's identity who<br>is the owner of each account. The users table has a record for<br>this data. The system can determine the accounts and users involved in a<br>transaction by running queries against these two columns, ensuring that the transaction is<br>allowed and accurately documented. In turn, the accounts table is used to hold<br>the account information for bank transactions while the user tables are used to<br>hold user information for user interactions and creating accounts.</p></div><div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Dashboard </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the requested links/navigation</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236549757-14423e82-18b8-4920-ae99-491845c8f118.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>dashboard in index page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain which ones are working for this milestone</td></tr>
<tr><td> <em>Response:</em> <p>In this current project, all links work. Due to submitting this project on<br>the last day, there will be some elements in milestone 3 in milestone<br>2. All links&nbsp; work, The Create Account link leads to the create account<br>page. The my account link leads to the accounts page where it shows<br>all the accounts the user have. The deposit link leads to the deposit<br>page where the user can deposit money from an account. The withdraw link<br>is the same as the deposit, but instead users can withdraw money. The<br>transfer link leads to the transfer page where the user can transfer money<br>between accounts.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Create a checking Account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the Create Account Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236549921-c6602dad-5b9c-4d8e-aa92-1446cfb6f2d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create Account Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots showing validation errors and success message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236549999-fe25e16d-84db-408c-b574-273fde229b3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>less the minimum amount when creating account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236550051-e01387f9-5fe8-4ce2-b143-13b9d94a8da1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success load<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the transaction generated from the initial deposit (from the DB)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236550863-96b03272-d0ea-409d-914d-bb9e209cf061.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing account creation, account is called hero<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236550803-86ac32b5-80e3-468e-a971-cfcbf3d9effb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing account creation in transaction history table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain which account number generation you used and the account creation process including the transaction logic</td></tr>
<tr><td> <em>Response:</em> <p><span id="docs-internal-guid-afe45ca9-7fff-640f-e320-d35b0bee598a"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; vertical-align: baseline;">When doing the number<br>generation, I did Option 1:</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; font-variant-alternates: normal; vertical-align: baseline;"><br>Generate a random 12 digit/character value; must regenerate if a duplicate collision occurs,<br>from the proposal.</span></span><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/">https://np656-is601-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to list their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's account list view (show 5 accounts)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551190-34f3b872-b462-41b1-9e1a-994df17d5e9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>accounts page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the page is displayed and the data lookup occurs</td></tr>
<tr><td> <em>Response:</em> <p>The main way how to retrieves account information from the database for the<br>currently logged-in user and renders the &quot;my_account.html&quot; template with that information is by<br>first, it retrieves account information for the currently logged-in user by executing a<br>SELECT statement on the &quot;IS601_Accounts&quot; table with a WHERE clause that filters accounts<br>belonging to the current user. Where it says LIMIT 10, it is for<br>limiting to numbe the number of accounts retrieved to 10.The retrieved account information<br>is stored in a variable called accounts. The function then calls the render_template&nbsp;function,<br>in which it takes the name of the template file (&quot;my_account.html&quot;) as its<br>first argument and a list of key-value pairs as its subsequent arguments.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/">https://np656-is601-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Account Transaction Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of an account's transaction history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551346-51c79700-3e58-496e-a7d9-62fc03e064b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transactions history page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the lookup and display occurs</td></tr>
<tr><td> <em>Response:</em> <pre><span style="font-family: Roboto, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;">The main way to fetch<br>the data is to call&nbsp;&nbsp;the query,&nbsp;&nbsp;IS601_TransactionHistory. The query is used to fetch the<br>transaction history for a specific account ID, which is passed as a parameter<br>in the query. The query selects all the columns from the IS601_TransactionHistory table,<br>from that table, it calls the data where the account_id matches the provided<br>account ID, orders the result by the transaction_date column in descending order, and<br>limits the number of results to 10 due to LIMIT 10.</span><br></pre><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/">https://np656-is601-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Deposit/Withdraw </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a Screenshot of the Deposit Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551497-c94f5149-e750-46c2-931a-1003decadb72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deposit page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551579-6d3fd5b2-f516-4717-a38a-3e654e8f1db7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deposit fail<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551346-51c79700-3e58-496e-a7d9-62fc03e064b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deposit success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a Screenshot of the Withdraw Page (this potentially can be the same page with different views)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551808-356c45ee-46a8-4db1-96a1-9ab03c94af7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>withdraw page pt 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551861-64bd841e-c0d3-4665-98d6-f79a416c807f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>withdraw page pt 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show validation error for negative numbers</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236552203-18a6dbb8-0013-4311-aa55-770932744d9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>withdraw fail for trying to take out negative money.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Show validation error for withdrawing more than the account contains</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236552021-7f514cd9-41bf-4297-80b5-e204ce085892.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>withdraw fail for withdrawing more than what account holds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Show a success message for deposit and withdraw (2 screenshots)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236552424-011b7656-2faa-4b7a-87ff-edab7b30a6c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>withdraw success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236551346-51c79700-3e58-496e-a7d9-62fc03e064b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deposit success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Show a screenshot of the transaction pairs in the DB for the above tests</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/236557789-7eb9a1bc-d44c-4f4f-b8db-f5938b19988f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>transaction history, look at the last 6 transactions, they follow the screenshots for<br>withdraw and deposit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain how transactions work</td></tr>
<tr><td> <em>Response:</em> <p>The main steps for transactions are:<div><ol style="border: 0px solid rgb(217, 217, 227); box-sizing:<br>border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y:<br>; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero:<br>; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0<br>0 transparent; --tw-ring-shadow:0 0 transparent; --tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ;<br>--tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia:<br>; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ;<br>--tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; list-style-position: initial; list-style-image: initial; margin:<br>1.25em 0px; padding: 0px 0px 0px 1rem; counter-reset: item 0; display: flex; flex-direction:<br>column;"><li style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0;<br>--tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position:<br>; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ;<br>--tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent;<br>--tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; margin: 0px; padding-left: 0.375em;">Look up the accounts for the source<br>and destination of the transaction.</li><li style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box;<br>--tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ;<br>--tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ;<br>--tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0<br>transparent; --tw-ring-shadow:0 0 transparent; --tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness:<br>; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ;<br>--tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert:<br>; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin: 0px; padding-left: 0.375em;">Create two transaction<br>records, one for the source account with a negative balance change and one<br>for the destination account with a positive balance change.</li><li style="border: 0px solid rgb(217,<br>217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1;<br>--tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ;<br>--tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px;<br>--tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent; --tw-shadow:0 0 transparent; --tw-shadow-colored:0 0<br>transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ;<br>--tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale:<br>; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin: 0px;<br>padding-left: 0.375em;">Calculate the expected total change in the accounts&#39; balances.</li><li style="border: 0px solid<br>rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1;<br>--tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position:<br>; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ;<br>--tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0 transparent; --tw-shadow:0 0 transparent; --tw-shadow-colored:0<br>0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert:<br>; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ;<br>--tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin:<br>0px; padding-left: 0.375em;">Update the balance of the source account by subtracting the expected<br>total change.</li><li style="border: 0px solid rgb(217, 217, 227); box-sizing: border-box; --tw-border-spacing-x:0; --tw-border-spacing-y:0; --tw-translate-x:0;<br>--tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity;<br>--tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing:<br>; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgba(59,130,246,0.5); --tw-ring-offset-shadow:0 0 transparent; --tw-ring-shadow:0 0<br>transparent; --tw-shadow:0 0 transparent; --tw-shadow-colored:0 0 transparent; --tw-blur: ; --tw-brightness: ; --tw-contrast: ;<br>--tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur:<br>; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ;<br>--tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin: 0px; padding-left: 0.375em;">Update the balance of the destination<br>account by adding the expected total change.</li></ol></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/43">https://github.com/neilpatel13/IS601-004/pull/43</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/">https://np656-is601-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Overall this project was much more doable and more managable than MiniPoroject3. The<br>problems I faced in MP3 were much doable in Milestone 2 for how<br>I knew how to deal with the sql issues and html formating issues.<br>The main problems I dealt with Milestone 2 was understanding and figuring out<br>how to do transactions for the banking project. At the end, I was<br>able to get a working function with some issues. The main resources I<br>used to help me figure out the problem was stack overflow, they had<br>some reasources of how to do a banking transaction. But overall this milestone<br>was not too difficult.<div>Stack overflow link to helped me:&nbsp;<a href="https://stackoverflow.com/questions/69676397/how-to-mak-a-transaction-method-in-a-bankaccount-class">https://stackoverflow.com/questions/69676397/how-to-mak-a-transaction-method-in-a-bankaccount-class</a></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://np656-is601-prod.herokuapp.com/login">https://np656-is601-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-milestone-2-bank-project/grade/np656" target="_blank">Grading</a></td></tr></table>