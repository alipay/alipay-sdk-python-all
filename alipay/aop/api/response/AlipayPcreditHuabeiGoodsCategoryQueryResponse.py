#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GoodsCategoryResult import GoodsCategoryResult


class AlipayPcreditHuabeiGoodsCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiGoodsCategoryQueryResponse, self).__init__()
        self._categorys = None
        self._success = None

    @property
    def categorys(self):
        return self._categorys

    @categorys.setter
    def categorys(self, value):
        if isinstance(value, list):
            self._categorys = list()
            for i in value:
                if isinstance(i, GoodsCategoryResult):
                    self._categorys.append(i)
                else:
                    self._categorys.append(GoodsCategoryResult.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiGoodsCategoryQueryResponse, self).parse_response_content(response_content)
        if 'categorys' in response:
            self.categorys = response['categorys']
        if 'success' in response:
            self.success = response['success']
