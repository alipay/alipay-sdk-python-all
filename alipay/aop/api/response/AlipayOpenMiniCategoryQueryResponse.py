#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppCategory import MiniAppCategory
from alipay.aop.api.domain.MiniAppCategory import MiniAppCategory


class AlipayOpenMiniCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCategoryQueryResponse, self).__init__()
        self._category_list = None
        self._mini_category_list = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, MiniAppCategory):
                    self._category_list.append(i)
                else:
                    self._category_list.append(MiniAppCategory.from_alipay_dict(i))
    @property
    def mini_category_list(self):
        return self._mini_category_list

    @mini_category_list.setter
    def mini_category_list(self, value):
        if isinstance(value, list):
            self._mini_category_list = list()
            for i in value:
                if isinstance(i, MiniAppCategory):
                    self._mini_category_list.append(i)
                else:
                    self._mini_category_list.append(MiniAppCategory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCategoryQueryResponse, self).parse_response_content(response_content)
        if 'category_list' in response:
            self.category_list = response['category_list']
        if 'mini_category_list' in response:
            self.mini_category_list = response['mini_category_list']
