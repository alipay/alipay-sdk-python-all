#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LendingRecords import LendingRecords


class AlipayEcapiprodDrawndnLendingrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnLendingrecordQueryResponse, self).__init__()
        self._lending_records = None
        self._request_id = None

    @property
    def lending_records(self):
        return self._lending_records

    @lending_records.setter
    def lending_records(self, value):
        if isinstance(value, list):
            self._lending_records = list()
            for i in value:
                if isinstance(i, LendingRecords):
                    self._lending_records.append(i)
                else:
                    self._lending_records.append(LendingRecords.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnLendingrecordQueryResponse, self).parse_response_content(response_content)
        if 'lending_records' in response:
            self.lending_records = response['lending_records']
        if 'request_id' in response:
            self.request_id = response['request_id']
