#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppServiceSchemaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceSchemaQueryResponse, self).__init__()
        self._category_id = None
        self._schema_version = None
        self._schema_xml = None
        self._template_type = None
        self._user_service_delivery_type = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def schema_version(self):
        return self._schema_version

    @schema_version.setter
    def schema_version(self, value):
        self._schema_version = value
    @property
    def schema_xml(self):
        return self._schema_xml

    @schema_xml.setter
    def schema_xml(self, value):
        self._schema_xml = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def user_service_delivery_type(self):
        return self._user_service_delivery_type

    @user_service_delivery_type.setter
    def user_service_delivery_type(self, value):
        self._user_service_delivery_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceSchemaQueryResponse, self).parse_response_content(response_content)
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'schema_version' in response:
            self.schema_version = response['schema_version']
        if 'schema_xml' in response:
            self.schema_xml = response['schema_xml']
        if 'template_type' in response:
            self.template_type = response['template_type']
        if 'user_service_delivery_type' in response:
            self.user_service_delivery_type = response['user_service_delivery_type']
