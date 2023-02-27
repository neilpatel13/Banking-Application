<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Neil Patel (np656)</td></tr>
<tr><td> <em>Generated: </em> 2/21/2023 1:16:59 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/np656" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220254430-b101bb30-a984-47a1-a44b-0abf85fd9079.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of the edited add function &quot;&quot;&quot;UCID: np656 (2/19) the solution for this<br>task was adding the name, description, and due date    <br>as in a dict key value pair using task[key] = value&quot;&quot;&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220254784-f4ea1b92-d897-437a-8329-83d9c16086b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>adding task success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220254866-342354e8-8e15-45ff-a165-6fb08d529018.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>adding task failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style=""> the solution for this task was adding the name,<br>description, and due date as in a dict key value pair using task[key]<br>= value. I set each variable equal to the passed by value in<br>the function due to add task asking for input, and that input had<br>a section for name, description, and due date. Once all conditions were good,<br>the task was then appended to the tasks list.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220255701-f6b93674-e289-4bf4-a2e0-2a1c537f84b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>process update editied code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was first checking the index<br>of the tasks to make sure user is selecting the right one the<br>checking if index was greater than equal than the len of tasks or<br>less than 0 was checking for the out of bounds issue, after it<br>was just processing the name, desc, and due by changing TODO to the<br>task with index of that variable.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220256173-9cdf851a-19ab-4119-a325-abf84c5293c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update task code edited <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220256358-4a234ca8-fd14-4386-be93-5cb31a0b532c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220256443-2fe4791a-3523-4fb1-b334-f98dfd1c1e25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was first checking the index<br>of the tasks to make sure user is selecting the right one, after<br>it was just checking the task in the specified index was there using<br>the if else task[paramater]&nbsp; then it was just updating the name, desc, and<br>due by setting the new input to the same fields of the task.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220256946-ad5a210e-ca8e-4f11-85ad-701641ecfd37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>mark done code edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257075-8b390165-3bef-4873-8e0a-48f70ba53521.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>mark done sucess<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257179-bf7c15c3-544c-4016-ae17-2b1df066f2e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>mark done failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was first checking the index<br>of the tasks to make sure user isselecting the right one, after it<br>checking if the task was either not done or already done, for not<br>done, I used the datetime.now in the done index of task to mark<br>it done, it made it set true, and for already done, just printing<br>a message saying its done already. then last step was calling the save<br>function</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257737-d3123845-edde-4c36-84dd-108e51ef052f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view task code edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257803-7b3a9af3-63a9-49ca-9f9c-d0645e9cf09e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view task success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257897-b309927f-e78e-44a3-8b89-9794f906dc10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view task failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220257946-fe5d0ff9-936a-4b6c-9d62-f9d46024ebeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list task for multiple<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220258308-b7e6aac8-a403-4d1a-9d0a-948a8a6290ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting function code edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220258487-4584849b-292a-4acd-ad2e-f4bc776d450c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220258546-e0b3c4bb-616b-4e90-89a6-2ceb982aaedc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was first checking the index<br>of the tasks to make sure user isselecting the right one, after it<br>was just using the del function to delete the task at the specified<br>index and printing a message or completed deletion. If there was a out<br>of bound error, I made sure to print a message saying that there<br>was no task at that index.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220258875-5e2e5727-f611-45f4-a1c9-4b979069b80d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>incomplete task code edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220259077-7badaf65-6da7-43a4-bf63-84df5237a77b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>incomplete success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220258969-9f5be6be-a258-4b08-95e5-fa925101185e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>incomplete failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was by appending all the<br>task not in done to a seperate list and printing the list out.<br>If there was no incomplete task, I would just print a message saying<br>there was no incomplete tasks.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220259525-12595ce3-5f43-4af8-bc91-6961f295e515.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>overdue task code editied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220259729-f8192631-c757-4ec3-9396-4976dbcbffcd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>overdue complete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220259806-2a7800a0-52cc-412d-89a7-f71ce9b2adee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>overdue fail<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task was first comparing all task<br>that were less than over_due variable and seeing if it was not in<br>done, and then appending it to a seperate list and printing it out.<br>I appended the over due task into _tasks and then ran list_tasks(_tasks).</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220260238-ef46b220-0145-40dd-8ba9-9ba14eaa154c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>remaining time code edited<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220260335-bf3ebc81-492b-401e-8631-c8fba59cd953.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>remaining time success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220260395-d5b94d3f-ee5e-4f29-9622-299d867741a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>remaining time failed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div style="line-height: 19px;"><div style="">the solution for this task using the datetime.strptime to get<br>the due date and subtract it from datetime.now to get the time remaining,<br>and then in the printing function, printing out each value of datetime.&nbsp;&nbsp;now =<br>datetime.now() ,due_date = datetime.strptime(task['due'], "%Y-%m-%d %H:%M:%S"),time_remain = due_date - now helped solved for<br>the remaining time left in the tasks.</div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220261505-af34ede5-2ba1-42b1-abe3-b3bcc1e4bd01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>general output #1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220261575-4f7573b0-741d-4bf4-afe8-ce42eed2e63f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>general output #2 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/90282158/220260942-b7d04013-1190-437c-b94c-67fdd493d820.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>saved JSON file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>The main issued I dealt with in this project was understand how the<br>datetime class and str to datetime function worked. That was the difficult part<br>due not understanding how the input for the due date was suppose to<br>be and how how to compare it with other times for the imcomplete<br>and overdue functions. Another issue I was having for when I needed to<br>make a another list and call the list task function to it, I<br>was having difficulty trying to correctly make the if else statement to append<br>it to the new list, luckily after a few tries and help from<br>the professor I was able to get it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/neilpatel13/IS601-004/pull/8">https://github.com/neilpatel13/IS601-004/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-1-tracker-app/grade/np656" target="_blank">Grading</a></td></tr></table>