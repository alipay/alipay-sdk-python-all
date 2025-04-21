#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BusinessBillGoodsQueryPageVO import BusinessBillGoodsQueryPageVO


class AlipayMarketingBusinessbillGoodsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBusinessbillGoodsQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._result_list = None
        self._total_pages = None
        self._total_size = None

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
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, BusinessBillGoodsQueryPageVO):
                    self._result_list.append(i)
                else:
                    self._result_list.append(BusinessBillGoodsQueryPageVO.from_alipay_dict(i))
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBusinessbillGoodsQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'result_list' in response:
            self.result_list = response['result_list']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
