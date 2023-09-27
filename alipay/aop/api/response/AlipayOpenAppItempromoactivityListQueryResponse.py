#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoActivityItemPageVO import PromoActivityItemPageVO


class AlipayOpenAppItempromoactivityListQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItempromoactivityListQueryResponse, self).__init__()
        self._data = None
        self._page_num = None
        self._page_size = None
        self._promotion_type = None
        self._title = None
        self._total_number = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, PromoActivityItemPageVO):
                    self._data.append(i)
                else:
                    self._data.append(PromoActivityItemPageVO.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItempromoactivityListQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'promotion_type' in response:
            self.promotion_type = response['promotion_type']
        if 'title' in response:
            self.title = response['title']
        if 'total_number' in response:
            self.total_number = response['total_number']
