#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CategoryAndParentVO import CategoryAndParentVO


class AlipayOpenAppItemAllcategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemAllcategoryQueryResponse, self).__init__()
        self._cats = None

    @property
    def cats(self):
        return self._cats

    @cats.setter
    def cats(self, value):
        if isinstance(value, list):
            self._cats = list()
            for i in value:
                if isinstance(i, CategoryAndParentVO):
                    self._cats.append(i)
                else:
                    self._cats.append(CategoryAndParentVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemAllcategoryQueryResponse, self).parse_response_content(response_content)
        if 'cats' in response:
            self.cats = response['cats']
