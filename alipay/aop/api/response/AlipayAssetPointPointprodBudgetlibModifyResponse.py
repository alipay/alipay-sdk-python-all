#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointPointprodBudgetlibModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointPointprodBudgetlibModifyResponse, self).__init__()
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointPointprodBudgetlibModifyResponse, self).parse_response_content(response_content)
        if 'message' in response:
            self.message = response['message']
