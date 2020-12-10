<h1 class="gap">0x0C. Web server</h1>


<div id="project_id" style="display: none" data-project-id="266"></div>

<p class="sm-gap">
<small>
<i class="fa fa-folder-open"></i>
Foundations - System engineering &amp; DevOps ― Web stack
</small>
</p>

<p>
<em>
<small>
<i class="fa fa-user"></i> by Sylvain Kalache, co-founder at Holberton School
</small>
</em>
</p>

<div class="gap formatted-content">
<p style="margin-bottom: 0"><em>For this project, students are expected to look at these concepts:</em></p>
<ul style="margin-top: 5px">
<li>
<em><a href="/concepts/12">DNS</a></em>
</li>
<li>
<em><a href="/concepts/17">Web Server</a></em>
</li>
<li>
<em><a href="/concepts/43">CI/CD</a></em>
</li>
<li>
<em><a href="/concepts/65">Docker</a></em>
</li>
<li>
<em><a href="/concepts/68">Web stack debugging</a></em>
</li>
<li>
<em><a href="/concepts/110">What is a Child Process?</a></em>
</li>
<li>
<em><a href="/concepts/124">DevOps</a></em>
</li>
<li>
<em><a href="/concepts/125">System Administration</a></em>
</li>
<li>
<em><a href="/concepts/126">Site Reliability Engineering</a></em>
</li>
</ul>
</div>

<article id="description" class="gap formatted-content">
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" alt="" style="" /></p>

<h2>Background Context</h2>

<p><a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" alt="" style="" /></a></p>

<p>In this project, some of the tasks will be graded on 2 aspects:</p>

<ol>
<li>Is your <code>web-01</code> server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>

<p>For example, if I need to create a file <code>/tmp/test</code> containing the string <code>hello world</code> and modify the configuration of Nginx to listen on port <code>8080</code> instead of <code>80</code>, I can use <code>emacs</code> on my server to create the file and to modify the Nginx configuration file <code>/etc/nginx/sites-enabled/default</code>.</p>

<p>But my answer file would contain:</p>

<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i &#39;s/80/8080/g&#39; /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>

<p>As you can tell, I am not using <code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an <a href="/rltoken/Hjv9yJQtW6X7VRa2ByMeEg" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the <code>root</code> user, you do not need to use the <code>sudo</code> command.</p>

<p>A good Software Engineer is a <a href="/rltoken/y1MX-uAX-0a4bgXfH3uweQ" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" style="" /></p>

<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment: </p>

<ul>
<li>start an <code>ubuntu:16.04</code> Docker container</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>

<p>Check out the Docker concept page for more info about how to manipulate containers.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/4tRRzyyETAySzU-bgNGLSw" title="How the web works" target="_blank">How the web works</a> </li>
<li><a href="/rltoken/H9OfhUnBDdxV-QQnIucMlA" title="Nginx" target="_blank">Nginx</a> </li>
<li><a href="/rltoken/wePwmjbJDgJZO7YPvffWxQ" title="How to Configure Nginx" target="_blank">How to Configure Nginx</a></li>
<li><strong>Child process</strong> concept page</li>
<li><a href="/rltoken/qkpso3mgcpv3tPUhBrZBOA" title="Root and sub domain" target="_blank">Root and sub domain</a> </li>
<li><a href="/rltoken/C9s3U62JbiOAvn9WCoxKsA" title="HTTP requests" target="_blank">HTTP requests</a> </li>
<li><a href="/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw" title="HTTP redirection" target="_blank">HTTP redirection</a> </li>
<li><a href="/rltoken/5UvC588x2hZR7dm6eRFPoQ" title="Not found HTTP response code" target="_blank">Not found HTTP response code</a> </li>
<li><a href="/rltoken/bkqQ72HZVAV65G8nB503Pw" title="Logs files on Linux" target="_blank">Logs files on Linux</a> </li>
</ul>

<p><strong>For reference:</strong></p>

<ul>
<li><a href="/rltoken/gdZet6dJ30MzaeoucXCfRA" title="RFC 7231 (HTTP/1.1)" target="_blank">RFC 7231 (HTTP/1.1)</a></li>
<li><a href="/rltoken/EWo6KcJSfShUKLPqzeiXqQ" title="RFC 7540 (HTTP/2)" target="_blank">RFC 7540 (HTTP/2)</a></li>
</ul>

<p><strong>man or help</strong>: </p>

<ul>
<li><code>scp</code></li>
<li><code>curl</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lGyY_30FRBmgKhisGmKd1A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web servers usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>

<h3>DNS</h3>

<ul>
<li>What DNS stands for</li>
<li>What is DNS main role</li>
</ul>

<h3>DNS Record Types</h3>

<ul>
<li><code>A</code></li>
<li><code>CNAME</code></li>
<li><code>TXT</code></li>
<li><code>MX</code></li>
</ul>