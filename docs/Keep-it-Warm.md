## Keep it warm

Notice that what we are sure about is “amortized runtime”. Due to Lambda's “probably start a new instance” feature, we cannot assume a consistent runtime. Alternatively, we can also “keep the instance warm” by pinging it periodically, which takes some extra cost, but is reasonably  consistently fast.

To add "keep it warm" feature to your Lambda function, go to Lambda Management Console, enter your function, and in Designer pad, add a CloudWatch Events trigger, create a new rule (name doesn't matter here) or use an exisiting rule with Schedule expression `rate(5 minutes)`

![keep-it-warm](https://github.com/anchen1011/mxnet-lambda/blob/lit-docs/docs/keep-it-warm.png)
