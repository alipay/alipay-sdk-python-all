#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CustomsDeclareRecordInfo import CustomsDeclareRecordInfo


class AlipayTradeCustomsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeCustomsQueryResponse, self).__init__()
        self._not_found = None
        self._records = None

    @property
    def not_found(self):
        return self._not_found

    @not_found.setter
    def not_found(self, value):
        self._not_found = value
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, CustomsDeclareRecordInfo):
                    self._records.append(i)
                else:
                    self._records.append(CustomsDeclareRecordInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeCustomsQueryResponse, self).parse_response_content(response_content)
        if 'not_found' in response:
            self.not_found = response['not_found']
        if 'records' in response:
            self.records = response['records']
