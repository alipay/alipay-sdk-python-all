#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NTaskSceneDetail import NTaskSceneDetail


class AlipayOpenSpNtaskSceneQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNtaskSceneQueryResponse, self).__init__()
        self._task_list = None

    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, NTaskSceneDetail):
                    self._task_list.append(i)
                else:
                    self._task_list.append(NTaskSceneDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNtaskSceneQueryResponse, self).parse_response_content(response_content)
        if 'task_list' in response:
            self.task_list = response['task_list']
