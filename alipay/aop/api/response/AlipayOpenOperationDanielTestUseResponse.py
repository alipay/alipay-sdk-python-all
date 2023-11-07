#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationDanielTestUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationDanielTestUseResponse, self).__init__()
        self._output_er = None

    @property
    def output_er(self):
        return self._output_er

    @output_er.setter
    def output_er(self, value):
        self._output_er = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationDanielTestUseResponse, self).parse_response_content(response_content)
        if 'output_er' in response:
            self.output_er = response['output_er']
