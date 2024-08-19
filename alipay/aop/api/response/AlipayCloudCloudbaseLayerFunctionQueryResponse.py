#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FunctionInfo import FunctionInfo


class AlipayCloudCloudbaseLayerFunctionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseLayerFunctionQueryResponse, self).__init__()
        self._functions = None

    @property
    def functions(self):
        return self._functions

    @functions.setter
    def functions(self, value):
        if isinstance(value, list):
            self._functions = list()
            for i in value:
                if isinstance(i, FunctionInfo):
                    self._functions.append(i)
                else:
                    self._functions.append(FunctionInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseLayerFunctionQueryResponse, self).parse_response_content(response_content)
        if 'functions' in response:
            self.functions = response['functions']
