#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportAdStocktaskCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdStocktaskCreateResponse, self).__init__()
        self._task_id = None

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdStocktaskCreateResponse, self).parse_response_content(response_content)
        if 'task_id' in response:
            self.task_id = response['task_id']
