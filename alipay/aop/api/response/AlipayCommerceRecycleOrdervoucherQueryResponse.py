#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleOrderVoucher import RecycleOrderVoucher


class AlipayCommerceRecycleOrdervoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleOrdervoucherQueryResponse, self).__init__()
        self._voucher_list = None

    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, RecycleOrderVoucher):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(RecycleOrderVoucher.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleOrdervoucherQueryResponse, self).parse_response_content(response_content)
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
