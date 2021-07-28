#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HbMerchantBill import HbMerchantBill


class AlipayPcreditHuabeiMerchantBillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiMerchantBillQueryResponse, self).__init__()
        self._bill_list = None
        self._size = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, HbMerchantBill):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(HbMerchantBill.from_alipay_dict(i))
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiMerchantBillQueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'size' in response:
            self.size = response['size']
