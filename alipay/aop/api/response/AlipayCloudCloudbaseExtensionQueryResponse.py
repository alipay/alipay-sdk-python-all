#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Extension import Extension


class AlipayCloudCloudbaseExtensionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseExtensionQueryResponse, self).__init__()
        self._extensions = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, value):
        if isinstance(value, list):
            self._extensions = list()
            for i in value:
                if isinstance(i, Extension):
                    self._extensions.append(i)
                else:
                    self._extensions.append(Extension.from_alipay_dict(i))
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
        response = super(AlipayCloudCloudbaseExtensionQueryResponse, self).parse_response_content(response_content)
        if 'extensions' in response:
            self.extensions = response['extensions']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
