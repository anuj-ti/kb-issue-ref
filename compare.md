### Turbo Output

Document ID: 12J_waJEbC1EEBL3MVy_RqyOWfh6ZslV45b-csN4B7Bs_0

Matching Entities:
ID: prod3, Type: product, Desc: Product Vision Spec
ID: cenpro-27036, Type: id, Desc: None
ID: howard abrams, Type: person, Desc: Author of technical spec document
ID: rahul subramaniam, Type: person, Desc: Business subject matter expert
ID: previous roadmap, Type: previous published version, Desc: None
ID: product summary, Type: summary, Desc: Briefly recap what the product is, focusing on what�s relevant to this Product Vision.
ID: devflows, Type: product, Desc: Technical spec document
ID: current product state, Type: current product state, Desc: Briefly recap how the product has evolved, focusing on what�s relevant to this Product Vision.
ID: it worker, Type: role, Desc: None
ID: aws, Type: technology, Desc: None
ID: apis, Type: technology, Desc: None
ID: subflows, Type: technology, Desc: None
ID: http requests, Type: technology, Desc: None
ID: scalability, Type: technology, Desc: None
ID: simplicity, Type: technology, Desc: None
ID: asynchronous, Type: technology, Desc: None
ID: acid transactions, Type: technology, Desc: None

Non-Matching Entities:
ID: cnu, Type: organization, Desc: None
ID: tpm, Type: organization, Desc: None
ID: it developer, Type: role, Desc: None
ID: prod3 product vision spec, Type: type, Desc: Type of technical spec document

Matching Edges:
Source: prod3, Type: PRODUCT_VISION_SPEC, Target: cenpro-27036
Source: prod3, Type: AUTHOR, Target: howard abrams
Source: devflows, Type: p2spec_author, Target: howard abrams
Source: prod3, Type: BUSINESS_SME, Target: rahul subramaniam
Source: prod3, Type: BUSINESS_SME, Target: rahul subramaniam
Source: prod3, Type: RELATED_SPECS, Target: previous roadmap
Source: prod3, Type: PREVIOUS_PUBLISHED_VERSION, Target: previous roadmap
Source: prod3, Type: PRODUCT_SUMMARY, Target: product summary
Source: prod3, Type: KEY_BETS, Target: devflows
Source: prod3, Type: CURRENT_PRODUCT_STATE, Target: current product state
Source: prod3, Type: KEY_BETS, Target: it worker
Source: prod3, Type: KEY_BETS, Target: aws
Source: prod3, Type: KEY_BETS, Target: aws
Source: prod3, Type: KEY_BETS, Target: aws
Source: prod3, Type: KEY_BETS, Target: apis
Source: prod3, Type: KEY_BETS, Target: subflows
Source: prod3, Type: KEY_BETS, Target: http requests
Source: prod3, Type: KEY_BETS, Target: scalability
Source: prod3, Type: KEY_BETS, Target: simplicity
Source: prod3, Type: KEY_BETS, Target: asynchronous
Source: prod3, Type: KEY_BETS, Target: acid transactions

Document ID: 12J_waJEbC1EEBL3MVy_RqyOWfh6ZslV45b-csN4B7Bs_1

Matching Entities:
ID: it worker, Type: role, Desc: None
ID: aws, Type: technology, Desc: None
ID: it developer, Type: role, Desc: None
ID: api, Type: technology, Desc: Application Programming Interface
ID: acid, Type: technology, Desc: Atomicity, Consistency, Isolation, Durability
ID: it workers, Type: job title, Desc: Non-developers who work in the IT field

Non-Matching Entities:
ID: ifttt, Type: software, Desc: A platform that allows users to create chains of simple conditional statements
ID: zapier, Type: software, Desc: A platform that connects different apps and automates workflows
ID: tray.io, Type: software, Desc: A platform for building integrations and automating workflows
ID: mulesoft, Type: software, Desc: A platform for building application networks
ID: dms, Type: technology, Desc: Database Migration Service
ID: lambda, Type: technology, Desc: A serverless computing service
ID: firehose, Type: technology, Desc: A real-time data streaming service
ID: glue, Type: technology, Desc: A fully managed extract, transform, and load (ETL) service
ID: comprehend, Type: technology, Desc: A natural language processing (NLP) service
ID: s3, Type: technology, Desc: Amazon Simple Storage Service
ID: athena, Type: technology, Desc: An interactive query service
ID: quicksight, Type: technology, Desc: A business intelligence (BI) service

Matching Edges:
Source: aws, Type: ENABLES, Target: it worker
Source: aws, Type: ENABLES, Target: aws
Source: aws, Type: ENABLES, Target: aws
Source: aws, Type: ENABLES, Target: aws
Source: aws, Type: ENABLES, Target: it developer
Source: aws, Type: ENABLES, Target: api
Source: aws, Type: ENABLES, Target: acid
Source: aws, Type: ENABLES, Target: it workers

Document ID: 12J_waJEbC1EEBL3MVy_RqyOWfh6ZslV45b-csN4B7Bs_2

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: aws, Type: technology, Desc: None
ID: it workers, Type: job title, Desc: Non-developers who work in the IT field
ID: windows, Type: software, Desc: An operating system
ID: linux, Type: software, Desc: An operating system
ID: trilogy, Type: organization, Desc: A company
ID: http, Type: term, Desc: Hypertext Transfer Protocol
ID: aws services, Type: software, Desc: Services provided by AWS

Non-Matching Entities:
ID: lambda, Type: technology, Desc: A serverless computing service
ID: glue, Type: technology, Desc: A fully managed extract, transform, and load (ETL) service
ID: comprehend, Type: technology, Desc: A natural language processing (NLP) service
ID: ip, Type: term, Desc: Intellectual Property
ID: it departments, Type: organization, Desc: Departments that work in IT
ID: sdk, Type: software, Desc: Software Development Kit
ID: sqs, Type: software, Desc: A message queuing service provided by AWS
ID: cloud developers, Type: person, Desc: Developers who work with cloud technologies
ID: devflow flow builders, Type: person, Desc: People who build DevFlow flows
ID: kinesis, Type: software, Desc: A data streaming service provided by AWS
ID: oracle, Type: software, Desc: A database management system
ID: data lake, Type: term, Desc: A storage repository that holds a vast amount of raw data in its native format

Matching Edges:
Source: trilogy, Type: BELIEVES, Target: aws
Source: devflows, Type: SOLVES, Target: it workers
Source: aws, Type: OS_OF_THE_FUTURE, Target: windows
Source: aws, Type: OS_OF_THE_FUTURE, Target: linux
Source: devflows, Type: EXTENSIBILITY_MECHANISM, Target: http
Source: devflows, Type: MANAGES, Target: aws services

Document ID: 12J_waJEbC1EEBL3MVy_RqyOWfh6ZslV45b-csN4B7Bs_3

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: aws, Type: technology, Desc: None
ID: subflows, Type: technology, Desc: None
ID: http, Type: term, Desc: Hypertext Transfer Protocol
ID: flow wizards, Type: software, Desc: A library of wizards for building flows
ID: pattern flows, Type: software, Desc: High-level nodes that implement common patterns
ID: core actions, Type: software, Desc: Actions built into DevFlows

Non-Matching Entities:
ID: glue, Type: technology, Desc: A fully managed extract, transform, and load (ETL) service
ID: comprehend, Type: technology, Desc: A natural language processing (NLP) service
ID: kinesis, Type: software, Desc: A data streaming service provided by AWS
ID: oracle, Type: software, Desc: A database management system
ID: isv, Type: organization, Desc: Independent Software Vendor
ID: cloudformation, Type: software, Desc: A service for managing AWS infrastructure as code
ID: ipaas, Type: software, Desc: Integration Platform as a Service

Matching Edges:
Source: devflows, Type: ADD_BUSINESS_VALUE, Target: aws
Source: devflows, Type: EXTEND_PROGRAMMING_MODEL, Target: subflows
Source: devflows, Type: EXTEND_PROGRAMMING_MODEL, Target: http
Source: devflows, Type: EXTEND_PROGRAMMING_MODEL, Target: flow wizards
Source: devflows, Type: EXTEND_PROGRAMMING_MODEL, Target: pattern flows
Source: devflows, Type: EXTEND_PROGRAMMING_MODEL, Target: core actions

Document ID: 12J_waJEbC1EEBL3MVy_RqyOWfh6ZslV45b-csN4B7Bs_4

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: aws, Type: technology, Desc: None
ID: cloudformation, Type: software, Desc: A service for managing AWS infrastructure as code
ID: ipaas, Type: software, Desc: Integration Platform as a Service
ID: paas, Type: technology, Desc: Platform as a Service

Non-Matching Entities:

Matching Edges:
Source: devflows, Type: USES, Target: aws
Source: devflows, Type: NOT_FOR, Target: cloudformation
Source: devflows, Type: NOT_FOR, Target: ipaas
Source: devflows, Type: FOR, Target: paas

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_0

Matching Entities:
ID: rahul subramaniam, Type: person, Desc: Business subject matter expert
ID: product summary, Type: summary, Desc: Briefly recap what the product is, focusing on what�s relevant to this Product Vision.
ID: devflows, Type: product, Desc: Technical spec document
ID: current product state, Type: current product state, Desc: Briefly recap how the product has evolved, focusing on what�s relevant to this Product Vision.
ID: aws, Type: technology, Desc: None
ID: s3, Type: technology, Desc: Amazon Simple Storage Service
ID: prod2, Type: product, Desc: Product Evolution Spec
ID: cnu:devfactory, Type: organization, Desc: DevFactory
ID: cenpro-23733, Type: technical term, Desc: None
ID: steve brain, Type: person, Desc: Author of technical spec document
ID: interview recording, Type: technical term, Desc: None
ID: visualbasic, Type: technical term, Desc: None
ID: saas, Type: technical term, Desc: None
ID: programming paradigm, Type: technical term, Desc: None
ID: cloud components, Type: technical term, Desc: None
ID: discoverable library, Type: technical term, Desc: None
ID: deployment decisions, Type: technical term, Desc: None
ID: aws ecosystem, Type: technical term, Desc: None
ID: forecast, Type: technical term, Desc: None
ID: athena & quicksight, Type: technical term, Desc: None
ID: redshift, Type: technical term, Desc: None
ID: ses, Type: technical term, Desc: None
ID: dynamodb, Type: technical term, Desc: None
ID: scheduled events, Type: technical term, Desc: None
ID: eventbridge, Type: technical term, Desc: None

Non-Matching Entities:
ID: aws adapters, Type: technical term, Desc: None
ID: input data, Type: technical term, Desc: None
ID: previous published version, Type: technical term, Desc: None
ID: changes since previous version, Type: technical term, Desc: None
ID: prod2 product evolution spec, Type: type, Desc: Type of technical spec document

Matching Edges:
Source: prod2, Type: BUSINESS_SME, Target: rahul subramaniam
Source: prod2, Type: PRODUCT_SUMMARY, Target: product summary
Source: product summary, Type: RECAPS, Target: devflows
Source: current product state, Type: RECAPS, Target: devflows
Source: prod2, Type: CURRENT_PRODUCT_STATE, Target: current product state
Source: product summary, Type: RECAPS, Target: aws
Source: current product state, Type: RECAPS, Target: s3
Source: prod2, Type: AUTHORED_BY, Target: cnu:devfactory
Source: prod2, Type: RELATED_TO, Target: cenpro-23733
Source: prod2, Type: AUTHOR, Target: steve brain
Source: devflows, Type: p2spec_author, Target: steve brain
Source: prod2, Type: INPUT_DATA, Target: interview recording
Source: product summary, Type: RECAPS, Target: visualbasic
Source: product summary, Type: RECAPS, Target: saas
Source: product summary, Type: RECAPS, Target: programming paradigm
Source: product summary, Type: RECAPS, Target: cloud components
Source: product summary, Type: RECAPS, Target: discoverable library
Source: product summary, Type: RECAPS, Target: deployment decisions
Source: product summary, Type: RECAPS, Target: aws ecosystem
Source: current product state, Type: RECAPS, Target: forecast
Source: current product state, Type: RECAPS, Target: athena & quicksight
Source: current product state, Type: RECAPS, Target: redshift
Source: current product state, Type: RECAPS, Target: ses
Source: current product state, Type: RECAPS, Target: dynamodb
Source: current product state, Type: RECAPS, Target: scheduled events
Source: current product state, Type: RECAPS, Target: eventbridge

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_1

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: aws, Type: technology, Desc: None
ID: s3, Type: technology, Desc: Amazon Simple Storage Service
ID: dynamodb, Type: technical term, Desc: None
ID: evolution strategy, Type: product, Desc: A strategy for evolving the product
ID: amazon connect, Type: product, Desc: An enterprise product
ID: aws taxonomy of services, Type: taxonomy, Desc: A taxonomy of services provided by AWS
ID: analytics, Type: service group, Desc: A service group for analytics
ID: developer tools, Type: category, Desc: A category of tools for developers
ID: front end web & mobile, Type: category, Desc: A category for front end web and mobile development
ID: game tech, Type: category, Desc: A category for game technology
ID: iot, Type: category, Desc: A category for Internet of Things
ID: management & governance, Type: category, Desc: A category for management and governance
ID: media services, Type: category, Desc: A category for media services
ID: migration & transfer, Type: category, Desc: A category for migration and transfer
ID: network and cdns, Type: category, Desc: A category for network and content delivery networks
ID: quantum technologies, Type: category, Desc: A category for quantum technologies
ID: robotics, Type: category, Desc: A category for robotics
ID: satellite, Type: category, Desc: A category for satellite
ID: serverless, Type: category, Desc: A category for serverless
ID: vr & ar, Type: category, Desc: A category for virtual reality and augmented reality

Non-Matching Entities:
ID: cloudfix, Type: product, Desc: A product for cloud financial management
ID: devflows itself, Type: product, Desc: A container environment

Matching Edges:
Source: aws, Type: PART_OF, Target: devflows
Source: evolution strategy, Type: INCREASE_COVERAGE, Target: aws
Source: aws, Type: PART_OF, Target: s3
Source: aws, Type: PART_OF, Target: dynamodb
Source: aws, Type: PART_OF, Target: amazon connect
Source: aws, Type: PART_OF, Target: aws taxonomy of services
Source: evolution strategy, Type: THEME, Target: analytics
Source: aws taxonomy of services, Type: PART_OF, Target: analytics
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: developer tools
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: front end web & mobile
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: game tech
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: iot
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: management & governance
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: media services
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: migration & transfer
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: network and cdns
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: quantum technologies
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: robotics
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: satellite
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: serverless
Source: aws taxonomy of services, Type: NOT_PRIORITIZE, Target: vr & ar

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_2

Matching Entities:
ID: api, Type: technology, Desc: Application Programming Interface
ID: glue, Type: technology, Desc: A fully managed extract, transform, and load (ETL) service
ID: athena, Type: technology, Desc: An interactive query service
ID: sqs, Type: software, Desc: A message queuing service provided by AWS
ID: kinesis, Type: software, Desc: A data streaming service provided by AWS
ID: redshift, Type: technical term, Desc: None
ID: eventbridge, Type: technical term, Desc: None
ID: analytics, Type: service group, Desc: A service group for analytics
ID: elasticsearch, Type: software, Desc: A query node for DevFlows.
ID: application integration, Type: category, Desc: The Application Integration category in AWS is a suite of services that enable communication between decoupled components.
ID: sns, Type: software, Desc: A service for sending messages.
ID: step functions, Type: software, Desc: A service for orchestrating flows.

Non-Matching Entities:

Matching Edges:
Source: application integration, Type: COMBINATION_OF, Target: api
Source: analytics, Type: COMBINATION_OF, Target: api
Source: analytics, Type: COMBINATION_OF, Target: glue
Source: analytics, Type: COMBINATION_OF, Target: athena
Source: application integration, Type: COMBINATION_OF, Target: sqs
Source: analytics, Type: COMBINATION_OF, Target: sqs
Source: analytics, Type: COMBINATION_OF, Target: kinesis
Source: analytics, Type: COMBINATION_OF, Target: redshift
Source: analytics, Type: COMBINATION_OF, Target: eventbridge
Source: application integration, Type: COMBINATION_OF, Target: eventbridge
Source: analytics, Type: COMBINATION_OF, Target: elasticsearch
Source: analytics, Type: COMBINATION_OF, Target: sns
Source: application integration, Type: COMBINATION_OF, Target: sns
Source: analytics, Type: COMBINATION_OF, Target: step functions
Source: application integration, Type: COMBINATION_OF, Target: step functions

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_3

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: api, Type: technology, Desc: Application Programming Interface
ID: sqs, Type: software, Desc: A message queuing service provided by AWS
ID: eventbridge, Type: technical term, Desc: None
ID: sns, Type: software, Desc: A service for sending messages.
ID: step functions, Type: software, Desc: A service for orchestrating flows.
ID: rest, Type: technical term, Desc: Representational State Transfer
ID: graphql, Type: technical term, Desc: A query language for APIs
ID: business applications, Type: technical term, Desc: Higher level capabilities useful in enterprise flows
ID: workdocs, Type: technical term, Desc: A document collaboration service
ID: pinpoint, Type: technical term, Desc: A mobile engagement service

Non-Matching Entities:

Matching Edges:
Source: workdocs, Type: ACTION, Target: devflows
Source: sqs, Type: ACTION, Target: devflows
Source: sns, Type: INPUT_NODE, Target: devflows
Source: sqs, Type: INPUT_NODE, Target: devflows
Source: eventbridge, Type: ACTION, Target: devflows
Source: step functions, Type: CALLS, Target: devflows
Source: eventbridge, Type: INPUT_NODE, Target: devflows
Source: business applications, Type: SOLVES, Target: devflows
Source: pinpoint, Type: ACTION, Target: devflows
Source: sns, Type: ACTION, Target: devflows
Source: workdocs, Type: SOLVES, Target: devflows
Source: devflows, Type: FIT_WELL_WITH, Target: api
Source: devflows, Type: FIT_WELL_WITH, Target: sqs
Source: devflows, Type: FIT_WELL_WITH, Target: eventbridge
Source: devflows, Type: FIT_WELL_WITH, Target: sns
Source: devflows, Type: FIT_WELL_WITH, Target: step functions
Source: api, Type: ACTION, Target: rest
Source: devflows, Type: FIT_WELL_WITH, Target: rest
Source: devflows, Type: FIT_WELL_WITH, Target: graphql
Source: devflows, Type: FIT_WELL_WITH, Target: business applications
Source: devflows, Type: FIT_WELL_WITH, Target: workdocs
Source: devflows, Type: FIT_WELL_WITH, Target: pinpoint

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_4

Matching Entities:
ID: athena, Type: technology, Desc: An interactive query service
ID: redshift, Type: technical term, Desc: None
ID: dynamodb, Type: technical term, Desc: None
ID: business applications, Type: technical term, Desc: Higher level capabilities useful in enterprise flows
ID: workdocs, Type: technical term, Desc: A document collaboration service
ID: pinpoint, Type: technical term, Desc: A mobile engagement service
ID: devflow, Type: software, Desc: A software that can start a DevFlow when something happens in an application
ID: simple email (ses), Type: software, Desc: A software that can send and receive emails simply
ID: connect, Type: software, Desc: A software that can allow an event in Connect to trigger a flow
ID: honeycode, Type: software, Desc: A software that can allow a simple UI in Honeycode to trigger a flow
ID: database, Type: software, Desc: A portfolio of database services provided by AWS
ID: documentdb, Type: software, Desc: A competing technology to DynamoDB

Non-Matching Entities:

Matching Edges:
Source: database, Type: PROVIDES, Target: athena
Source: database, Type: PROVIDES, Target: redshift
Source: database, Type: PROVIDES, Target: dynamodb
Source: workdocs, Type: MOVED_TO_SPECIFIC_FOLDER, Target: business applications
Source: workdocs, Type: MOVE_FILE, Target: business applications
Source: pinpoint, Type: SEND_EMAIL, Target: business applications
Source: devflow, Type: TAKES_ACTION_ON, Target: business applications
Source: honeycode, Type: TRIGGER_FLOW, Target: business applications
Source: connect, Type: TRIGGER_FLOW, Target: business applications
Source: workdocs, Type: INPUT_NODES, Target: business applications
Source: workdocs, Type: INPUT_NODES, Target: workdocs
Source: business applications, Type: SOLVES, Target: workdocs
Source: business applications, Type: SOLVES, Target: pinpoint
Source: business applications, Type: SOLVES, Target: devflow
Source: pinpoint, Type: SEND_EMAIL, Target: simple email (ses)
Source: business applications, Type: SOLVES, Target: simple email (ses)
Source: business applications, Type: SOLVES, Target: connect
Source: business applications, Type: SOLVES, Target: honeycode
Source: business applications, Type: SOLVES, Target: database
Source: database, Type: PROVIDES, Target: documentdb

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_5

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: aws, Type: technology, Desc: None
ID: athena, Type: technology, Desc: An interactive query service
ID: forecast, Type: technical term, Desc: None
ID: redshift, Type: technical term, Desc: None
ID: dynamodb, Type: technical term, Desc: None
ID: documentdb, Type: software, Desc: A competing technology to DynamoDB
ID: sql query adapter, Type: software, Desc: An adapter to support queries for Aurora and RDS
ID: neptune, Type: database, Desc: A graph database service provided by AWS
ID: timestream, Type: database, Desc: A time series database service provided by AWS
ID: joe, Type: person, Desc: A person
ID: machine learning, Type: theme, Desc: A theme related to machine learning
ID: sagemaker, Type: software, Desc: A machine learning platform provided by AWS
ID: central engineering, Type: organization, Desc: An organization
ID: ml, Type: service, Desc: Machine learning services provided by AWS

Non-Matching Entities:

Matching Edges:
Source: aws, Type: PROVIDES, Target: devflows
Source: aws, Type: PROVIDES, Target: athena
Source: central engineering, Type: SHIPPED, Target: forecast
Source: aws, Type: PROVIDES, Target: redshift
Source: aws, Type: PROVIDES, Target: dynamodb
Source: aws, Type: PROVIDES, Target: documentdb
Source: aws, Type: PROVIDES, Target: sql query adapter
Source: aws, Type: PROVIDES, Target: neptune
Source: aws, Type: PROVIDES, Target: timestream
Source: joe, Type: NOT_IN, Target: timestream
Source: aws, Type: PROVIDES, Target: machine learning
Source: aws, Type: PROVIDES, Target: sagemaker
Source: aws, Type: PROVIDES, Target: ml

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_6

Matching Entities:
ID: aws, Type: technology, Desc: None
ID: comprehend, Type: technology, Desc: A natural language processing (NLP) service
ID: forecast, Type: technical term, Desc: None
ID: sagemaker, Type: software, Desc: A machine learning platform provided by AWS
ID: ml, Type: service, Desc: Machine learning services provided by AWS
ID: personalize, Type: software, Desc: AWS service for personalization
ID: rekognition, Type: software, Desc: AWS service for image and video analysis
ID: translate, Type: software, Desc: AWS service for language translation
ID: lake formation, Type: software, Desc: AWS service for data lake management
ID: iam, Type: software, Desc: AWS Identity and Access Management service
ID: secretsmanager, Type: software, Desc: AWS service for managing secrets

Non-Matching Entities:
ID: guardduty, Type: software, Desc: AWS service for threat detection
ID: macie, Type: software, Desc: AWS service for data security

Matching Edges:
Source: aws, Type: HAS_SERVICE, Target: comprehend
Source: aws, Type: HAS_SERVICE, Target: forecast
Source: aws, Type: HAS_SERVICE, Target: sagemaker
Source: aws, Type: HAS_SERVICE, Target: ml
Source: aws, Type: HAS_SERVICE, Target: personalize
Source: aws, Type: HAS_SERVICE, Target: rekognition
Source: aws, Type: HAS_SERVICE, Target: translate
Source: aws, Type: HAS_SERVICE, Target: lake formation
Source: aws, Type: HAS_SERVICE, Target: iam
Source: aws, Type: HAS_SERVICE, Target: secretsmanager

Document ID: 14CKAlP03u4wRyhbsSrPwEQzLxqljH57LU7gJLPCZeD8_7

Matching Entities:
ID: devflows, Type: product, Desc: Technical spec document
ID: dms, Type: technology, Desc: Database Migration Service
ID: s3, Type: technology, Desc: Amazon Simple Storage Service
ID: secretsmanager, Type: software, Desc: AWS service for managing secrets
ID: guardduty, Type: software, Desc: AWS service for threat detection
ID: macie, Type: software, Desc: AWS service for data security
ID: storage, Type: theme, Desc: AWS has an array of services for file storage, block storage, data transfer and edge storage.
ID: efs, Type: software, Desc: Read or write a file to EFS.
ID: aws transfer, Type: software, Desc: Orchestrate transfers using DevFlows.
ID: aws backup, Type: software, Desc: Orchestrate backups using DevFlows.
ID: appendices, Type: section, Desc: None
ID: appendix a, Type: section, Desc: Archived Themes
ID: appendix b, Type: section, Desc: Other AWS Services we will want to build Adapters for
ID: chime, Type: software, Desc: None
ID: chime voice connector, Type: software, Desc: None
ID: elasticache, Type: software, Desc: None
ID: location service, Type: software, Desc: None
ID: lex, Type: software, Desc: None
ID: polly, Type: software, Desc: None
ID: kendra, Type: software, Desc: None
ID: textract, Type: software, Desc: https://workstation-df.atlassian.net/browse/CENPRO-26490[[.underline]#Textract#]
ID: transcribe, Type: software, Desc: https://workstation-df.atlassian.net/browse/CENPRO-26491[[.underline]#Transcribe#]
ID: elemental media, Type: software, Desc: None
ID: application migration service, Type: software, Desc: None
ID: application discovery service, Type: software, Desc: None
ID: cognito, Type: software, Desc: None
ID: aws glacier, Type: software, Desc: None
ID: appsync, Type: software, Desc: None
ID: codecommit, Type: software, Desc: None
ID: codebuild, Type: software, Desc: None
ID: codepipeline, Type: software, Desc: None
ID: codedeploy, Type: software, Desc: None

Non-Matching Entities:
ID: joe, Type: person, Desc: A person

Matching Edges:
Source: macie, Type: TRIGGERED_BY, Target: devflows
Source: guardduty, Type: TRIGGERED_BY, Target: devflows
Source: aws backup, Type: ORCHESTRATE_BACKUPS, Target: devflows
Source: aws transfer, Type: ORCHESTRATE_TRANSFERS, Target: devflows
Source: appendix b, Type: CONSIDERS, Target: dms
Source: storage, Type: HAS_SERVICES, Target: s3
Source: appendix b, Type: CONSIDERS, Target: secretsmanager
Source: efs, Type: READ_WRITE_FILE, Target: efs
Source: appendices, Type: CONTAINS, Target: appendix a
Source: appendices, Type: CONTAINS, Target: appendix b
Source: appendix b, Type: CONSIDERS, Target: chime
Source: appendix b, Type: CONSIDERS, Target: chime voice connector
Source: appendix b, Type: CONSIDERS, Target: elasticache
Source: appendix b, Type: CONSIDERS, Target: location service
Source: appendix b, Type: CONSIDERS, Target: lex
Source: appendix b, Type: CONSIDERS, Target: polly
Source: appendix b, Type: CONSIDERS, Target: kendra
Source: appendix b, Type: CONSIDERS, Target: textract
Source: appendix b, Type: CONSIDERS, Target: transcribe
Source: appendix b, Type: CONSIDERS, Target: elemental media
Source: appendix b, Type: CONSIDERS, Target: application migration service
Source: appendix b, Type: CONSIDERS, Target: application discovery service
Source: appendix b, Type: CONSIDERS, Target: cognito
Source: appendix b, Type: CONSIDERS, Target: aws glacier
Source: appendix b, Type: CONSIDERS, Target: appsync
Source: appendix b, Type: CONSIDERS, Target: codecommit
Source: appendix b, Type: CONSIDERS, Target: codebuild
Source: appendix b, Type: CONSIDERS, Target: codepipeline
Source: appendix b, Type: CONSIDERS, Target: codedeploy
