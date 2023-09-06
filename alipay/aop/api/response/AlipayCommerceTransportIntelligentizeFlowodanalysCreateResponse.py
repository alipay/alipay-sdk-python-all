#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceSubTaskCreateOpenapiResult import ServiceSubTaskCreateOpenapiResult


class AlipayCommerceTransportIntelligentizeFlowodanalysCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeFlowodanalysCreateResponse, self).__init__()
        self._service_task_id = None
        self._service_task_type = None
        self._sub_task_create_result_list = None

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
    @property
    def sub_task_create_result_list(self):
        return self._sub_task_create_result_list

    @sub_task_create_result_list.setter
    def sub_task_create_result_list(self, value):
        if isinstance(value, list):
            self._sub_task_create_result_list = list()
            for i in value:
                if isinstance(i, ServiceSubTaskCreateOpenapiResult):
                    self._sub_task_create_result_list.append(i)
                else:
                    self._sub_task_create_result_list.append(ServiceSubTaskCreateOpenapiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeFlowodanalysCreateResponse, self).parse_response_content(response_content)
        if 'service_task_id' in response:
            self.service_task_id = response['service_task_id']
        if 'service_task_type' in response:
            self.service_task_type = response['service_task_type']
        if 'sub_task_create_result_list' in response:
            self.sub_task_create_result_list = response['sub_task_create_result_list']
