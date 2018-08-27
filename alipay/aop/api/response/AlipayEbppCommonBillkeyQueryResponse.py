#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EbppBillKey import EbppBillKey


class AlipayEbppCommonBillkeyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommonBillkeyQueryResponse, self).__init__()
        self._bill_key_list = None

    @property
    def bill_key_list(self):
        return self._bill_key_list

    @bill_key_list.setter
    def bill_key_list(self, value):
        if isinstance(value, list):
            self._bill_key_list = list()
            for i in value:
                if isinstance(i, EbppBillKey):
                    self._bill_key_list.append(i)
                else:
                    self._bill_key_list.append(EbppBillKey.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommonBillkeyQueryResponse, self).parse_response_content(response_content)
        if 'bill_key_list' in response:
            self.bill_key_list = response['bill_key_list']
