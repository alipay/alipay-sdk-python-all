#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PucInstCode import PucInstCode


class AlipayEbppJfInstcodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfInstcodeQueryResponse, self).__init__()
        self._inst_code_list = None

    @property
    def inst_code_list(self):
        return self._inst_code_list

    @inst_code_list.setter
    def inst_code_list(self, value):
        if isinstance(value, list):
            self._inst_code_list = list()
            for i in value:
                if isinstance(i, PucInstCode):
                    self._inst_code_list.append(i)
                else:
                    self._inst_code_list.append(PucInstCode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfInstcodeQueryResponse, self).parse_response_content(response_content)
        if 'inst_code_list' in response:
            self.inst_code_list = response['inst_code_list']
