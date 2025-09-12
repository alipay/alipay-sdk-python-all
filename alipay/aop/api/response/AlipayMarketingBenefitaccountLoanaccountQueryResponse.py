#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanAccountQueryDetailDTO import LoanAccountQueryDetailDTO


class AlipayMarketingBenefitaccountLoanaccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountLoanaccountQueryResponse, self).__init__()
        self._data_list = None
        self._next_end_time = None
        self._next_order_no = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, LoanAccountQueryDetailDTO):
                    self._data_list.append(i)
                else:
                    self._data_list.append(LoanAccountQueryDetailDTO.from_alipay_dict(i))
    @property
    def next_end_time(self):
        return self._next_end_time

    @next_end_time.setter
    def next_end_time(self, value):
        self._next_end_time = value
    @property
    def next_order_no(self):
        return self._next_order_no

    @next_order_no.setter
    def next_order_no(self, value):
        self._next_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountLoanaccountQueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'next_end_time' in response:
            self.next_end_time = response['next_end_time']
        if 'next_order_no' in response:
            self.next_order_no = response['next_order_no']
