#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LocalCategoryAndParentVO import LocalCategoryAndParentVO


class AlipayOpenAppLocalitemAllcategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppLocalitemAllcategoryQueryResponse, self).__init__()
        self._cats = None

    @property
    def cats(self):
        return self._cats

    @cats.setter
    def cats(self, value):
        if isinstance(value, list):
            self._cats = list()
            for i in value:
                if isinstance(i, LocalCategoryAndParentVO):
                    self._cats.append(i)
                else:
                    self._cats.append(LocalCategoryAndParentVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppLocalitemAllcategoryQueryResponse, self).parse_response_content(response_content)
        if 'cats' in response:
            self.cats = response['cats']
