#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationGamemarketingBenefitVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationGamemarketingBenefitVerifyResponse, self).__init__()
        self._voucher_verify_status = None

    @property
    def voucher_verify_status(self):
        return self._voucher_verify_status

    @voucher_verify_status.setter
    def voucher_verify_status(self, value):
        self._voucher_verify_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationGamemarketingBenefitVerifyResponse, self).parse_response_content(response_content)
        if 'voucher_verify_status' in response:
            self.voucher_verify_status = response['voucher_verify_status']
