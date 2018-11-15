# dad-joke-bot

## tl;dr

A Dad Jokes Bot, available on Twitter - check it out [here](https://twitter.com/tata_jokes) and on Telegram.

## Description

Twitter / Telegram Dad joke bot which uses the [icanhazdadjoke.com](https://icanhazdadjoke.com/api) API.

Built with:

- Python
- Serverless
- AWS Lambda

## Set-up

### AWS

Set-up an AWS account and a profile with appropriate Lambda IAM permissions.

Add the profile id and access key in `~/.aws/credentials` with the same name as `profile` in the `serverless.yml` config file.

Or source the id and key directly like this in your terminal:

```bash
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

### Twitter / Telegram credentials

Follow instructions with Twitter and Telegram to get set-up and then convert the template file `serverless.env.yml` to `serverless.env.yml` and add the credentials.

### Serverless

```bash
# Install the Serverless Framework
$ npm install serverless -g

# Install the necessary plugins
$ npm install
```

Check [Serverless](https://serverless.com) documentation for more info.

### Serverless Set-up

With the above in place, you should be ready to deploy.

```bash
# Deploy
serverless deploy -v

# Using the service endpoint (API Gateway urls) returned in the output, configure the Webhook for the Telegram bot
$ curl -X POST https://<your_url>.amazonaws.com/production/set_webhook

# To invoke a Lambda function e.g. the Twitter bot function
serverless invoke -f post_to_twitter -l
```

## Local set-up

For future development, here's how to get set-up locally:

```bash
# create virtual env
python3 -m venv env

# activate the virtual env
source env/bin/activate

# install dependencies
pip install -r requirements-dev.txt
```

## Code Style

Python code is styled per flake8 and formatted using [yapf](https://github.com/google/yapf).
