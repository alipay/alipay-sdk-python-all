#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SportsToolRecord import SportsToolRecord


class AlipayCommerceEducateSmartcampusSportsrecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSmartcampusSportsrecordBatchqueryResponse, self).__init__()
        self._has_more = None
        self._sports_record_list = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def sports_record_list(self):
        return self._sports_record_list

    @sports_record_list.setter
    def sports_record_list(self, value):
        if isinstance(value, list):
            self._sports_record_list = list()
            for i in value:
                if isinstance(i, SportsToolRecord):
                    self._sports_record_list.append(i)
                else:
                    self._sports_record_list.append(SportsToolRecord.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSmartcampusSportsrecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'sports_record_list' in response:
            self.sports_record_list = response['sports_record_list']
