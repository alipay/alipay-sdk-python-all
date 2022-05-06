#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudFinsaasOperationtaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudFinsaasOperationtaskCreateResponse, self).__init__()
        self._operation_task_id = None

    @property
    def operation_task_id(self):
        return self._operation_task_id

    @operation_task_id.setter
    def operation_task_id(self, value):
        self._operation_task_id = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudFinsaasOperationtaskCreateResponse, self).parse_response_content(response_content)
        if 'operation_task_id' in response:
            self.operation_task_id = response['operation_task_id']
