#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CategoryRootDTO import CategoryRootDTO


class AlipayMerchantShopcodeCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantShopcodeCategoryQueryResponse, self).__init__()
        self._categories = None

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if isinstance(value, list):
            self._categories = list()
            for i in value:
                if isinstance(i, CategoryRootDTO):
                    self._categories.append(i)
                else:
                    self._categories.append(CategoryRootDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantShopcodeCategoryQueryResponse, self).parse_response_content(response_content)
        if 'categories' in response:
            self.categories = response['categories']
