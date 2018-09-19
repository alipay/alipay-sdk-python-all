#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherLiteInfo import VoucherLiteInfo


class AlipayMarketingVoucherListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingVoucherListQueryResponse, self).__init__()
        self._vouchers = None

    @property
    def vouchers(self):
        return self._vouchers

    @vouchers.setter
    def vouchers(self, value):
        if isinstance(value, list):
            self._vouchers = list()
            for i in value:
                if isinstance(i, VoucherLiteInfo):
                    self._vouchers.append(i)
                else:
                    self._vouchers.append(VoucherLiteInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingVoucherListQueryResponse, self).parse_response_content(response_content)
        if 'vouchers' in response:
            self.vouchers = response['vouchers']
