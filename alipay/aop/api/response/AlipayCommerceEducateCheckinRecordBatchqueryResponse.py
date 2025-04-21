#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduCheckInRecord import EduCheckInRecord


class AlipayCommerceEducateCheckinRecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCheckinRecordBatchqueryResponse, self).__init__()
        self._record_list = None
        self._total_num = None

    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, EduCheckInRecord):
                    self._record_list.append(i)
                else:
                    self._record_list.append(EduCheckInRecord.from_alipay_dict(i))
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCheckinRecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'record_list' in response:
            self.record_list = response['record_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
