

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="Holberton School">
    <meta name="google" content="notranslate" />
    
    <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    
    <title>Project: 0x04. Loops, conditions and parsing | Holberton Intranet</title>

    <link rel="stylesheet" media="all" href="/assets/application-d8ceb5678b732ada9ec17acfbb069b39b0fb4fe84eb2386d7682b6df53cce6b6.css" />
    <script src="https://www.gstatic.com/charts/loader.js"></script>
	  <script src="/assets/application-3b7e9c43b3f74f2e55c2fb2e70c2a67111cc4a63918e99386c6c5861382cea42.js"></script>
	  <link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-80dd4e2b2b534776f1430ecc265116b6135be1872b6a06edb53a0fa80e97a308.ico" />
	  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="8uxP+eW4riUsc8CxfdENt5gK11evAUpXIWZTwEFLTz9U0tOS0bPi4/+ZWdNOu6PgoVTVOtFJXfFBliiBVYW7tg==" />

    <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Video player -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/ewwink/clappr-quality-selector-plugin@latest/quality-selector.js"></script>

    <!-- Store user timezone -->
    <script>
      Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
    </script>

    <script src="/packs/js/application-f0e59c44581136cb2218.js"></script>
  </head>

  <body class="
    signed_in 
    env_production
    
    " 
    translate="no" 
    class="notranslate"
    data-theme-suffix=""
    data-checker-special-theme="">

      <input type="hidden" id="hbtn-slack-url" value="https://holberton-students.slack.com" />
      <nav id="nav-left" class="hidden-xs title-font">
        <a href="/">
          <div id="hbtn-logo" class="">
            <div class="logo"></div>
              <a class="onair_container" data-toggle="modal" data-target="#video_streams_current_modal" title="Video Streaming in progress...">
                <div class="onair_item">
                  <i class="fa fa-television" aria-hidden="true"></i>
                  <i class="fa fa-podcast animate-flicker" aria-hidden="true"></i>
                </div>
              </a>
          </div>
</a>        <ul>
           
  <li>
    <a target="_blank" href="https://holberton-students.slack.com">
        <div class="icon">
          <i class="fa fa-slack"></i>
        </div>
      Slack
</a>  </li>

    <hr />
  
    <!-- STUDENT -->
    <li>
      <a href="/dashboards/my_planning">
          <div class="icon">
            <i class="fa fa-calendar"></i>
          </div>
        Planning
</a>    </li>
    <li>
      <a href="/dashboards/my_current_projects">
          <div class="icon">
            <i class="fa fa-code-fork"></i>
          </div>
        Projects
</a>    </li>
      <li>
        <a href="/dashboards/my_professional_track">
            <div class="icon">
              <i class="fa fa-thumbs-o-up"></i>
            </div>
          Professional track
</a>      </li>
    <li>
      <a href="/dashboards/corrections_i_can_make">
          <div class="icon">
            <i class="fa fa-check"></i>
          </div>
        QA Reviews
</a>    </li>
      <li>
        <a href="/dashboards/my_current_reefineries">
            <div class="icon">
              <i class="fa fa-comments"></i>
            </div>
          Mock interviews
</a>      </li>

      <li>
        <a href="/dashboards/my_current_evaluation_quizzes">
            <div class="icon">
              <i class="fa fa-question"></i>
            </div>
          Evaluation quizzes
</a>      </li>
    

    <hr />

    <h4>My resources</h4>

      <li>
        <a href="/dashboards/my_curriculums">
            <div class="icon">
              <i class="fa fa-graduation-cap"></i>
            </div>
          Curriculums
</a>      </li>

    <li>
      <a href="/dashboards/my_concepts">
          <div class="icon">
            <i class="fa fa-file-text"></i>
          </div>
        Concepts
</a>    </li>
    

      <li>
        <a href="/dashboards/video_rooms">
            <div class="icon">
              <i class="fa fa-video-camera"></i>
            </div>
          Conference rooms
</a>      </li>

      <li>
        <a href="/dashboards/my_server">
            <div class="icon">
              <i class="fa fa-server"></i>
            </div>
          Servers
</a>      </li>

      <li>
        <a href="/dashboards/my_containers">
            <div class="icon">
              <i class="fa fa-cloud"></i>
            </div>
          Containers
</a>      </li>
    

      <li>
        <a target="_blank" href="https://students-support.hbtn.io/hc">
            <div class="icon">
              <i class="fa fa-graduation-cap"></i>
            </div>
          School information
</a>      </li>

    <hr />

    <h4>My campus</h4>

    <li>
      <a href="/dashboards/my_peers">
          <div class="icon">
            <i class="fa fa-users"></i>
          </div>
        Peers
</a>    </li>
    <li>
      <a href="/dashboards/my_captain_log">
          <div class="icon">
            <i class="fa fa-book"></i>
          </div>
        Captain's Logs
</a>    </li>

      <li>
        <a href="/dashboards/my_officers">
            <div class="icon" style="padding-left: 2px;">
              <i class="fa fa-building"></i>
            </div>
          Officers
</a>      </li>

      <li>
        <a href="/dashboards/my_speakers_of_the_day">
            <div class="icon">
              <i class="fa fa-microphone"></i>
            </div>
          Speakers of the Day
</a>      </li>

<hr />
<li>
  <a href="/users/my_profile">
      <div class="icon">
        <i class="fa fa-user"></i>
      </div>
    My Profile
</a></li>

        </ul>
      </nav>

    <main>

        <nav class="navbar navbar-default navbar-main visible-xs">
          <div class="container">
            <div class="navbar-header mobile-nav-bar ">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="/">
                <div id="hbtn-logo">
                  <div class="logo"></div>
                </div>
</a>                <div class="onair_container" data-toggle="modal" data-target="#video_streams_current_modal"  title="Video Streaming in progress...">
                  <div class="onair_item">
                    <i class="fa fa-television" aria-hidden="true"></i>
                    <i class="fa fa-podcast animate-flicker" aria-hidden="true"></i>
                  </div>
                </div>
            </div>
          </div>
          <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
               
  <li>
    <a target="_blank" href="https://holberton-students.slack.com">
      Slack
</a>  </li>

    <hr />
  
    <!-- STUDENT -->
    <li>
      <a href="/dashboards/my_planning">
        Planning
</a>    </li>
    <li>
      <a href="/dashboards/my_current_projects">
        Projects
</a>    </li>
      <li>
        <a href="/dashboards/my_professional_track">
          Professional track
</a>      </li>
    <li>
      <a href="/dashboards/corrections_i_can_make">
        QA Reviews
</a>    </li>
      <li>
        <a href="/dashboards/my_current_reefineries">
          Mock interviews
</a>      </li>

      <li>
        <a href="/dashboards/my_current_evaluation_quizzes">
          Evaluation quizzes
</a>      </li>
    

    <hr />

    <h4>My resources</h4>

      <li>
        <a href="/dashboards/my_curriculums">
          Curriculums
</a>      </li>

    <li>
      <a href="/dashboards/my_concepts">
        Concepts
</a>    </li>
    

      <li>
        <a href="/dashboards/video_rooms">
          Conference rooms
</a>      </li>

      <li>
        <a href="/dashboards/my_server">
          Servers
</a>      </li>

      <li>
        <a href="/dashboards/my_containers">
          Containers
</a>      </li>
    

      <li>
        <a target="_blank" href="https://students-support.hbtn.io/hc">
          School information
</a>      </li>

    <hr />

    <h4>My campus</h4>

    <li>
      <a href="/dashboards/my_peers">
        Peers
</a>    </li>
    <li>
      <a href="/dashboards/my_captain_log">
        Captain's Logs
</a>    </li>

      <li>
        <a href="/dashboards/my_officers">
          Officers
</a>      </li>

      <li>
        <a href="/dashboards/my_speakers_of_the_day">
          Speakers of the Day
</a>      </li>

<hr />
<li>
  <a href="/users/my_profile">
    My Profile
</a></li>

              <hr />
              <li><a rel="nofollow" data-method="delete" href="/auth/sign_out">Log out (Jorge Ramirez)</a></li>
            </ul>
          </div>
        </nav>

      <div id="layout-bars">
        

        

        

        
      </div>
      

      <article class="">
        

  <div id="jigsaw-shortcut-lists">



</div>

<h1 class="gap">0x04. Loops, conditions and parsing</h1>


<div id="project_id" style="display: none" data-project-id="251"></div>

<p class="sm-gap">
  <small>
    <i class="fa fa-folder-open"></i>
    Foundations - System engineering &amp; DevOps ― Bash
      &nbsp;
      <a id="block-modal-link" data-toggle="modal" data-target="#block-modal" href="#"><i class="fa fa-question-circle"></i></a>
  </small>
</p>

  <p>
    <em>
      <small>
        <i class="fa fa-user"></i> by Sylvain Kalache, co-founder at Holberton School
      </small>
    </em>
  </p>




  <p>
    <small>
      <i class="fa fa-calendar"></i>
          Ongoing project - started 10-22-2020, must end by 10-23-2020 (in about 9 hours)
        - you're done with <span id="student_task_done_percentage">0</span>% of tasks.
    </small>
  </p>

    <p>
      <small>
        <i class="fa fa-check"></i>
          Checker will be released at 10-22-2020 03:36 PM
      </small>
    </p>


    <p>
      <small>
        <i class="fa fa-check-square"></i>
        QA review fully automated.
      </small>
    </p>










    <div class="gap formatted-content">
      <p style="margin-bottom: 0"><em>For this project, students are expected to look at this concept:</em></p>
      <ul style="margin-top: 5px">
          <li>
            <em><a href="/concepts/9">Shell</a></em>
          </li>
      </ul>
    </div>

  <article id="description" class="gap formatted-content">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/BC2neyc5GcI" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201022%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201022T201519Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=fb9662fcbd6463914c468844e21ebc8ef8c2c77c22a5249b6d7fccf662bc05c7" alt="" style="" /></a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/XnVjFM8a1W4RfRu4TCPY-g" title="The <code>for</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>for</code> loop</a> </li>
<li><a href="/rltoken/TKpmMkXbW4dgKxdKt51fZA" title="The <code>while</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>while</code> loop</a> </li>
<li><a href="/rltoken/6MzdEyyTpW9R1k0hbKFUbQ" title="The <code>until</code> loop&quot; target=&ldquo;_blank&rdquo;>The <code>until</code> loop</a> </li>
<li><a href="/rltoken/zOH3mQvvHyO_ITinhKSV6Q" title="Loops sample" target="_blank">Loops sample</a> </li>
<li><a href="/rltoken/IM0Gv6VPzwAmqzlJxETZkw" title="Variable assignment and arithmetic" target="_blank">Variable assignment and arithmetic</a> </li>
<li><a href="/rltoken/K3E6xI9-goDM-93vsjCpPA" title="Comparison operators" target="_blank">Comparison operators</a> </li>
<li><a href="/rltoken/0OZLLDT28KrRZdid-l6hwg" title="File test operators" target="_blank">File test operators</a> </li>
<li><a href="/rltoken/Dyrnap2UC-LrzrmCOJRx8A" title="Make your scripts portable" target="_blank">Make your scripts portable</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>env</code></li>
<li><code>cut</code></li>
<li><code>for</code></li>
<li><code>while</code></li>
<li><code>until</code></li>
<li><code>if</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/gshUY8R5dEKQKBBvTTGAbQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>More Info</h2>

<h3>Shellcheck</h3>

<p><a href="/rltoken/E7Pr2zeM3cdY5-C0HKwtbw" title="Shellcheck" target="_blank">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. <code>Shellcheck</code> is your friend! <strong>All your Bash scripts must pass <code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>

<p><code>Shellcheck</code> is available on the school&rsquo;s computers. If you want to use it on your own computer, here is how to <a href="/rltoken/SOX0HZTMgzHbcxrvU1X4hw" title="install it" target="_blank">install it</a>.</p>

<p>Examples:</p>

<p>Not passing <code>Shellcheck</code>:<br />
<br />
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png" alt="" style="" /></p>

<p>Passing <code>Shellcheck</code>:<br />
<br />
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png" alt="" style="" /></p>

<p>For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code <code>SC2034</code>, you can browse <a href="/rltoken/1SeRQAUtYIpfXXIQeD1PFQ" title="https://github.com/koalaman/shellcheck/wiki/SC2034" target="_blank">https://github.com/koalaman/shellcheck/wiki/SC2034</a>.</p>

  </article>




    <!-- Servers -->

    <!-- Tasks -->
      <hr class="gap">
      <h2 class="gap">Tasks</h2>
      <section class="formatted-content">
            <div data-role="task1223" data-position="1">
              <div class=" clearfix gap" id="task-1223">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1223">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1223" data-project-id="251" data-toggle="modal" data-target="#task-1223-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1223-users-done-modal" data-task-id="1223" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "0. Create a SSH RSA key pair"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    0. Create a SSH RSA key pair
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Read for this task:</p>

<ul>
<li><a href="/rltoken/_11FMUABmTFrUaQvTr8rbw" title="Linux and Mac OS users" target="_blank">Linux and Mac OS users</a></li>
<li><a href="/rltoken/_JMRDGehQWRXzce3EVRdWA" title="Windows users" target="_blank">Windows users</a></li>
</ul>

<p>man: <code>ssh-keygen</code></p>

<p>You will soon have to manage your own <strong>servers</strong> concept page hosted on remote <a href="/rltoken/e4-Q5Ebz_iidUZAkvrPyEA" title="data centers" target="_blank">data centers</a>. We need to set them up with your RSA public key so that you can access them via SSH.</p>

<p>Create a RSA key pair.</p>

<p>Requirements:</p>

<ul>
<li>Share your <strong>public key</strong> in your answer file <code>0-RSA_public_key.pub</code></li>
<li>Fill the <code>SSH public key</code> field of your <a href="/rltoken/Oxtupmk95xGx7_FFQ3WTbA" title="intranet profile" target="_blank">intranet profile</a> with the public key you just generated</li>
<li><strong>Keep the private key to yourself in a secure location</strong>, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects</li>
<li>If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase</li>
</ul>

<p>SSH and RSA keys will be covered in depth in a later project.</p>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>0-RSA_public_key.pub</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1224" data-position="2">
              <div class=" clearfix gap" id="task-1224">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1224">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1224" data-project-id="251" data-toggle="modal" data-target="#task-1224-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1224-users-done-modal" data-task-id="1224" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "1. For Holberton School loop"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    1. For Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirement:</p>

<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
</ul>

<pre><code>sylvain@ubuntu$ head -n 2 1-for_holberton_school 
#!/usr/bin/env bash
# This script is displaying &quot;Holberton School&quot; 10 times
sylvain@ubuntu$ ./1-for_holberton_school 
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$ 
</code></pre>

<p>Note that: </p>

<ul>
<li>The first line of my Bash script starts with <code>#!/usr/bin/env bash</code></li>
<li>The second line of my Bash scripts is a comment explaining what it is doing</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>1-for_holberton_school</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1225" data-position="3">
              <div class=" clearfix gap" id="task-1225">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1225">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1225" data-project-id="251" data-toggle="modal" data-target="#task-1225-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1225-users-done-modal" data-task-id="1225" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "2. While Holberton School loop"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    2. While Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>

<pre><code>sylvain@ubuntu$ ./2-while_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>2-while_holberton_school</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1226" data-position="4">
              <div class=" clearfix gap" id="task-1226">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1226">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1226" data-project-id="251" data-toggle="modal" data-target="#task-1226-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1226-users-done-modal" data-task-id="1226" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "3. Until Holberton School loop"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    3. Until Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>until</code> loop (<code>for</code> and <code>while</code> are forbidden)</li>
</ul>

<pre><code>sylvain@ubuntu$ ./3-until_holberton_school
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>3-until_holberton_school</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1227" data-position="5">
              <div class=" clearfix gap" id="task-1227">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1227">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1227" data-project-id="251" data-toggle="modal" data-target="#task-1227-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1227-users-done-modal" data-task-id="1227" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "4. If 9, say Hi!"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    4. If 9, say Hi!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays <code>Holberton School</code> 10 times, but for the 9th iteration, displays <code>Holberton School</code> <em>and then</em> <code>Hi</code> on a new line.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code> statement</li>
</ul>

<pre><code>sylvain@ubuntu$ ./4-if_9_say_hi
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Holberton School
Hi
Holberton School
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>4-if_9_say_hi</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1228" data-position="6">
              <div class=" clearfix gap" id="task-1228">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1228">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1228" data-project-id="251" data-toggle="modal" data-target="#task-1228-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1228-users-done-modal" data-task-id="1228" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "5. 4 bad luck, 8 is your chance"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    5. 4 bad luck, 8 is your chance
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that loops from 1 to 10 and:</p>

<ul>
<li>displays <code>bad luck</code> for the 4th loop iteration</li>
<li>displays <code>good luck</code> for the 8th loop iteration</li>
<li>displays <code>Holberton School</code> for the other iterations</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code>, <code>elif</code> and <code>else</code> statements</li>
</ul>

<pre><code>sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Holberton School
Holberton School
Holberton School
bad luck
Holberton School
Holberton School
Holberton School
good luck
Holberton School
Holberton School
sylvain@ubuntu$ 
</code></pre>

<p>For the most curious:</p>

<ul>
<li><a href="/rltoken/ZhodlAA_cpEBHGtyQkDtqA" title="8 in the Chinese culture" target="_blank">8 in the Chinese culture</a></li>
<li><a href="/rltoken/yVebRHCOdVy08j5Fylv5lQ" title="4 in the Chinese culture" target="_blank">4 in the Chinese culture</a></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>5-4_bad_luck_8_is_your_chance</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1229" data-position="7">
              <div class=" clearfix gap" id="task-1229">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1229">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1229" data-project-id="251" data-toggle="modal" data-target="#task-1229-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1229-users-done-modal" data-task-id="1229" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "6. Superstitious numbers"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    6. Superstitious numbers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays numbers from 1 to 20 and:</p>

<ul>
<li>displays <code>4</code> <em>and then</em> <code>bad luck from China</code> for the 4th loop iteration</li>
<li>displays <code>9</code> <em>and then</em> <code>bad luck from Japan</code> for the 9th loop iteration</li>
<li>displays <code>17</code> <em>and then</em> <code>bad luck from Italy</code> for the 17th loop iteration</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>case</code> statement</li>
</ul>

<pre><code>sylvain@ubuntu$ ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>6-superstitious_numbers</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1230" data-position="8">
              <div class=" clearfix gap" id="task-1230">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1230">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1230" data-project-id="251" data-toggle="modal" data-target="#task-1230-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1230-users-done-modal" data-task-id="1230" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "7. Clock"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    7. Clock
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p>

<ul>
<li>display hours from 0 to 12</li>
<li>display minutes from 1 to 59</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>

<p>Note that in this example, we only display the first 70 lines using the <code>head</code> command.</p>

<pre><code>sylvain@ubuntu$ ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>7-clock</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1231" data-position="9">
              <div class=" clearfix gap" id="task-1231">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1231">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1231" data-project-id="251" data-toggle="modal" data-target="#task-1231-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1231-users-done-modal" data-task-id="1231" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "8. For ls"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    8. For ls
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays:</p>

<ul>
<li>The content of the current directory</li>
<li>In a list format</li>
<li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
<li>Do not display hidden files</li>
</ul>

<pre><code>sylvain@ubuntu$ ls
100-read_and_cut              1-for_holberton_school         6-superstitious_numbers
101-tell_the_story_of_passwd  2-while_holberton_school       7-clock
102-lets_parse_apache_logs    3-until_holberton_school       8-for_ls
103-dig_the-data              4-if_9_say_hi                  9-to_file_or_not_to_file
10-fizzbuzz                   5-4_bad_luck_8_is_your_chance
sylvain@ubuntu$  ./8-for_ls
read_and_cut
tell_the_story_of_passwd
lets_parse_apache_logs
dig_the-data
fizzbuzz
for_holberton_school
while_holberton_school
until_holberton_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>8-for_ls</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1266" data-position="10">
              <div class=" clearfix gap" id="task-1266">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1266">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1266" data-project-id="251" data-toggle="modal" data-target="#task-1266-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1266-users-done-modal" data-task-id="1266" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "9. To file, or not to file"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    9. To file, or not to file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that gives you information about the <code>holbertonschool</code> file.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>if</code> and, <code>else</code> (<code>case</code> is forbidden)</li>
<li>Your Bash script should check if the file exists and print:

<ul>
<li>if the file exists: <code>holbertonschool file exists</code></li>
<li>if the file does not exist: <code>holbertonschool file does not exist</code></li>
</ul></li>
<li>If the file exists, print:

<ul>
<li>if the file is empty: <code>holbertonschool file is empty</code></li>
<li>if the file is not empty: <code>holbertonschool file is not empty</code></li>
<li>if the file is a regular file: <code>holbertonschool is a regular file</code></li>
<li>if the file is not a regular file: (nothing)</li>
</ul></li>
</ul>

<pre><code>sylvain@ubuntu$ file holbertonschool
holbertonschool: cannot open `holbertonschool&#39; (No such file or directory)
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file does not exist
sylvain@ubuntu$ touch holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is empty
holbertonschool is a regular file
sylvain@ubuntu$ echo &#39;betty&#39; &gt; holbertonschool 
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
holbertonschool is a regular file
sylvain@ubuntu$ rm holbertonschool 
sylvain@ubuntu$ mkdir holbertonschool
sylvain@ubuntu$ ./9-to_file_or_not_to_file 
holbertonschool file exists
holbertonschool file is not empty
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>9-to_file_or_not_to_file</code></li>
    </ul>





</div>
 
            </div>
            <div data-role="task1279" data-position="11">
              <div class=" clearfix gap" id="task-1279">
<span id="user_id" data-id="1662"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1279">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1279" data-project-id="251" data-toggle="modal" data-target="#task-1279-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1279-users-done-modal" data-task-id="1279" data-project-id="251">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Students who are done with "10. FizzBuzz"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner" >
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


    </div>

  <h4 class="task">
    10. FizzBuzz
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a Bash script that displays numbers from 1 to 100.</p>

<p>Requirements:</p>

<ul>
<li>Displays <code>FizzBuzz</code> when the number is a multiple of 3 and 5</li>
<li>Displays <code>Fizz</code> when the number is multiple of 3</li>
<li>Displays <code>Buzz</code> when the number is a multiple of 5</li>
<li>Otherwise, displays the number</li>
<li>In a list format</li>
</ul>

<pre><code>sylvain@ubuntu$ ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
sylvain@ubuntu$ 
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x04-loops_conditions_and_parsing</code></li>
        <li>File: <code>10-fizzbuzz</code></li>
    </ul>





</div>
 
            </div>
      </section>


      <p class="lg-gap formatted-content">
          <a class="btn btn-primary btn-block" data-confirm="Are you sure? You still have mandatory tasks to do on the projects &quot;0x04. Loops, conditions and parsing&quot;, &quot;0x04. A tweet a day keeps the @julienbarbier42 away&quot;, &quot;0x00. Share your knowledge &quot;, you really should focus on those first." href="/projects/251/unlock_optionals">Done with the mandatory tasks? Unlock 4 advanced tasks now!</a>
      </p>




  <div class="modal fade" id="block-modal">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title">About the "Bash" block</h4>
      </div>
      <div class="modal-body">
        <p>Unless stated, all your projects will be auto-corrected with Ubuntu 14.04 LTS.</p>

      </div>
    </div><!-- /.modal-content -->
  </div><!-- /.modal-dialog -->
</div><!-- /.modal -->






      </article>
      
      <div class="copyright">Copyright &copy; 2020 Holberton School. All rights reserved.</div>
    </main>

      <div id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
    <i class="fa fa-search" aria-hidden="true"></i>
    <i class="fa fa-window-minimize" aria-hidden="true"></i>
</div>
      <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar" 
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨"
    />
</div>
            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>
            </div>
        </div>
    </div>
</div>
        <div class="modal fade" id="video_streams_current_modal">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Video streaming</h4>
            </div>
            <div class="modal-body">
                <ul class="streams list-group"></ul>
                <div class="player">
                    <div class="header">
                        <div class="back"><i class="fa fa-chevron-left" aria-hidden="true"></i></div>
                        <div class="title"></div>
                    </div>
                    <div id="video_streams_current_modal_player"></div>
                </div>
                <div class="spinner" >
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div class="error"></div>
            </div>
        </div>
    </div>
</div>



      <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>

    
      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create', 
            'UA-67152800-6', 
            'auto', {
              userId: '1662'
            }
          );

        ga('send', 'pageview');

        $(document).ready(function() { 
          ga(function(tracker) { 
            var clientId = tracker.get('clientId'); 
            $('.ga-client-id').val(clientId); 
          }); 
        });
      </script>



      <input id="checker_pride_assets" type="hidden" value="[]" />
  </body>
</html>
