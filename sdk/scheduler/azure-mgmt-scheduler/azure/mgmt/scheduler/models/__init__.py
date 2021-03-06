# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import BasicAuthentication
    from ._models_py3 import ClientCertAuthentication
    from ._models_py3 import HttpAuthentication
    from ._models_py3 import HttpRequest
    from ._models_py3 import JobAction
    from ._models_py3 import JobCollectionDefinition
    from ._models_py3 import JobCollectionListResult
    from ._models_py3 import JobCollectionProperties
    from ._models_py3 import JobCollectionQuota
    from ._models_py3 import JobDefinition
    from ._models_py3 import JobErrorAction
    from ._models_py3 import JobHistoryDefinition
    from ._models_py3 import JobHistoryDefinitionProperties
    from ._models_py3 import JobHistoryFilter
    from ._models_py3 import JobHistoryListResult
    from ._models_py3 import JobListResult
    from ._models_py3 import JobMaxRecurrence
    from ._models_py3 import JobProperties
    from ._models_py3 import JobRecurrence
    from ._models_py3 import JobRecurrenceSchedule
    from ._models_py3 import JobRecurrenceScheduleMonthlyOccurrence
    from ._models_py3 import JobStateFilter
    from ._models_py3 import JobStatus
    from ._models_py3 import OAuthAuthentication
    from ._models_py3 import RetryPolicy
    from ._models_py3 import ServiceBusAuthentication
    from ._models_py3 import ServiceBusBrokeredMessageProperties
    from ._models_py3 import ServiceBusMessage
    from ._models_py3 import ServiceBusQueueMessage
    from ._models_py3 import ServiceBusTopicMessage
    from ._models_py3 import Sku
    from ._models_py3 import StorageQueueMessage
except (SyntaxError, ImportError):
    from ._models import BasicAuthentication  # type: ignore
    from ._models import ClientCertAuthentication  # type: ignore
    from ._models import HttpAuthentication  # type: ignore
    from ._models import HttpRequest  # type: ignore
    from ._models import JobAction  # type: ignore
    from ._models import JobCollectionDefinition  # type: ignore
    from ._models import JobCollectionListResult  # type: ignore
    from ._models import JobCollectionProperties  # type: ignore
    from ._models import JobCollectionQuota  # type: ignore
    from ._models import JobDefinition  # type: ignore
    from ._models import JobErrorAction  # type: ignore
    from ._models import JobHistoryDefinition  # type: ignore
    from ._models import JobHistoryDefinitionProperties  # type: ignore
    from ._models import JobHistoryFilter  # type: ignore
    from ._models import JobHistoryListResult  # type: ignore
    from ._models import JobListResult  # type: ignore
    from ._models import JobMaxRecurrence  # type: ignore
    from ._models import JobProperties  # type: ignore
    from ._models import JobRecurrence  # type: ignore
    from ._models import JobRecurrenceSchedule  # type: ignore
    from ._models import JobRecurrenceScheduleMonthlyOccurrence  # type: ignore
    from ._models import JobStateFilter  # type: ignore
    from ._models import JobStatus  # type: ignore
    from ._models import OAuthAuthentication  # type: ignore
    from ._models import RetryPolicy  # type: ignore
    from ._models import ServiceBusAuthentication  # type: ignore
    from ._models import ServiceBusBrokeredMessageProperties  # type: ignore
    from ._models import ServiceBusMessage  # type: ignore
    from ._models import ServiceBusQueueMessage  # type: ignore
    from ._models import ServiceBusTopicMessage  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import StorageQueueMessage  # type: ignore

from ._scheduler_management_client_enums import (
    DayOfWeek,
    HttpAuthenticationType,
    JobActionType,
    JobCollectionState,
    JobExecutionStatus,
    JobHistoryActionName,
    JobScheduleDay,
    JobState,
    RecurrenceFrequency,
    RetryType,
    ServiceBusAuthenticationType,
    ServiceBusTransportType,
    SkuDefinition,
)

__all__ = [
    'BasicAuthentication',
    'ClientCertAuthentication',
    'HttpAuthentication',
    'HttpRequest',
    'JobAction',
    'JobCollectionDefinition',
    'JobCollectionListResult',
    'JobCollectionProperties',
    'JobCollectionQuota',
    'JobDefinition',
    'JobErrorAction',
    'JobHistoryDefinition',
    'JobHistoryDefinitionProperties',
    'JobHistoryFilter',
    'JobHistoryListResult',
    'JobListResult',
    'JobMaxRecurrence',
    'JobProperties',
    'JobRecurrence',
    'JobRecurrenceSchedule',
    'JobRecurrenceScheduleMonthlyOccurrence',
    'JobStateFilter',
    'JobStatus',
    'OAuthAuthentication',
    'RetryPolicy',
    'ServiceBusAuthentication',
    'ServiceBusBrokeredMessageProperties',
    'ServiceBusMessage',
    'ServiceBusQueueMessage',
    'ServiceBusTopicMessage',
    'Sku',
    'StorageQueueMessage',
    'DayOfWeek',
    'HttpAuthenticationType',
    'JobActionType',
    'JobCollectionState',
    'JobExecutionStatus',
    'JobHistoryActionName',
    'JobScheduleDay',
    'JobState',
    'RecurrenceFrequency',
    'RetryType',
    'ServiceBusAuthenticationType',
    'ServiceBusTransportType',
    'SkuDefinition',
]
