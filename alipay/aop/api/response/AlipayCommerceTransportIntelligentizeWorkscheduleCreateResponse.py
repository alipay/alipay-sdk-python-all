#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportIntelligentizeWorkscheduleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeWorkscheduleCreateResponse, self).__init__()
        self._ext_info = None
        self._service_task_id = None
        self._service_task_type = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def service_task_id(self):
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, value):
        self._service_task_id = value
    @property
    def service_task_type(self):
        return self._service_task_type

    @service_task_type.setter
    def service_task_type(self, value):
        self._service_task_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeWorkscheduleCreateResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'service_task_id' in response:
            self.service_task_id = response['service_task_id']
        if 'service_task_type' in response:
            self.service_task_type = response['service_task_type']
