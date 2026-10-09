#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassAccountNameHashRecordDTO import PassAccountNameHashRecordDTO


class AnttechOceanbasePassaccountNamehashBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassaccountNamehashBatchqueryResponse, self).__init__()
        self._records = None
        self._total = None

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, PassAccountNameHashRecordDTO):
                    self._records.append(i)
                else:
                    self._records.append(PassAccountNameHashRecordDTO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassaccountNamehashBatchqueryResponse, self).parse_response_content(response_content)
        if 'records' in response:
            self.records = response['records']
        if 'total' in response:
            self.total = response['total']
