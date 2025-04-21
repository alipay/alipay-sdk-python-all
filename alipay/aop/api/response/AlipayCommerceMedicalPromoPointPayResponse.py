#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPromoPointPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPromoPointPayResponse, self).__init__()
        self._res_code = None
        self._res_flag = None
        self._res_msg = None

    @property
    def res_code(self):
        return self._res_code

    @res_code.setter
    def res_code(self, value):
        self._res_code = value
    @property
    def res_flag(self):
        return self._res_flag

    @res_flag.setter
    def res_flag(self, value):
        self._res_flag = value
    @property
    def res_msg(self):
        return self._res_msg

    @res_msg.setter
    def res_msg(self, value):
        self._res_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPromoPointPayResponse, self).parse_response_content(response_content)
        if 'res_code' in response:
            self.res_code = response['res_code']
        if 'res_flag' in response:
            self.res_flag = response['res_flag']
        if 'res_msg' in response:
            self.res_msg = response['res_msg']
