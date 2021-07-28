#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsSceneTaskFlowDTO import InsSceneTaskFlowDTO


class AlipayInsSceneTaskflowBatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneTaskflowBatchQueryResponse, self).__init__()
        self._task_flow_list = None

    @property
    def task_flow_list(self):
        return self._task_flow_list

    @task_flow_list.setter
    def task_flow_list(self, value):
        if isinstance(value, list):
            self._task_flow_list = list()
            for i in value:
                if isinstance(i, InsSceneTaskFlowDTO):
                    self._task_flow_list.append(i)
                else:
                    self._task_flow_list.append(InsSceneTaskFlowDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneTaskflowBatchQueryResponse, self).parse_response_content(response_content)
        if 'task_flow_list' in response:
            self.task_flow_list = response['task_flow_list']
