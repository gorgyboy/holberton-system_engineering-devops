<article class="">

<div id="jigsaw-shortcut-lists">

</div>

<h1 class="gap">0x06. Regular expression</h1>

<div id="project_id" style="display: none" data-project-id="78"></div>

<p class="sm-gap">
<small>
<i class="fa fa-folder-open"></i>
Foundations - System engineering &amp; DevOps ― Scripting
</small>
</p>

<p>
<em>
<small>
<i class="fa fa-user"></i> by Sylvain Kalache, co-founder at Holberton School
</small>
</em>
</p>

<article id="description" class="gap formatted-content">
<h2>Background Context</h2>

<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>

<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>

<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.slideshare.net/neha_jain/introducing-regular-expressions" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a> </li>
<li><a href="https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a> </li>
<li><a href="https://rubular.com/" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a> </li>
<li><a href="https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a> </li>
<li><a href="https://regexone.com/" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a> </li>
</ul>

</article>
