#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectBindConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectBindConsultResponse, self).__init__()
        self._handle_result = None

    @property
    def handle_result(self):
        return self._handle_result

    @handle_result.setter
    def handle_result(self, value):
        self._handle_result = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectBindConsultResponse, self).parse_response_content(response_content)
        if 'handle_result' in response:
            self.handle_result = response['handle_result']
