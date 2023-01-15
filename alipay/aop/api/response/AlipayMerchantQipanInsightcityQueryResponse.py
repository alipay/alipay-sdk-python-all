#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PortraitProvinceValue import PortraitProvinceValue


class AlipayMerchantQipanInsightcityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanInsightcityQueryResponse, self).__init__()
        self._coverage = None
        self._data_list = None
        self._portrait_desc = None
        self._portrait_key = None
        self._portrait_name = None
        self._report_date = None

    @property
    def coverage(self):
        return self._coverage

    @coverage.setter
    def coverage(self, value):
        self._coverage = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, PortraitProvinceValue):
                    self._data_list.append(i)
                else:
                    self._data_list.append(PortraitProvinceValue.from_alipay_dict(i))
    @property
    def portrait_desc(self):
        return self._portrait_desc

    @portrait_desc.setter
    def portrait_desc(self, value):
        self._portrait_desc = value
    @property
    def portrait_key(self):
        return self._portrait_key

    @portrait_key.setter
    def portrait_key(self, value):
        self._portrait_key = value
    @property
    def portrait_name(self):
        return self._portrait_name

    @portrait_name.setter
    def portrait_name(self, value):
        self._portrait_name = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanInsightcityQueryResponse, self).parse_response_content(response_content)
        if 'coverage' in response:
            self.coverage = response['coverage']
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'portrait_desc' in response:
            self.portrait_desc = response['portrait_desc']
        if 'portrait_key' in response:
            self.portrait_key = response['portrait_key']
        if 'portrait_name' in response:
            self.portrait_name = response['portrait_name']
        if 'report_date' in response:
            self.report_date = response['report_date']
