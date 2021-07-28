#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FrontCategoryInfo import FrontCategoryInfo


class AntMerchantExpandFrontcategorySecurityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandFrontcategorySecurityQueryResponse, self).__init__()
        self._front_category_list = None

    @property
    def front_category_list(self):
        return self._front_category_list

    @front_category_list.setter
    def front_category_list(self, value):
        if isinstance(value, list):
            self._front_category_list = list()
            for i in value:
                if isinstance(i, FrontCategoryInfo):
                    self._front_category_list.append(i)
                else:
                    self._front_category_list.append(FrontCategoryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandFrontcategorySecurityQueryResponse, self).parse_response_content(response_content)
        if 'front_category_list' in response:
            self.front_category_list = response['front_category_list']
