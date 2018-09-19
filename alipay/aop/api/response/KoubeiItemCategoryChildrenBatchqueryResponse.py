#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StandardCategoryInfo import StandardCategoryInfo


class KoubeiItemCategoryChildrenBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemCategoryChildrenBatchqueryResponse, self).__init__()
        self._category_list = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, StandardCategoryInfo):
                    self._category_list.append(i)
                else:
                    self._category_list.append(StandardCategoryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiItemCategoryChildrenBatchqueryResponse, self).parse_response_content(response_content)
        if 'category_list' in response:
            self.category_list = response['category_list']
