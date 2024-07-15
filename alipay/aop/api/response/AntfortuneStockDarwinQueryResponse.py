#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DarwinParameter import DarwinParameter


class AntfortuneStockDarwinQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockDarwinQueryResponse, self).__init__()
        self._darwin_parameter = None
        self._exp_id = None

    @property
    def darwin_parameter(self):
        return self._darwin_parameter

    @darwin_parameter.setter
    def darwin_parameter(self, value):
        if isinstance(value, list):
            self._darwin_parameter = list()
            for i in value:
                if isinstance(i, DarwinParameter):
                    self._darwin_parameter.append(i)
                else:
                    self._darwin_parameter.append(DarwinParameter.from_alipay_dict(i))
    @property
    def exp_id(self):
        return self._exp_id

    @exp_id.setter
    def exp_id(self, value):
        self._exp_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockDarwinQueryResponse, self).parse_response_content(response_content)
        if 'darwin_parameter' in response:
            self.darwin_parameter = response['darwin_parameter']
        if 'exp_id' in response:
            self.exp_id = response['exp_id']
