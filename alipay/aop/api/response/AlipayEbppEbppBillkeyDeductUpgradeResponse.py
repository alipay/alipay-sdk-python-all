#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppEbppBillkeyDeductUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppEbppBillkeyDeductUpgradeResponse, self).__init__()
        self._submit_res = None

    @property
    def submit_res(self):
        return self._submit_res

    @submit_res.setter
    def submit_res(self, value):
        self._submit_res = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppEbppBillkeyDeductUpgradeResponse, self).parse_response_content(response_content)
        if 'submit_res' in response:
            self.submit_res = response['submit_res']
