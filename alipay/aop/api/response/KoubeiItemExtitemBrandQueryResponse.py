#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtBrand import ExtBrand


class KoubeiItemExtitemBrandQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemExtitemBrandQueryResponse, self).__init__()
        self._brand_list = None

    @property
    def brand_list(self):
        return self._brand_list

    @brand_list.setter
    def brand_list(self, value):
        if isinstance(value, list):
            self._brand_list = list()
            for i in value:
                if isinstance(i, ExtBrand):
                    self._brand_list.append(i)
                else:
                    self._brand_list.append(ExtBrand.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiItemExtitemBrandQueryResponse, self).parse_response_content(response_content)
        if 'brand_list' in response:
            self.brand_list = response['brand_list']
