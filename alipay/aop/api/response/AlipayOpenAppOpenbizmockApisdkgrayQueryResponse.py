#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppOpenbizmockApisdkgrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppOpenbizmockApisdkgrayQueryResponse, self).__init__()
        self._output_param = None

    @property
    def output_param(self):
        return self._output_param

    @output_param.setter
    def output_param(self, value):
        self._output_param = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppOpenbizmockApisdkgrayQueryResponse, self).parse_response_content(response_content)
        if 'output_param' in response:
            self.output_param = response['output_param']
