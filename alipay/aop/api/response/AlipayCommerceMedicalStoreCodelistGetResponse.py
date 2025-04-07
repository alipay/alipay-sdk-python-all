#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalStoreCodelistGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStoreCodelistGetResponse, self).__init__()
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
                self._records.append(i)
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStoreCodelistGetResponse, self).parse_response_content(response_content)
        if 'records' in response:
            self.records = response['records']
        if 'total' in response:
            self.total = response['total']
