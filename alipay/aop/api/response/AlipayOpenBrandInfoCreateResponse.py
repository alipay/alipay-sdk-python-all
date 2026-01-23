#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BrandFailResponse import BrandFailResponse


class AlipayOpenBrandInfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenBrandInfoCreateResponse, self).__init__()
        self._brand_id = None
        self._fail_reasons = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, list):
            self._fail_reasons = list()
            for i in value:
                if isinstance(i, BrandFailResponse):
                    self._fail_reasons.append(i)
                else:
                    self._fail_reasons.append(BrandFailResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenBrandInfoCreateResponse, self).parse_response_content(response_content)
        if 'brand_id' in response:
            self.brand_id = response['brand_id']
        if 'fail_reasons' in response:
            self.fail_reasons = response['fail_reasons']
