#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YunTaskWhiteUserDTO import YunTaskWhiteUserDTO


class AlipayCommerceYuntaskWhitehistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskWhitehistoryQueryResponse, self).__init__()
        self._page = None
        self._page_size = None
        self._total_size = None
        self._white_list = None

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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def white_list(self):
        return self._white_list

    @white_list.setter
    def white_list(self, value):
        if isinstance(value, list):
            self._white_list = list()
            for i in value:
                if isinstance(i, YunTaskWhiteUserDTO):
                    self._white_list.append(i)
                else:
                    self._white_list.append(YunTaskWhiteUserDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskWhitehistoryQueryResponse, self).parse_response_content(response_content)
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'white_list' in response:
            self.white_list = response['white_list']
