<!--
title: 'AWS Simple HTTP Endpoint example in Python'
description: 'This template demonstrates how to make a simple REST API with Python running on AWS Lambda and API Gateway using the traditional Serverless Framework.'
layout: Doc
framework: v2
platform: AWS
language: python
priority: 2
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

This template demonstrates how to make a simple REST API with Python running on AWS Lambda and API Gateway using the traditional Serverless Framework.

# Serverless Framework Python REST API on AWS

This template demonstrates how to make a simple REST API with Python running on AWS Lambda and API Gateway using the traditional Serverless Framework.

This template does not include any kind of persistence (database). For a more advanced examples check out the [examples repo](https://github.com/serverless/examples/) which includes DynamoDB, Mongo, Fauna and other examples.

## Usage

### Deployment

This example is made to work with the Serverless Framework dashboard which includes advanced features like CI/CD, monitoring, metrics, etc.

```
$ serverless login
$ serverless deploy
```

To deploy without the dashboard you will need to remove `org` and `app` fields from the `serverless.yml`, and you won’t have to run `sls login` before deploying.

After running deploy, you should see output similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python-rest-api.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-python-rest-api
stage: dev
region: us-east-1
stack: aws-python-rest-api-dev
resources: 12
api keys:
  None
endpoints:
  ANY - https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
functions:
  api: aws-python-rest-api-dev-hello
layers:
  None
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [http event docs](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/).

### Invocation

After successful deployment, you can call the created application via HTTP:

```bash
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

Which should result in response similar to the following (removed `input` content for brevity):

```json
{
  "message": "Go Serverless v2.0! Your function executed successfully!",
  "input": {
    ...
  }
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
  "statusCode": 200,
  "body": "{\n  \"message\": \"Go Serverless v2.0! Your function executed successfully!\",\n  \"input\": \"\"\n}"
}
```

Alternatively, it is also possible to emulate API Gateway and Lambda locally by using `serverless-offline` plugin. In order to do that, execute the following command:

```bash
serverless plugin install -n serverless-offline
```

It will add the `serverless-offline` plugin to `devDependencies` in `package.json` file as well as will add it to `plugins` in `serverless.yml`.

After installation, you can start local emulation with:

```
serverless offline
```

To learn more about the capabilities of `serverless-offline`, please refer to its [GitHub repository](https://github.com/dherault/serverless-offline).

### Bundling dependencies

In case you would like to include 3rd party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).




Amplitude


Amplitude is the range of the Cycle from low to high, measured in whatever units ‘denominate’ that Cycle.  For example, in the financial world, a Cycle’s amplitude is typically measured in a currency.  The amplitude is the range in price from low to high within a Cycle.


Cycle Length


Cycle Length refers to the timing of the peaks or troughs within a Cycle.  In the financial world, the Cycle length is measured in calendar terms.  For example, one Daily Cycle might average 22 trading days between lows.  A longer duration Cycle is measured in weeks, while the secular Cycles are measure in months and even years. 


Daily Cycle (DC)


The shortest Cycle which I track at Bitcoin Live (although shorter Cycles exist) is the Daily Cycle, which is measured in trading days. All Cycles are measured from the low point of the Cycle to the next low point.  Each asset tracked has unique Cycle characteristics which we have tracked over time.  A typical Bitcoin Cycle will run for 60 days from low to low, in each Bull Market.  In a bear market, we find that Cycles are erratic, and the Cycle length will vary more than in a bull market.  Over a given period however, in a bear market the cycle length average should still come close.   


Daily Cycle Low (DCL)


The DCL is the low point of the Cycle which marks the end of one Daily Cycle and the beginning of the next Cycle. Understanding when the low is expected is critical to successful Cycle trading.


Weekly or Intermediate Cycle (IC)


The Weekly Cycle is measured in weeks and is the most important Cycle for investment purposes. The movements and flows of the Weekly Cycle are much more consistent than those of shorter cycles, and Weekly Cycles are long enough to allow investors to take a position without having to manage it on a daily basis.  The Bitcoin Weekly


Weekly Cycle Low (ICL)


The ICL is the low point of the Cycle which marks the end of one Weekly Cycle and the beginning of the next Cycle. Understanding when the low is expected is critical to successful Cycle trading.


Half Cycle Lows (HCL)


The Half Cycle Low is a natural mid-Cycle Low point that is found within most Cycles.  It’s typically a lower point within a Cycle that occurs around the middle of the expected length of the Cycle. 


Timing Bands


Every Cycle has a timing band for when we expect significant pivots to occur within the cycle.  Whether a Cycle Low or Cycle Top, we expect Cycles to form important pivots within expected time frames.  These time frames are not arbitrary numbers; they are derived from the history of an asset’s past Cycle behavior.  The more we know about an asset’s past Cycle characteristics, the better our odds are of predicting the future price movements.


It’s important to understand that these timing bands encompass only roughly 50% of cases.  When we say that a given market forms a Cycle Low between 56-64 trading days, for example, we are saying that a Cycle Low occurs within that timing band roughly 50% of the time.  The other 50% of the time it will fall outside of that band and it could be shorter or longer.  When we quote a Cycle duration we are quoting the average length of all cycles.    


Cycle Failure


A Cycle is considered to have failed when its price falls below the price at the point that began the Cycle.  A Cycle Failure is an important development because it typically signals (in about 90% of cases) that the more dominant Cycle is in decline or that we’re in a bear market.


For example, if a Daily Cycle fails it means that the ending point of the Cycle will be lower than its starting point.  That is the definition of a decline.  So failing Cycles are a normal process when an asset is in decline.  In bear markets we see many more Left Translated (more on Translation below) Cycles and Failed Cycles because the asset is in decline.   This is currently what we’re experiencing in the Bitcoin and Crypto space.