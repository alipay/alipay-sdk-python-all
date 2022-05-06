#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankMarketingMcaplatformContractQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankMarketingMcaplatformContractQueryResponse, self).__init__()
        self._sign_status = None

    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value

    def parse_response_content(self, response_content):
        response = super(MybankMarketingMcaplatformContractQueryResponse, self).parse_response_content(response_content)
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
