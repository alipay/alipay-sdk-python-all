#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LivestreamOrder import LivestreamOrder


class AlipayCommerceLivestreamOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLivestreamOrderQueryResponse, self).__init__()
        self._contents = None
        self._page = None
        self._page_size = None
        self._total_count = None

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, list):
            self._contents = list()
            for i in value:
                if isinstance(i, LivestreamOrder):
                    self._contents.append(i)
                else:
                    self._contents.append(LivestreamOrder.from_alipay_dict(i))
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLivestreamOrderQueryResponse, self).parse_response_content(response_content)
        if 'contents' in response:
            self.contents = response['contents']
        if 'page' in response:
            self.page = response['page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
