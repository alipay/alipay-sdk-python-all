#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneProductInquiryApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneProductInquiryApplyResponse, self).__init__()
        self._premium = None

    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneProductInquiryApplyResponse, self).parse_response_content(response_content)
        if 'premium' in response:
            self.premium = response['premium']
