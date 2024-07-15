#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LmCategoryVO import LmCategoryVO


class AlipayCloudCloudpromoMallCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallCategoryQueryResponse, self).__init__()
        self._categories = None

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if isinstance(value, list):
            self._categories = list()
            for i in value:
                if isinstance(i, LmCategoryVO):
                    self._categories.append(i)
                else:
                    self._categories.append(LmCategoryVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallCategoryQueryResponse, self).parse_response_content(response_content)
        if 'categories' in response:
            self.categories = response['categories']
