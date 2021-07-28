#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneTaskflowBatchFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneTaskflowBatchFinishResponse, self).__init__()
        self._task_flow_id_list = None

    @property
    def task_flow_id_list(self):
        return self._task_flow_id_list

    @task_flow_id_list.setter
    def task_flow_id_list(self, value):
        if isinstance(value, list):
            self._task_flow_id_list = list()
            for i in value:
                self._task_flow_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneTaskflowBatchFinishResponse, self).parse_response_content(response_content)
        if 'task_flow_id_list' in response:
            self.task_flow_id_list = response['task_flow_id_list']
