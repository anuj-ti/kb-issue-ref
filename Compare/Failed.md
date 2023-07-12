1.
Jul 12, 2023, 13:15:36.230 (UTC+05:30)	[ERROR] AttributeError: 'list' object has no attribute 'items' Traceback (most recent call last):   File "/var/task/app.py", line 269, in lambda_handler     nodes = node_gen.generate_nodes_for_kg(chunk_kg, doc_extracted_data_json, initial_chunk_id, chunk_id)   File "/var/task/app.py", line 24, in generate_nodes_for_kg     for field, field_data in self.node_template.items():

2.
Jul 12, 2023, 13:15:32.869 (UTC+05:30)	[ERROR] AttributeError: 'list' object has no attribute 'items' Traceback (most recent call last):   File "/var/task/app.py", line 269, in lambda_handler     nodes = node_gen.generate_nodes_for_kg(chunk_kg, doc_extracted_data_json, initial_chunk_id, chunk_id)   File "/var/task/app.py", line 24, in generate_nodes_for_kg     for field, field_data in self.node_template.items():

3.
Jul 12, 2023, 12:59:49.491 (UTC+05:30)	[ERROR] AttributeError: 'list' object has no attribute 'items' Traceback (most recent call last):   File "/var/task/app.py", line 269, in lambda_handler     nodes = node_gen.generate_nodes_for_kg(chunk_kg, doc_extracted_data_json, initial_chunk_id, chunk_id)   File "/var/task/app.py", line 24, in generate_nodes_for_kg     for field, field_data in self.node_template.items():

4.
Unterminated string
Jul 12, 2023, 13:10:59.968 (UTC+05:30)	[ERROR] 2023-07-12T07:40:59.968Z bbe88773-a390-4529-9cb7-1cac3640dcfb fallback llm failed for stage kg_edges_creation: text-davinci-003 model failed after 2 retries..
Jul 12, 2023, 13:10:59.968 (UTC+05:30)	[ERROR] 2023-07-12T07:40:59.968Z bbe88773-a390-4529-9cb7-1cac3640dcfb Error occurred while running LLMWithRetriesAndFallback: fallback llm failed for stage kg_edges_creation: text-davinci-003 model failed after 2 retries..

5.
Unterminated string
Jul 12, 2023, 12:58:50.597 (UTC+05:30)	[ERROR] 2023-07-12T07:28:50.597Z cdb5a71d-b9bb-45a3-a486-84edde8fc40e fallback llm failed for stage kg_edges_creation: text-davinci-003 model failed after 2 retries..
Jul 12, 2023, 12:58:50.597 (UTC+05:30)	[ERROR] 2023-07-12T07:28:50.597Z cdb5a71d-b9bb-45a3-a486-84edde8fc40e Error occurred while running LLMWithRetriesAndFallback: fallback llm failed for stage kg_edges_creation: text-davinci-003 model failed after 2 retries..


