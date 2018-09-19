#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Category import Category
from alipay.aop.api.domain.Category import Category


class KoubeiMarketingDataShopCategoryGetResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataShopCategoryGetResponse, self).__init__()
        self._category_list = None
        self._other = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, Category):
                    self._category_list.append(i)
                else:
                    self._category_list.append(Category.from_alipay_dict(i))
    @property
    def other(self):
        return self._other

    @other.setter
    def other(self, value):
        if isinstance(value, Category):
            self._other = value
        else:
            self._other = Category.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataShopCategoryGetResponse, self).parse_response_content(response_content)
        if 'category_list' in response:
            self.category_list = response['category_list']
        if 'other' in response:
            self.other = response['other']
