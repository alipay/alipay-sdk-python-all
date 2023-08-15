#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StaticDomain import StaticDomain


class AlipayCloudCloudrunStaticsiteDomainBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudrunStaticsiteDomainBatchqueryResponse, self).__init__()
        self._domain_list = None
        self._next_token = None
        self._page_size = None

    @property
    def domain_list(self):
        return self._domain_list

    @domain_list.setter
    def domain_list(self, value):
        if isinstance(value, list):
            self._domain_list = list()
            for i in value:
                if isinstance(i, StaticDomain):
                    self._domain_list.append(i)
                else:
                    self._domain_list.append(StaticDomain.from_alipay_dict(i))
    @property
    def next_token(self):
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudrunStaticsiteDomainBatchqueryResponse, self).parse_response_content(response_content)
        if 'domain_list' in response:
            self.domain_list = response['domain_list']
        if 'next_token' in response:
            self.next_token = response['next_token']
        if 'page_size' in response:
            self.page_size = response['page_size']
