#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArticleCategoryInfo import ArticleCategoryInfo


class AlipayIserviceCcmSwTreecategoryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwTreecategoryBatchqueryResponse, self).__init__()
        self._categories = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if isinstance(value, list):
            self._categories = list()
            for i in value:
                if isinstance(i, ArticleCategoryInfo):
                    self._categories.append(i)
                else:
                    self._categories.append(ArticleCategoryInfo.from_alipay_dict(i))
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
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwTreecategoryBatchqueryResponse, self).parse_response_content(response_content)
        if 'categories' in response:
            self.categories = response['categories']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
