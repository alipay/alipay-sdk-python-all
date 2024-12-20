#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantPaymrchdataQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantPaymrchdataQrcodeCreateResponse, self).__init__()
        self._open_result = None
        self._qrcode_business_apply_no = None

    @property
    def open_result(self):
        return self._open_result

    @open_result.setter
    def open_result(self, value):
        self._open_result = value
    @property
    def qrcode_business_apply_no(self):
        return self._qrcode_business_apply_no

    @qrcode_business_apply_no.setter
    def qrcode_business_apply_no(self, value):
        self._qrcode_business_apply_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantPaymrchdataQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'open_result' in response:
            self.open_result = response['open_result']
        if 'qrcode_business_apply_no' in response:
            self.qrcode_business_apply_no = response['qrcode_business_apply_no']
