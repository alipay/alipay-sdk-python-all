#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenApidefaultparamQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenApidefaultparamQueryResponse, self).__init__()
        self._param = None

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenApidefaultparamQueryResponse, self).parse_response_content(response_content)
        if 'param' in response:
            self.param = response['param']
