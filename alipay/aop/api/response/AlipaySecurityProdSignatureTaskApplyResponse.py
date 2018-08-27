#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignTaskResult import SignTaskResult


class AlipaySecurityProdSignatureTaskApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSignatureTaskApplyResponse, self).__init__()
        self._order_id = None
        self._task_list = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, SignTaskResult):
                    self._task_list.append(i)
                else:
                    self._task_list.append(SignTaskResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSignatureTaskApplyResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'task_list' in response:
            self.task_list = response['task_list']
