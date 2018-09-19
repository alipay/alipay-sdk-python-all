#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandAutomatApplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAutomatApplyModifyResponse, self).__init__()
        self._alipay_terminal_id = None

    @property
    def alipay_terminal_id(self):
        return self._alipay_terminal_id

    @alipay_terminal_id.setter
    def alipay_terminal_id(self, value):
        self._alipay_terminal_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAutomatApplyModifyResponse, self).parse_response_content(response_content)
        if 'alipay_terminal_id' in response:
            self.alipay_terminal_id = response['alipay_terminal_id']
