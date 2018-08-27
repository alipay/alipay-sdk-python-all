#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CPBillResultSet import CPBillResultSet


class AlipayEcoCplifeBillBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCplifeBillBatchqueryResponse, self).__init__()
        self._bill_result_set = None
        self._current_page_num = None
        self._total_bill_count = None

    @property
    def bill_result_set(self):
        return self._bill_result_set

    @bill_result_set.setter
    def bill_result_set(self, value):
        if isinstance(value, list):
            self._bill_result_set = list()
            for i in value:
                if isinstance(i, CPBillResultSet):
                    self._bill_result_set.append(i)
                else:
                    self._bill_result_set.append(CPBillResultSet.from_alipay_dict(i))
    @property
    def current_page_num(self):
        return self._current_page_num

    @current_page_num.setter
    def current_page_num(self, value):
        self._current_page_num = value
    @property
    def total_bill_count(self):
        return self._total_bill_count

    @total_bill_count.setter
    def total_bill_count(self, value):
        self._total_bill_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCplifeBillBatchqueryResponse, self).parse_response_content(response_content)
        if 'bill_result_set' in response:
            self.bill_result_set = response['bill_result_set']
        if 'current_page_num' in response:
            self.current_page_num = response['current_page_num']
        if 'total_bill_count' in response:
            self.total_bill_count = response['total_bill_count']
