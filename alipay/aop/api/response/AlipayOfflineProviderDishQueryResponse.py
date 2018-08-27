#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvShopDishModel import IsvShopDishModel


class AlipayOfflineProviderDishQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderDishQueryResponse, self).__init__()
        self._items = None
        self._list = None
        self._page = None
        self._page_size = None
        self._pages = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    @property
    def list(self):
        return self._list

    @list.setter
    def list(self, value):
        if isinstance(value, list):
            self._list = list()
            for i in value:
                if isinstance(i, IsvShopDishModel):
                    self._list.append(i)
                else:
                    self._list.append(IsvShopDishModel.from_alipay_dict(i))
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderDishQueryResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
        if 'list' in response:
            self.list = response['list']
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'pages' in response:
            self.pages = response['pages']
