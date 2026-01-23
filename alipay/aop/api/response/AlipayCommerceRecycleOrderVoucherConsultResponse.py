#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleVoucherInfo import RecycleVoucherInfo


class AlipayCommerceRecycleOrderVoucherConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrderVoucherConsultResponse, self).__init__()
        self._voucher_info = None

    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, RecycleVoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = RecycleVoucherInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrderVoucherConsultResponse, self).parse_response_content(response_content)
        if 'voucher_info' in response:
            self.voucher_info = response['voucher_info']
