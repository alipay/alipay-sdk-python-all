#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentPayQueryBillListResponse import RentPayQueryBillListResponse


class AlipayEbppIndustryRentBillbatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentBillbatchQueryResponse, self).__init__()
        self._batch_list = None
        self._total_amount = None

    @property
    def batch_list(self):
        return self._batch_list

    @batch_list.setter
    def batch_list(self, value):
        if isinstance(value, list):
            self._batch_list = list()
            for i in value:
                if isinstance(i, RentPayQueryBillListResponse):
                    self._batch_list.append(i)
                else:
                    self._batch_list.append(RentPayQueryBillListResponse.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentBillbatchQueryResponse, self).parse_response_content(response_content)
        if 'batch_list' in response:
            self.batch_list = response['batch_list']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
