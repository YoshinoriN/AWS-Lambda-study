```sh
aws-lambda-python# python-lambda-local -f hello_hello hello_aws_lambda.py hello.json

Loading function
[root - INFO - 2016-10-20 07:42:42,160] Event: {u'key3': u'\u307a\u307a\u307a\u306e\u307a', u'key2': u'\u307d\u3088\u307d\u3088', u'key1': u'\u307b\u3052\u3052'}
[root - INFO - 2016-10-20 07:42:42,160] START RequestId: e949415a-bd93-44b9-b465-c7c3f46fb801
[root - INFO - 2016-10-20 07:42:42,161] END RequestId: e949415a-bd93-44b9-b465-c7c3f46fb801
[root - INFO - 2016-10-20 07:42:42,161] RESULT:
{
    "stackTrace": [
        [
            "/usr/local/lib/python2.7/dist-packages/lambda_local/main.py",
            80,
            "execute",
            "result = func(event, context.activate())"
        ],
        [
            "hello_aws_lambda.py",
            7,
            "hello_hello",
            "print(\"value1 =\" + event['key1'])"
        ]
    ],
    "errorType": "UnicodeEncodeError",
    "errorMessage": "'latin-1' codec can't encode characters in position 8-10: ordinal not in range(256)"
}
```
