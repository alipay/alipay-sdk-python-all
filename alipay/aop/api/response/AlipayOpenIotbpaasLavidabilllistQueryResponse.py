#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BillInfo import BillInfo


class AlipayOpenIotbpaasLavidabilllistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasLavidabilllistQueryResponse, self).__init__()
        self._bill_count = None
        self._bill_list = None

    @property
    def bill_count(self):
        return self._bill_count

    @bill_count.setter
    def bill_count(self, value):
        self._bill_count = value
    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, BillInfo):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(BillInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasLavidabilllistQueryResponse, self).parse_response_content(response_content)
        if 'bill_count' in response:
            self.bill_count = response['bill_count']
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
