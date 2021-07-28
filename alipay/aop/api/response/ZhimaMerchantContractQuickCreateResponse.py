#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantContractQuickCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractQuickCreateResponse, self).__init__()
        self._biz_code = None
        self._biz_desc = None
        self._offer_no = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_desc(self):
        return self._biz_desc

    @biz_desc.setter
    def biz_desc(self, value):
        self._biz_desc = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractQuickCreateResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_desc' in response:
            self.biz_desc = response['biz_desc']
        if 'offer_no' in response:
            self.offer_no = response['offer_no']
