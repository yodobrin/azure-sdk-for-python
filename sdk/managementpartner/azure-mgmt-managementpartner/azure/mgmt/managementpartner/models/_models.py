# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """this is the management partner operations error.

    :param error: this is the ExtendedErrorInfo property.
    :type error: ~azure.mgmt.managementpartner.models.ExtendedErrorInfo
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ExtendedErrorInfo'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ExtendedErrorInfo(msrest.serialization.Model):
    """this is the extended error info.

    :param code: this is the error response code. Possible values include: "NotFound", "Conflict",
     "BadRequest".
    :type code: str or ~azure.mgmt.managementpartner.models.ErrorResponseCode
    :param message: this is the extended error info message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtendedErrorInfo, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class OperationDisplay(msrest.serialization.Model):
    """this is the management partner operation.

    :param provider: the is management partner provider.
    :type provider: str
    :param resource: the is management partner resource.
    :type resource: str
    :param operation: the is management partner operation.
    :type operation: str
    :param description: the is management partner operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationList(msrest.serialization.Model):
    """this is the management partner operations list.

    :param value: this is the operation response list.
    :type value: list[~azure.mgmt.managementpartner.models.OperationResponse]
    :param next_link: Url to get the next page of items.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationResponse]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class OperationResponse(msrest.serialization.Model):
    """this is the management partner operations response.

    :param name: this is the operation response name.
    :type name: str
    :param display: this is the operation display.
    :type display: ~azure.mgmt.managementpartner.models.OperationDisplay
    :param origin: the is operation response origin information.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationResponse, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)


class PartnerResponse(msrest.serialization.Model):
    """this is the management partner operations response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param etag: Type of the partner.
    :type etag: int
    :ivar id: Identifier of the partner.
    :vartype id: str
    :ivar name: Name of the partner.
    :vartype name: str
    :ivar type: Type of resource. "Microsoft.ManagementPartner/partners".
    :vartype type: str
    :param partner_id: This is the partner id.
    :type partner_id: str
    :param partner_name: This is the partner name.
    :type partner_name: str
    :param tenant_id: This is the tenant id.
    :type tenant_id: str
    :param object_id: This is the object id.
    :type object_id: str
    :param version: This is the version.
    :type version: int
    :param updated_time: This is the DateTime when the partner was updated.
    :type updated_time: ~datetime.datetime
    :param created_time: This is the DateTime when the partner was created.
    :type created_time: ~datetime.datetime
    :param state: This is the partner state. Possible values include: "Active", "Deleted".
    :type state: str or ~azure.mgmt.managementpartner.models.ManagementPartnerState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'partner_id': {'key': 'properties.partnerId', 'type': 'str'},
        'partner_name': {'key': 'properties.partnerName', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'object_id': {'key': 'properties.objectId', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'int'},
        'updated_time': {'key': 'properties.updatedTime', 'type': 'iso-8601'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PartnerResponse, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
        self.id = None
        self.name = None
        self.type = None
        self.partner_id = kwargs.get('partner_id', None)
        self.partner_name = kwargs.get('partner_name', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.object_id = kwargs.get('object_id', None)
        self.version = kwargs.get('version', None)
        self.updated_time = kwargs.get('updated_time', None)
        self.created_time = kwargs.get('created_time', None)
        self.state = kwargs.get('state', None)
