Received Event:
</br>

Received event: 
```
{'Input': {'index': 'documents', 'documents': [{'metadata': {'originalModifiedTime': '2022-06-22T13:07:09.681Z', 'originalOwnersEmail': 'spec.automation@devfactory.com', 'name': 'Prod2 Technical Teardown Spec - Jive:Jive Cloud - Jive Web UI - CENPRO-27043 - Week 15 2022', 'originalCreatedTime': '2022-03-18T15:22:32.528Z', 'originalFileSource': 'https://docs.google.com/document/d/1s0Cib3xZO3SB__4ft3xP5AKqCVBnpJcenWmQL5vyB5s', 'source': 'https://docs.google.com/document/d/1s0Cib3xZO3SB__4ft3xP5AKqCVBnpJcenWmQL5vyB5s', 'mimeType': 'application/vnd.google-apps.document', 'kgNodeId': None, 'parents': 'llm-kb-dataset', 'originalOwnersName': 'Spec Automation'}, 'id': '1ormdpfHESTYSNG1olB6DLGuHoCaYFs2QR89LhrhkSbQ_0', 'text': '[width="100%",cols="100%",options="header",]\n\|===\na\|\n*Prod2 Technical Teardown Spec*\n\n*Jive:Jive Cloud*\n\n*Jive Web UI*\n\n\|===\n\n[width="100%",cols="16%,32%,21%,31%",options="header",]\n\|===\n\|*Epic ID*\n\|https://workstation-df.atlassian.net/browse/CENPRO-27043[[.underline]#CENPRO-27043#]\n\|*Business SME* \|mailto:alex.pagoulatos@aurea.com[[.underline]#Alex\nPagoulatos#]\n\|*Start Date* \|2022-03-21 \|*Technical SME* a\|\nmailto:shakeel.shahzad@aurea.com[[.underline]#Shakeel Shahzad#]\n\nmailto:birkan.duman@aurea.com[[.underline]#Birkan Duman#]\n\nJhon Alexander Holguin (auth)\n\nDmitriy Elisov (video)\n\nRohit Kumar (video)\n\n\|*Submission Date (for Exec Review)* \|2022-04-16 \|*Type* \|Deep dive\nsurvey for a change spec.\n\n\|*Interview Recording* a\|\nhttps://drive.google.com/file/d/1fGfXnnBA-PC-BNvzmvWB2i0od1LKJdZD/view?usp=sharing[[.underline]#Technical\nSME Interview#] - (Shakeel Shahzad)\n\nhttps://crossover.zoom.us/rec/share/K5jKWmoiiDfBcGZKFTfaXrRVmxKJB1zSFcGRD6rIkQSe6YEgt8V_rYYq-fhLjUKt.7XGB2LNS_L8jJdK8?startTime=1648733691000%20(Passcode:%20@!Z.5T8%5E)[[.underline]#CloudFront\n+ FrontDoor#] (Jhon Alexander Holguin)\n\n\| \|\n\n\|*Related Specs*\n\|https://docs.google.com/document/d/1ut1NkA6GUIqKIeCbaUZ0esKYq2_Unpd2aTeO08EOfTM/edit[[.underline]#Jive\nCore Display Microservices Clone#] \| \|\n\n\|*Pre Mortem* \|The spec provides no short-term, easy answers for\n_significant_ Jive UI updates. \| \|\n\n\|*Previous Exec Feedback* \|N/A \| \|\n\n\|*Changes Since the Previous Version* \|N/A \| \|\n\n\|*Change Log* \|N/A \| \|\n\|===\n\n[width="99%",cols="25%,28%,47%",options="header",]'}], 'tenant': 'dev_customer_esw_space'}, 'ValueEnteredInForm': '{\n "Input": {\n "tenant.$": "States.Format(\'{}_{}\', $.ExecutionInput.customer_name, $.ExecutionInput.space_name)",\n "index": "documents",\n "documents": [\n {\n "id.$": "$.Input.chunk.id",\n "text.$": "$.Input.chunk.text",\n "metadata": json.merge({\n "source.$": "$.TaskResult.metadata.originalFileSource"\n }, "$.TaskResult.metadata")\n }\n ]\n }\n}'}
```

</br>
Payload:


```json
{
	"index": "documents",
	"documents": [
		{
			"metadata": {
				"originalModifiedTime": "2022-06-22T13:07:09.681Z",
				"originalOwnersEmail": "spec.automation@devfactory.com",
				"name": "Prod2 Technical Teardown Spec - Jive:Jive Cloud - Jive Web UI - CENPRO-27043 - Week 15 2022",
				"originalCreatedTime": "2022-03-18T15:22:32.528Z",
				"originalFileSource": "https://docs.google.com/document/d/1s0Cib3xZO3SB__4ft3xP5AKqCVBnpJcenWmQL5vyB5s",
				"source": "https://docs.google.com/document/d/1s0Cib3xZO3SB__4ft3xP5AKqCVBnpJcenWmQL5vyB5s",
				"mimeType": "application/vnd.google-apps.document",
				"kgNodeId": null,
				"parents": "llm-kb-dataset",
				"originalOwnersName": "Spec Automation"
			},
			"id": "1ormdpfHESTYSNG1olB6DLGuHoCaYFs2QR89LhrhkSbQ_0",
			"text": "[width=\"100%\",cols=\"100%\",options=\"header\",]\n\\|===\na\\|\n*Prod2 Technical Teardown Spec*\n\n*Jive:Jive Cloud*\n\n*Jive Web UI*\n\n\\|===\n\n[width=\"100%\",cols=\"16%,32%,21%,31%\",options=\"header\",]\n\\|===\n\\|*Epic ID*\n\\|https://workstation-df.atlassian.net/browse/CENPRO-27043[[.underline]#CENPRO-27043#]\n\\|*Business SME* \\|mailto:alex.pagoulatos@aurea.com[[.underline]#Alex\nPagoulatos#]\n\\|*Start Date* \\|2022-03-21 \\|*Technical SME* a\\|\nmailto:shakeel.shahzad@aurea.com[[.underline]#Shakeel Shahzad#]\n\nmailto:birkan.duman@aurea.com[[.underline]#Birkan Duman#]\n\nJhon Alexander Holguin (auth)\n\nDmitriy Elisov (video)\n\nRohit Kumar (video)\n\n\\|*Submission Date (for Exec Review)* \\|2022-04-16 \\|*Type* \\|Deep dive\nsurvey for a change spec.\n\n\\|*Interview Recording* a\\|\nhttps://drive.google.com/file/d/1fGfXnnBA-PC-BNvzmvWB2i0od1LKJdZD/view?usp=sharing[[.underline]#Technical\nSME Interview#] - (Shakeel Shahzad)\n\nhttps://crossover.zoom.us/rec/share/K5jKWmoiiDfBcGZKFTfaXrRVmxKJB1zSFcGRD6rIkQSe6YEgt8V_rYYq-fhLjUKt.7XGB2LNS_L8jJdK8?startTime=1648733691000%20(Passcode:%20@!Z.5T8%5E)[[.underline]#CloudFront\n+ FrontDoor#] (Jhon Alexander Holguin)\n\n\\| \\|\n\n\\|*Related Specs*\n\\|https://docs.google.com/document/d/1ut1NkA6GUIqKIeCbaUZ0esKYq2_Unpd2aTeO08EOfTM/edit[[.underline]#Jive\nCore Display Microservices Clone#] \\| \\|\n\n\\|*Pre Mortem* \\|The spec provides no short-term, easy answers for\n_significant_ Jive UI updates. \\| \\|\n\n\\|*Previous Exec Feedback* \\|N/A \\| \\|\n\n\\|*Changes Since the Previous Version* \\|N/A \\| \\|\n\n\\|*Change Log* \\|N/A \\| \\|\n\\|===\n\n[width=\"99%\",cols=\"25%,28%,47%\",options=\"header\",]"
		}
	],
	"tenant": "dev_customer_esw_space"
}
```
</br>
Jul 14, 2023, 14:52:14.946 (UTC+05:30)	[INFO] 2023-07-14T09:22:14.946Z 8d2598e8-3d52-4fae-a10a-d7a7a26f6214
</br>
Got response status: 400
</br>
Got response: {"error":"Request body invalid","message":"Expecting value: line 1 column 1 (char 0)"}
</br>
Failed to upsert texts!
</br>
Failed to upsert texts! Response: {"error":"Request body invalid","message":"Expecting value: line 1 column 1 (char 0)"}
</br>
Exception: Failed to upsert texts! Response: {"error":"Request body invalid","message":"Expecting value: line 1 column 1 (char 0)"} Traceback (most recent call last):   File "/var/task/app.py", line 69, in lambda_handler     raise e   File "/var/task/app.py", line 65, in lambda_handler     raise Exception(f"Failed to upsert texts! Response: {response.text}")
</br>
