#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DomainBind import DomainBind


class AlipayCloudCloudbaseHttpaccessBindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseHttpaccessBindQueryResponse, self).__init__()
        self._domain_binds = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def domain_binds(self):
        return self._domain_binds

    @domain_binds.setter
    def domain_binds(self, value):
        if isinstance(value, list):
            self._domain_binds = list()
            for i in value:
                if isinstance(i, DomainBind):
                    self._domain_binds.append(i)
                else:
                    self._domain_binds.append(DomainBind.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseHttpaccessBindQueryResponse, self).parse_response_content(response_content)
        if 'domain_binds' in response:
            self.domain_binds = response['domain_binds']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
