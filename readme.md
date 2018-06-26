<h1>Danbot: A basic Twitterbot</h1>
<h2>Danbot periodically posts very simple statuses to Twitter. Right now they look like this:
	<br>
	<img src= 'screenshot1.jpg'/>
</h2>
<ul>
	<li>
		Download the project folder to your local machine
	</li>
	<li>
		Create a file called credentials.py in the project folder. Include dictionaries for your Twitter account's keys and secrets in the following format: <br>
		<code>
			keys = {
				'CONSUMER_KEY' : 'consumer key goes here',
				'ACCESS_KEY' : 'access key goes here'
			}
			secrets = {
				'CONSUMER_SECRET' : 'consumer secret goes here',
				'ACCESS_SECRET' : 'access secret goes here'
			}
		</code>
	</li>
	<li>
		Set the post interval variable ('INTERVAL') in bot.py
	</li>
	<li>
		Run python bot.py from the command line
	</li>
</ul>

<ul>
	<li>Add more interesting text generators!</li>
</ul>