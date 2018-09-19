#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransThirdpartyRewardCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransThirdpartyRewardCreateResponse, self).__init__()
        self._transfer_no = None

    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransThirdpartyRewardCreateResponse, self).parse_response_content(response_content)
        if 'transfer_no' in response:
            self.transfer_no = response['transfer_no']
