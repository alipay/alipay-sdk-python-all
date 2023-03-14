#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntlcNdaProtocolSignRecordExtDO import AntlcNdaProtocolSignRecordExtDO


class AlipayBossProdAntlegalchainNdalistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlegalchainNdalistQueryResponse, self).__init__()
        self._items_per_page = None
        self._page = None
        self._page_list = None
        self._total_items = None
        self._total_pages = None

    @property
    def items_per_page(self):
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, value):
        self._items_per_page = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_list(self):
        return self._page_list

    @page_list.setter
    def page_list(self, value):
        if isinstance(value, list):
            self._page_list = list()
            for i in value:
                if isinstance(i, AntlcNdaProtocolSignRecordExtDO):
                    self._page_list.append(i)
                else:
                    self._page_list.append(AntlcNdaProtocolSignRecordExtDO.from_alipay_dict(i))
    @property
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlegalchainNdalistQueryResponse, self).parse_response_content(response_content)
        if 'items_per_page' in response:
            self.items_per_page = response['items_per_page']
        if 'page' in response:
            self.page = response['page']
        if 'page_list' in response:
            self.page_list = response['page_list']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
