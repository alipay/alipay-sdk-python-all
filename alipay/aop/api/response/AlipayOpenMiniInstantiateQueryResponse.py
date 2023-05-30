#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniInstantiateInfo import MiniInstantiateInfo


class AlipayOpenMiniInstantiateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInstantiateQueryResponse, self).__init__()
        self._instantiate_list = None
        self._page_no = None
        self._page_size = None
        self._total_items = None

    @property
    def instantiate_list(self):
        return self._instantiate_list

    @instantiate_list.setter
    def instantiate_list(self, value):
        if isinstance(value, list):
            self._instantiate_list = list()
            for i in value:
                if isinstance(i, MiniInstantiateInfo):
                    self._instantiate_list.append(i)
                else:
                    self._instantiate_list.append(MiniInstantiateInfo.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInstantiateQueryResponse, self).parse_response_content(response_content)
        if 'instantiate_list' in response:
            self.instantiate_list = response['instantiate_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_items' in response:
            self.total_items = response['total_items']
