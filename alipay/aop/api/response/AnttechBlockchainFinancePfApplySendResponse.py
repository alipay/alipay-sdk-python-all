#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinancePfApplySendResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinancePfApplySendResponse, self).__init__()
        self._financing_id = None
        self._msg = None
        self._platform_id = None

    @property
    def financing_id(self):
        return self._financing_id

    @financing_id.setter
    def financing_id(self, value):
        self._financing_id = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinancePfApplySendResponse, self).parse_response_content(response_content)
        if 'financing_id' in response:
            self.financing_id = response['financing_id']
        if 'msg' in response:
            self.msg = response['msg']
        if 'platform_id' in response:
            self.platform_id = response['platform_id']
