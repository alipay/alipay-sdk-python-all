#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CategoryVO import CategoryVO
from alipay.aop.api.domain.CategoryVO import CategoryVO


class KoubeiRetailWmsCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailWmsCategoryQueryResponse, self).__init__()
        self._category = None
        self._sub_categories = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, CategoryVO):
            self._category = value
        else:
            self._category = CategoryVO.from_alipay_dict(value)
    @property
    def sub_categories(self):
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, value):
        if isinstance(value, list):
            self._sub_categories = list()
            for i in value:
                if isinstance(i, CategoryVO):
                    self._sub_categories.append(i)
                else:
                    self._sub_categories.append(CategoryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailWmsCategoryQueryResponse, self).parse_response_content(response_content)
        if 'category' in response:
            self.category = response['category']
        if 'sub_categories' in response:
            self.sub_categories = response['sub_categories']
