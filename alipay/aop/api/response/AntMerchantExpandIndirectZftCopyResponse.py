#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectZftCopyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftCopyResponse, self).__init__()
        self._smid_new = None

    @property
    def smid_new(self):
        return self._smid_new

    @smid_new.setter
    def smid_new(self, value):
        self._smid_new = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftCopyResponse, self).parse_response_content(response_content)
        if 'smid_new' in response:
            self.smid_new = response['smid_new']
