#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Category import Category
from alipay.aop.api.domain.SpiOutputObject import SpiOutputObject


class KoubeiMarketingTessssssssssstQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingTessssssssssstQueryResponse, self).__init__()
        self._a = None
        self._category = None
        self._output = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, Category):
            self._category = value
        else:
            self._category = Category.from_alipay_dict(value)
    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        if isinstance(value, SpiOutputObject):
            self._output = value
        else:
            self._output = SpiOutputObject.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingTessssssssssstQueryResponse, self).parse_response_content(response_content)
        if 'a' in response:
            self.a = response['a']
        if 'category' in response:
            self.category = response['category']
        if 'output' in response:
            self.output = response['output']
