#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignTaskFileResult import SignTaskFileResult


class AlipaySecurityProdSignatureTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSignatureTaskQueryResponse, self).__init__()
        self._biz_id = None
        self._order_id = None
        self._status = None
        self._task_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_list(self):
        return self._task_list

    @task_list.setter
    def task_list(self, value):
        if isinstance(value, list):
            self._task_list = list()
            for i in value:
                if isinstance(i, SignTaskFileResult):
                    self._task_list.append(i)
                else:
                    self._task_list.append(SignTaskFileResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSignatureTaskQueryResponse, self).parse_response_content(response_content)
        if 'biz_id' in response:
            self.biz_id = response['biz_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'status' in response:
            self.status = response['status']
        if 'task_list' in response:
            self.task_list = response['task_list']
