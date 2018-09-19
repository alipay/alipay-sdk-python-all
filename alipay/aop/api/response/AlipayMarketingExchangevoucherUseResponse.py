#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingExchangevoucherUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingExchangevoucherUseResponse, self).__init__()
        self._voucher_id = None

    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingExchangevoucherUseResponse, self).parse_response_content(response_content)
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
