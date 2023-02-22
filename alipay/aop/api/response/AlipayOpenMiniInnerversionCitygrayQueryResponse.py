#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppGrayCityDto import MiniAppGrayCityDto


class AlipayOpenMiniInnerversionCitygrayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionCitygrayQueryResponse, self).__init__()
        self._city_code = None
        self._city_codes = None
        self._city_name = None
        self._gray_citys = None
        self._rule_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_codes(self):
        return self._city_codes

    @city_codes.setter
    def city_codes(self, value):
        if isinstance(value, list):
            self._city_codes = list()
            for i in value:
                self._city_codes.append(i)
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def gray_citys(self):
        return self._gray_citys

    @gray_citys.setter
    def gray_citys(self, value):
        if isinstance(value, list):
            self._gray_citys = list()
            for i in value:
                if isinstance(i, MiniAppGrayCityDto):
                    self._gray_citys.append(i)
                else:
                    self._gray_citys.append(MiniAppGrayCityDto.from_alipay_dict(i))
    @property
    def rule_code(self):
        return self._rule_code

    @rule_code.setter
    def rule_code(self, value):
        self._rule_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionCitygrayQueryResponse, self).parse_response_content(response_content)
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'city_codes' in response:
            self.city_codes = response['city_codes']
        if 'city_name' in response:
            self.city_name = response['city_name']
        if 'gray_citys' in response:
            self.gray_citys = response['gray_citys']
        if 'rule_code' in response:
            self.rule_code = response['rule_code']
