#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipaySolutionRecord import AlipaySolutionRecord


class AlipayMerchantSolutionRecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolutionRecordQueryResponse, self).__init__()
        self._record_data = None
        self._record_status_code = None
        self._record_status_desc = None
        self._solution_code = None

    @property
    def record_data(self):
        return self._record_data

    @record_data.setter
    def record_data(self, value):
        if isinstance(value, list):
            self._record_data = list()
            for i in value:
                if isinstance(i, AlipaySolutionRecord):
                    self._record_data.append(i)
                else:
                    self._record_data.append(AlipaySolutionRecord.from_alipay_dict(i))
    @property
    def record_status_code(self):
        return self._record_status_code

    @record_status_code.setter
    def record_status_code(self, value):
        self._record_status_code = value
    @property
    def record_status_desc(self):
        return self._record_status_desc

    @record_status_desc.setter
    def record_status_desc(self, value):
        self._record_status_desc = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolutionRecordQueryResponse, self).parse_response_content(response_content)
        if 'record_data' in response:
            self.record_data = response['record_data']
        if 'record_status_code' in response:
            self.record_status_code = response['record_status_code']
        if 'record_status_desc' in response:
            self.record_status_desc = response['record_status_desc']
        if 'solution_code' in response:
            self.solution_code = response['solution_code']
