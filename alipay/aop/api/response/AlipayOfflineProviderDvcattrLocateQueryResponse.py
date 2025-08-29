#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DvcAttrForLocate import DvcAttrForLocate


class AlipayOfflineProviderDvcattrLocateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderDvcattrLocateQueryResponse, self).__init__()
        self._dvc_attr_for_locate = None
        self._page_index = None
        self._page_size = None
        self._total_count = None

    @property
    def dvc_attr_for_locate(self):
        return self._dvc_attr_for_locate

    @dvc_attr_for_locate.setter
    def dvc_attr_for_locate(self, value):
        if isinstance(value, list):
            self._dvc_attr_for_locate = list()
            for i in value:
                if isinstance(i, DvcAttrForLocate):
                    self._dvc_attr_for_locate.append(i)
                else:
                    self._dvc_attr_for_locate.append(DvcAttrForLocate.from_alipay_dict(i))
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderDvcattrLocateQueryResponse, self).parse_response_content(response_content)
        if 'dvc_attr_for_locate' in response:
            self.dvc_attr_for_locate = response['dvc_attr_for_locate']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
