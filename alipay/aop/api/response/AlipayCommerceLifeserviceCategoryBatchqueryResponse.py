#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AxfItemCategoryVO import AxfItemCategoryVO


class AlipayCommerceLifeserviceCategoryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceCategoryBatchqueryResponse, self).__init__()
        self._category_info = None

    @property
    def category_info(self):
        return self._category_info

    @category_info.setter
    def category_info(self, value):
        if isinstance(value, list):
            self._category_info = list()
            for i in value:
                if isinstance(i, AxfItemCategoryVO):
                    self._category_info.append(i)
                else:
                    self._category_info.append(AxfItemCategoryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceCategoryBatchqueryResponse, self).parse_response_content(response_content)
        if 'category_info' in response:
            self.category_info = response['category_info']
