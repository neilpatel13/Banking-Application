<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Neil Patel (np656)</td></tr>
<tr><td> <em>Generated: </em> 4/24/2023 11:43:52 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/np656" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234155323-cba9568d-dc98-435d-adef-e80cc15c26ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home page when first running server<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234155384-669cf87a-89e1-471f-8498-e41a0fc9ce70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234155467-a0040310-1a95-43fe-a34a-bb60f086815e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company add page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234155529-f46e5feb-1cde-42ec-b3a7-df10db7c8ca4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee search page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234155953-c1825ef5-140d-4dca-9b0d-7fb7c9cf3d16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee add page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234156674-24423fc1-6713-4780-8b79-8782447dc761.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin import page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157028-09b71b06-71a2-4f8b-bd5f-499a5dca1828.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Companies tables<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157086-75e4681a-8320-4a20-86f2-ba3c6bd86b63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157325-10966a33-c898-41c8-ae60-850c1a23b5f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting no file for admin import<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157367-5bfc1e9b-5488-4c15-998b-cd683036c99d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting wrong type of file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157404-b0a66e6d-35c3-46c1-8971-a0217935dde5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting right file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157848-b3bfc2a5-2214-47bd-a968-7e8f9e1f9228.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>table of sucessful upload<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234161593-243082c9-ade1-41d7-b0e0-2c100f1600b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin import code part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234161660-00c47434-6b8d-40c7-bc36-93357d1d7c92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin import code part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234161747-07313fc1-5a4c-414c-92ab-c148bdbf6e33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin import code part 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157325-10966a33-c898-41c8-ae60-850c1a23b5f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting no file for admin import<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157367-5bfc1e9b-5488-4c15-998b-cd683036c99d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting wrong type of file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157404-b0a66e6d-35c3-46c1-8971-a0217935dde5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>submitting right type of file for import<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234158100-400602b4-201e-4543-ad74-bca504cd0bf3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>table of sucessful company upload<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234157848-b3bfc2a5-2214-47bd-a968-7e8f9e1f9228.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>table of sucessful Employee upload<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234161372-d9f86d32-25b9-4c23-8580-41ebb59625a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for add route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160035-8c3104a4-dd33-4f08-9e7c-3efaa9fbd11b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first name flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160116-7cf5b361-4428-4613-b8a9-12911315d5fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last name flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160166-710e4cc1-c1dc-40a2-9076-f11cfeac5739.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160228-5267b044-aa1c-4b40-b5ab-bf9d2a3d5d4c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160255-3ff573bc-484d-4902-8a0d-dc21afbdfd7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>correct email format flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160352-92a60f30-8a36-4eef-88d4-28c4b341ddb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success employee creation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160388-7aa3d4e2-89e7-452c-a42d-a910c55d8fec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>duplicate email flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234160655-4defe6dc-fd14-443d-969f-267a0819f42c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code block<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234162147-39dd04a3-564c-4b6b-9c49-7469d051d703.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>newest employee made is called gif<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234162373-c9b6be00-3ab5-4d84-aea9-8deaf9ca565b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Employees code part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234162400-ca385542-2770-4eab-871e-2879ee97eea7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Employees code part 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234162718-f936128b-502d-4fee-bf17-828bb551dee4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search employee page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163246-db965118-367d-405c-82ec-0e30458f99f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ascending order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234162692-606b167b-0b30-446e-b43a-4521528728ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163649-460da6c1-fabc-43d3-878f-8e25c62ebe72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company filter<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163829-8a08790a-806a-45a9-bc1e-7c1cc909b7f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee code part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163871-85201b78-8c09-4c69-b380-795a7c87697b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee code part 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163975-769a7c16-5928-414a-95fe-6ccc6f33be3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee db before change (Look at number 1, james)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164579-30ed1f5c-2eaf-46e8-b69c-63adfe682f19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee db after change<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164033-a4c4bcec-4f64-4543-995e-39a3729cdbbc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee page before change<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164532-91540d03-a40c-4115-b86d-3e2c8d9ce7cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee page after change<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234163975-769a7c16-5928-414a-95fe-6ccc6f33be3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee db before change (Look at number 1, james)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164579-30ed1f5c-2eaf-46e8-b69c-63adfe682f19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit employee db after change<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164958-f2ad338a-e5d1-41a3-8088-b458b78414d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for add company part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234164987-4aea0ec4-c921-4035-8d90-0d5c0904330d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for add company part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165008-36488809-1460-49ee-87fc-0b653b51ed7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for add company part 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165262-6545b6df-f8fa-456f-b20a-dbd95a6932e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165298-15c43c86-19ec-4878-ae90-0e736f7190c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165330-68e1d722-d019-47bd-9bb5-093273aa75db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165406-390a277a-0ad9-4ba0-bb0b-ef5d1b8a4645.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165447-b6b7f7df-6149-4d8b-9806-7b636307064a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165494-7b7864b5-89e5-43c7-b897-eaed4231aff1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165588-f1e38a21-cb96-49c9-86c0-a6a760c8163e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success creation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234165813-b1b71305-af41-4a3b-9aad-478c7779b107.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company table pre filled in<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234166345-66184811-8809-4312-a461-295c4ab27e9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search code part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234166414-176e9273-5705-435e-873a-428907d0bb83.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search code part 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234166540-fd751186-6652-44c2-aeff-994eff1615ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name filter on<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234166584-0c0c827f-417a-4c48-b8b6-8117316f87b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167073-784a091c-add8-4419-aef1-e188d3996862.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state filter<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167382-75f06e77-fd62-408f-aa63-e5b36a903bd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit company code part 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167412-5bd1e9a8-34ae-47f6-b4fa-bb1cb47e2adc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit company code part 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167442-6faa45d6-533b-4273-9329-1a4bf771967a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit company code part 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167558-8ef8e603-c77a-41f9-9e0b-f1f3872d867e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit company page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167644-524cebd7-9033-431d-8cbf-81762e914963.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>db before update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167672-aa1493db-9087-4164-acff-92430bd2afee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>db after update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167600-70636688-8c96-42a4-9d78-85eefe8590dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167706-ca1b4849-6485-4cda-9c89-43a058a22db3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>page after update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167644-524cebd7-9033-431d-8cbf-81762e914963.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>db before update (look at tests)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167672-aa1493db-9087-4164-acff-92430bd2afee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>db after update<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167887-3812a24b-c8bc-4e2b-ab8b-2bf581d08d36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete route company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234168161-c266326c-4f54-4d74-94b8-c4b72bd0c6e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employee delete route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234168161-c266326c-4f54-4d74-94b8-c4b72bd0c6e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before employee delete <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234168283-960e3310-688f-4c52-9586-9d10e35bc599.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after employee delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167887-3812a24b-c8bc-4e2b-ab8b-2bf581d08d36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete route companies<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234167959-4603eb99-c532-407f-9ee2-a6b7153276a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>companies before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234168006-cd9c1af7-5929-46b6-a5de-bafa33fc76dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>companies after delete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/234169352-6103da7e-eeb0-42ef-9ce3-0a36e3bbcf6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>pytest, many failed due to issues calling the sort filter in the search<br>page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>The most important thing I learned while doing this mini-project was how important<br>it was to define how you want the code to be structured. The<br>biggest problem I was the queries. The reason why is due to not<br>having experience actually coding queries, so I made plently of mistakes when it<br>came to how to call the data correctly. Another issue I faced many<br>times was vs code having visual issues when i thought I had made<br>an error in my code. Overall this project was above average difficulty, but<br>enjoyable.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/np656" target="_blank">Grading</a></td></tr></table>