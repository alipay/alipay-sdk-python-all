#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenVoucherDTO import OpenVoucherDTO


class AlipayMarketingVoucherExchangevoucherRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherExchangevoucherRefundResponse, self).__init__()
        self._voucher = None

    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, OpenVoucherDTO):
            self._voucher = value
        else:
            self._voucher = OpenVoucherDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherExchangevoucherRefundResponse, self).parse_response_content(response_content)
        if 'voucher' in response:
            self.voucher = response['voucher']
