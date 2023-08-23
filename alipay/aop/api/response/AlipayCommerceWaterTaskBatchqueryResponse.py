#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaskDetailListResponse import TaskDetailListResponse


class AlipayCommerceWaterTaskBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterTaskBatchqueryResponse, self).__init__()
        self._task_detail_list_response = None

    @property
    def task_detail_list_response(self):
        return self._task_detail_list_response

    @task_detail_list_response.setter
    def task_detail_list_response(self, value):
        if isinstance(value, list):
            self._task_detail_list_response = list()
            for i in value:
                if isinstance(i, TaskDetailListResponse):
                    self._task_detail_list_response.append(i)
                else:
                    self._task_detail_list_response.append(TaskDetailListResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterTaskBatchqueryResponse, self).parse_response_content(response_content)
        if 'task_detail_list_response' in response:
            self.task_detail_list_response = response['task_detail_list_response']
