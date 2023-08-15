#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Version import Version


class AlipayCloudCloudbaseFunctionVersionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseFunctionVersionQueryResponse, self).__init__()
        self._page_index = None
        self._page_size = None
        self._total = None
        self._versions = None

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
    @property
    def versions(self):
        return self._versions

    @versions.setter
    def versions(self, value):
        if isinstance(value, list):
            self._versions = list()
            for i in value:
                if isinstance(i, Version):
                    self._versions.append(i)
                else:
                    self._versions.append(Version.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseFunctionVersionQueryResponse, self).parse_response_content(response_content)
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'versions' in response:
            self.versions = response['versions']
