#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FeeRecords import FeeRecords


class AlipayEcapiprodDrawndnFeerecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnFeerecordQueryResponse, self).__init__()
        self._fee_records = None
        self._request_id = None

    @property
    def fee_records(self):
        return self._fee_records

    @fee_records.setter
    def fee_records(self, value):
        if isinstance(value, list):
            self._fee_records = list()
            for i in value:
                if isinstance(i, FeeRecords):
                    self._fee_records.append(i)
                else:
                    self._fee_records.append(FeeRecords.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnFeerecordQueryResponse, self).parse_response_content(response_content)
        if 'fee_records' in response:
            self.fee_records = response['fee_records']
        if 'request_id' in response:
            self.request_id = response['request_id']
