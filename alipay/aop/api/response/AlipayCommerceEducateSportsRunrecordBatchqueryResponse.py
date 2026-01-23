#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SportsRunRecord import SportsRunRecord


class AlipayCommerceEducateSportsRunrecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSportsRunrecordBatchqueryResponse, self).__init__()
        self._run_record_list = None
        self._total_num = None

    @property
    def run_record_list(self):
        return self._run_record_list

    @run_record_list.setter
    def run_record_list(self, value):
        if isinstance(value, list):
            self._run_record_list = list()
            for i in value:
                if isinstance(i, SportsRunRecord):
                    self._run_record_list.append(i)
                else:
                    self._run_record_list.append(SportsRunRecord.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSportsRunrecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'run_record_list' in response:
            self.run_record_list = response['run_record_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
