#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppMerchantExternalbillCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppMerchantExternalbillCreateResponse, self).__init__()
        self._alipay_bill_id = None

    @property
    def alipay_bill_id(self):
        return self._alipay_bill_id

    @alipay_bill_id.setter
    def alipay_bill_id(self, value):
        self._alipay_bill_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppMerchantExternalbillCreateResponse, self).parse_response_content(response_content)
        if 'alipay_bill_id' in response:
            self.alipay_bill_id = response['alipay_bill_id']
