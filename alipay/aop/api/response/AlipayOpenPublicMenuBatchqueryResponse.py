#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryMenu import QueryMenu


class AlipayOpenPublicMenuBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicMenuBatchqueryResponse, self).__init__()
        self._count = None
        self._menus = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def menus(self):
        return self._menus

    @menus.setter
    def menus(self, value):
        if isinstance(value, list):
            self._menus = list()
            for i in value:
                if isinstance(i, QueryMenu):
                    self._menus.append(i)
                else:
                    self._menus.append(QueryMenu.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicMenuBatchqueryResponse, self).parse_response_content(response_content)
        if 'count' in response:
            self.count = response['count']
        if 'menus' in response:
            self.menus = response['menus']
