#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskInstanceInfoDTO import TaskInstanceInfoDTO


class AlipayCommerceCommonTaskinstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCommonTaskinstanceQueryResponse, self).__init__()
        self._task_instance_info = None

    @property
    def task_instance_info(self):
        return self._task_instance_info

    @task_instance_info.setter
    def task_instance_info(self, value):
        if isinstance(value, TaskInstanceInfoDTO):
            self._task_instance_info = value
        else:
            self._task_instance_info = TaskInstanceInfoDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCommonTaskinstanceQueryResponse, self).parse_response_content(response_content)
        if 'task_instance_info' in response:
            self.task_instance_info = response['task_instance_info']
