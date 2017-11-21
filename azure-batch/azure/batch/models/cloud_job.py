# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudJob(Model):
    """An Azure Batch job.

    :param id: A string that uniquely identifies the job within the account.
     The ID is case-preserving and case-insensitive (that is, you may not have
     two IDs within an account that differ only by case).
    :type id: str
    :param display_name: The display name for the job.
    :type display_name: str
    :param uses_task_dependencies: Whether tasks in the job can define
     dependencies on each other. The default is false.
    :type uses_task_dependencies: bool
    :param url: The URL of the job.
    :type url: str
    :param e_tag: The ETag of the job. This is an opaque string. You can use
     it to detect whether the job has changed between requests. In particular,
     you can be pass the ETag when updating a job to specify that your changes
     should take effect only if nobody else has modified the job in the
     meantime.
    :type e_tag: str
    :param last_modified: The last modified time of the job. This is the last
     time at which the job level data, such as the job state or priority,
     changed. It does not factor in task-level changes such as adding new tasks
     or tasks changing state.
    :type last_modified: datetime
    :param creation_time: The creation time of the job.
    :type creation_time: datetime
    :param state: The current state of the job. Possible values include:
     'active', 'disabling', 'disabled', 'enabling', 'terminating', 'completed',
     'deleting'
    :type state: str or ~azure.batch.models.JobState
    :param state_transition_time: The time at which the job entered its
     current state.
    :type state_transition_time: datetime
    :param previous_state: The previous state of the job. This property is not
     set if the job is in its initial Active state. Possible values include:
     'active', 'disabling', 'disabled', 'enabling', 'terminating', 'completed',
     'deleting'
    :type previous_state: str or ~azure.batch.models.JobState
    :param previous_state_transition_time: The time at which the job entered
     its previous state. This property is not set if the job is in its initial
     Active state.
    :type previous_state_transition_time: datetime
    :param priority: The priority of the job. Priority values can range from
     -1000 to 1000, with -1000 being the lowest priority and 1000 being the
     highest priority. The default value is 0.
    :type priority: int
    :param constraints: The execution constraints for the job.
    :type constraints: ~azure.batch.models.JobConstraints
    :param job_manager_task: Details of a Job Manager task to be launched when
     the job is started.
    :type job_manager_task: ~azure.batch.models.JobManagerTask
    :param job_preparation_task: The Job Preparation task. The Job Preparation
     task is a special task run on each node before any other task of the job.
    :type job_preparation_task: ~azure.batch.models.JobPreparationTask
    :param job_release_task: The Job Release task. The Job Release task is a
     special task run at the end of the job on each node that has run any other
     task of the job.
    :type job_release_task: ~azure.batch.models.JobReleaseTask
    :param common_environment_settings: The list of common environment
     variable settings. These environment variables are set for all tasks in
     the job (including the Job Manager, Job Preparation and Job Release
     tasks). Individual tasks can override an environment setting specified
     here by specifying the same setting name with a different value.
    :type common_environment_settings:
     list[~azure.batch.models.EnvironmentSetting]
    :param pool_info: The pool settings associated with the job.
    :type pool_info: ~azure.batch.models.PoolInformation
    :param on_all_tasks_complete: The action the Batch service should take
     when all tasks in the job are in the completed state. The default is
     noaction. Possible values include: 'noAction', 'terminateJob'
    :type on_all_tasks_complete: str or ~azure.batch.models.OnAllTasksComplete
    :param on_task_failure: The action the Batch service should take when any
     task in the job fails. A task is considered to have failed if has a
     failureInfo. A failureInfo is set if the task completes with a non-zero
     exit code after exhausting its retry count, or if there was an error
     starting the task, for example due to a resource file download error. The
     default is noaction. Possible values include: 'noAction',
     'performExitOptionsJobAction'
    :type on_task_failure: str or ~azure.batch.models.OnTaskFailure
    :param metadata: A list of name-value pairs associated with the job as
     metadata. The Batch service does not assign any meaning to metadata; it is
     solely for the use of user code.
    :type metadata: list[~azure.batch.models.MetadataItem]
    :param execution_info: The execution information for the job.
    :type execution_info: ~azure.batch.models.JobExecutionInformation
    :param stats: Resource usage statistics for the entire lifetime of the
     job.
    :type stats: ~azure.batch.models.JobStatistics
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'uses_task_dependencies': {'key': 'usesTaskDependencies', 'type': 'bool'},
        'url': {'key': 'url', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'JobState'},
        'state_transition_time': {'key': 'stateTransitionTime', 'type': 'iso-8601'},
        'previous_state': {'key': 'previousState', 'type': 'JobState'},
        'previous_state_transition_time': {'key': 'previousStateTransitionTime', 'type': 'iso-8601'},
        'priority': {'key': 'priority', 'type': 'int'},
        'constraints': {'key': 'constraints', 'type': 'JobConstraints'},
        'job_manager_task': {'key': 'jobManagerTask', 'type': 'JobManagerTask'},
        'job_preparation_task': {'key': 'jobPreparationTask', 'type': 'JobPreparationTask'},
        'job_release_task': {'key': 'jobReleaseTask', 'type': 'JobReleaseTask'},
        'common_environment_settings': {'key': 'commonEnvironmentSettings', 'type': '[EnvironmentSetting]'},
        'pool_info': {'key': 'poolInfo', 'type': 'PoolInformation'},
        'on_all_tasks_complete': {'key': 'onAllTasksComplete', 'type': 'OnAllTasksComplete'},
        'on_task_failure': {'key': 'onTaskFailure', 'type': 'OnTaskFailure'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'execution_info': {'key': 'executionInfo', 'type': 'JobExecutionInformation'},
        'stats': {'key': 'stats', 'type': 'JobStatistics'},
    }

    def __init__(self, id=None, display_name=None, uses_task_dependencies=None, url=None, e_tag=None, last_modified=None, creation_time=None, state=None, state_transition_time=None, previous_state=None, previous_state_transition_time=None, priority=None, constraints=None, job_manager_task=None, job_preparation_task=None, job_release_task=None, common_environment_settings=None, pool_info=None, on_all_tasks_complete=None, on_task_failure=None, metadata=None, execution_info=None, stats=None):
        self.id = id
        self.display_name = display_name
        self.uses_task_dependencies = uses_task_dependencies
        self.url = url
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.creation_time = creation_time
        self.state = state
        self.state_transition_time = state_transition_time
        self.previous_state = previous_state
        self.previous_state_transition_time = previous_state_transition_time
        self.priority = priority
        self.constraints = constraints
        self.job_manager_task = job_manager_task
        self.job_preparation_task = job_preparation_task
        self.job_release_task = job_release_task
        self.common_environment_settings = common_environment_settings
        self.pool_info = pool_info
        self.on_all_tasks_complete = on_all_tasks_complete
        self.on_task_failure = on_task_failure
        self.metadata = metadata
        self.execution_info = execution_info
        self.stats = stats
