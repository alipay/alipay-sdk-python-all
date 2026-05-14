#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailTaskSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailTaskSaveResponse, self).__init__()
        self._operate_type = None
        self._response_list = None
        self._task_action = None

    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def response_list(self):
        return self._response_list

    @response_list.setter
    def response_list(self, value):
        self._response_list = value
    @property
    def task_action(self):
        return self._task_action

    @task_action.setter
    def task_action(self, value):
        self._task_action = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailTaskSaveResponse, self).parse_response_content(response_content)
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'response_list' in response:
            self.response_list = response['response_list']
        if 'task_action' in response:
            self.task_action = response['task_action']
