#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskReceiveInfo import TaskReceiveInfo


class AlipayCommerceOperationPromoterTaskReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterTaskReceiveResponse, self).__init__()
        self._task_receive_result = None

    @property
    def task_receive_result(self):
        return self._task_receive_result

    @task_receive_result.setter
    def task_receive_result(self, value):
        if isinstance(value, TaskReceiveInfo):
            self._task_receive_result = value
        else:
            self._task_receive_result = TaskReceiveInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterTaskReceiveResponse, self).parse_response_content(response_content)
        if 'task_receive_result' in response:
            self.task_receive_result = response['task_receive_result']
