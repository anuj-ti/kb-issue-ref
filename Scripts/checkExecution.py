import time
import boto3


def check_state_machine_status(state_machine_arn):
    """
    Check the status of an AWS Step Functions state machine.

    Args:
        state_machine_arn (str): The ARN of the state machine to check.

    Returns:
        str: The status of the state machine.
    """
    session = boto3.Session(
        aws_access_key_id='###',
        aws_secret_access_key='###'
    )

    client = session.client('stepfunctions')

    while True:
        response = client.describe_state_machine(
            stateMachineArn=state_machine_arn
        )

        status = response['status']
        print(f"State machine status: {status}")

        # Check if the state machine has any executions
        executions = client.list_executions(
            stateMachineArn=state_machine_arn,
            statusFilter='RUNNING'  # Consider only running executions
        )['executions']

        if executions:
            print("There are running executions in the state machine.")
        else:
            print("No running executions. The execution has stopped.")
            break  # Exit the loop if there are no executions

        # Sleep for a short duration before checking again
        time.sleep(10)

    if status == 'ACTIVE':
        print("The state machine is running normally.")
    elif status == 'DELETING':
        print("The state machine is being deleted.")
    elif status == 'FAILED':
        print("The state machine encountered an error and is no longer running.")
    elif status == 'CREATING':
        print("The state machine is being created.")
    elif status == 'UPDATING':
        print("The state machine is being updated.")
    elif status == 'DELETING_RUNNING':
        print("The state machine is being deleted while running.")
    elif status == 'UPDATING_RUNNING':
        print("The state machine is being updated while running.")

    return status


state_machine_arn = 'arn:aws:states:us-east-1:346945241475:stateMachine:StateMachine-NuMoW1LF1G1f'

status = check_state_machine_status(state_machine_arn)
