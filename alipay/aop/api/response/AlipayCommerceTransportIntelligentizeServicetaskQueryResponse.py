#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServiceSubTaskQueryOpenapiResult import ServiceSubTaskQueryOpenapiResult


class AlipayCommerceTransportIntelligentizeServicetaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportIntelligentizeServicetaskQueryResponse, self).__init__()
        self._end_time = None
        self._ext_info = None
        self._result_code = None
        self._result_msg = None
        self._service_task_id = None
        self._service_task_result = None
        self._service_task_status = None
        self._service_task_type = None
        self._start_time = None
        self._sub_task_list = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def service_task_id(self):
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, value):
        self._service_task_id = value
    @property
    def service_task_result(self):
        return self._service_task_result

    @service_task_result.setter
    def service_task_result(self, value):
        self._service_task_result = value
    @property
    def service_task_status(self):
        return self._service_task_status

    @service_task_status.setter
    def service_task_status(self, value):
        self._service_task_status = value
    @property
    def service_task_type(self):
        return self._service_task_type

    @service_task_type.setter
    def service_task_type(self, value):
        self._service_task_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_task_list(self):
        return self._sub_task_list

    @sub_task_list.setter
    def sub_task_list(self, value):
        if isinstance(value, list):
            self._sub_task_list = list()
            for i in value:
                if isinstance(i, ServiceSubTaskQueryOpenapiResult):
                    self._sub_task_list.append(i)
                else:
                    self._sub_task_list.append(ServiceSubTaskQueryOpenapiResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportIntelligentizeServicetaskQueryResponse, self).parse_response_content(response_content)
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'service_task_id' in response:
            self.service_task_id = response['service_task_id']
        if 'service_task_result' in response:
            self.service_task_result = response['service_task_result']
        if 'service_task_status' in response:
            self.service_task_status = response['service_task_status']
        if 'service_task_type' in response:
            self.service_task_type = response['service_task_type']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'sub_task_list' in response:
            self.sub_task_list = response['sub_task_list']
