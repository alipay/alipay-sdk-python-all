#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TrustBillOrder import TrustBillOrder


class AnttechBlockchainFinanceTvpBillBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpBillBatchqueryResponse, self).__init__()
        self._bill_list = None
        self._total_count = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, TrustBillOrder):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(TrustBillOrder.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpBillBatchqueryResponse, self).parse_response_content(response_content)
        if 'bill_list' in response:
            self.bill_list = response['bill_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
