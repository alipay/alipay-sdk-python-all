#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountRecord import AccountRecord


class AlipayUserAccountSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountSearchResponse, self).__init__()
        self._account_records = None
        self._total_pages = None
        self._total_results = None

    @property
    def account_records(self):
        return self._account_records

    @account_records.setter
    def account_records(self, value):
        if isinstance(value, list):
            self._account_records = list()
            for i in value:
                if isinstance(i, AccountRecord):
                    self._account_records.append(i)
                else:
                    self._account_records.append(AccountRecord.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountSearchResponse, self).parse_response_content(response_content)
        if 'account_records' in response:
            self.account_records = response['account_records']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_results' in response:
            self.total_results = response['total_results']
