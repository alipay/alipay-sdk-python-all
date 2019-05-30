#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountFinriskMarkriskDatafactorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountFinriskMarkriskDatafactorQueryResponse, self).__init__()
        self._result_map = None

    @property
    def result_map(self):
        return self._result_map

    @result_map.setter
    def result_map(self, value):
        self._result_map = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountFinriskMarkriskDatafactorQueryResponse, self).parse_response_content(response_content)
        if 'result_map' in response:
            self.result_map = response['result_map']
