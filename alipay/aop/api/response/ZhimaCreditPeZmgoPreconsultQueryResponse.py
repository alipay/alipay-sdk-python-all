#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoPreconsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoPreconsultQueryResponse, self).__init__()
        self._admittance = None

    @property
    def admittance(self):
        return self._admittance

    @admittance.setter
    def admittance(self, value):
        self._admittance = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoPreconsultQueryResponse, self).parse_response_content(response_content)
        if 'admittance' in response:
            self.admittance = response['admittance']
