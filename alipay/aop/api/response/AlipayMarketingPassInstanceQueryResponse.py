#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassInstanceDetail import PassInstanceDetail


class AlipayMarketingPassInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPassInstanceQueryResponse, self).__init__()
        self._instance_list = None
        self._page_num = None
        self._page_size = None
        self._total = None
        self._total_page = None

    @property
    def instance_list(self):
        return self._instance_list

    @instance_list.setter
    def instance_list(self, value):
        if isinstance(value, list):
            self._instance_list = list()
            for i in value:
                if isinstance(i, PassInstanceDetail):
                    self._instance_list.append(i)
                else:
                    self._instance_list.append(PassInstanceDetail.from_alipay_dict(i))
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
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPassInstanceQueryResponse, self).parse_response_content(response_content)
        if 'instance_list' in response:
            self.instance_list = response['instance_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'total_page' in response:
            self.total_page = response['total_page']
