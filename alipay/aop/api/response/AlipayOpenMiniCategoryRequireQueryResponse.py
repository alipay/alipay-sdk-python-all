#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CategoryRequireInfo import CategoryRequireInfo


class AlipayOpenMiniCategoryRequireQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniCategoryRequireQueryResponse, self).__init__()
        self._category_require_info_list = None

    @property
    def category_require_info_list(self):
        return self._category_require_info_list

    @category_require_info_list.setter
    def category_require_info_list(self, value):
        if isinstance(value, list):
            self._category_require_info_list = list()
            for i in value:
                if isinstance(i, CategoryRequireInfo):
                    self._category_require_info_list.append(i)
                else:
                    self._category_require_info_list.append(CategoryRequireInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniCategoryRequireQueryResponse, self).parse_response_content(response_content)
        if 'category_require_info_list' in response:
            self.category_require_info_list = response['category_require_info_list']
