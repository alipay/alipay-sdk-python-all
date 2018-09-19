#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PassTemplateDetail import PassTemplateDetail


class AlipayMarketingPassTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPassTemplateQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._total = None
        self._total_page = None
        self._tpl_list = None

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
    @property
    def tpl_list(self):
        return self._tpl_list

    @tpl_list.setter
    def tpl_list(self, value):
        if isinstance(value, list):
            self._tpl_list = list()
            for i in value:
                if isinstance(i, PassTemplateDetail):
                    self._tpl_list.append(i)
                else:
                    self._tpl_list.append(PassTemplateDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPassTemplateQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
        if 'total_page' in response:
            self.total_page = response['total_page']
        if 'tpl_list' in response:
            self.tpl_list = response['tpl_list']
