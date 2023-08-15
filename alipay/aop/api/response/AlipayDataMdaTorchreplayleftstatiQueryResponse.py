#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaTorchreplayleftstatiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaTorchreplayleftstatiQueryResponse, self).__init__()
        self._country_cnt = None
        self._foreign_platform = None
        self._foreign_platform_cnt = None
        self._internal_platform = None
        self._internal_platform_cnt = None

    @property
    def country_cnt(self):
        return self._country_cnt

    @country_cnt.setter
    def country_cnt(self, value):
        self._country_cnt = value
    @property
    def foreign_platform(self):
        return self._foreign_platform

    @foreign_platform.setter
    def foreign_platform(self, value):
        self._foreign_platform = value
    @property
    def foreign_platform_cnt(self):
        return self._foreign_platform_cnt

    @foreign_platform_cnt.setter
    def foreign_platform_cnt(self, value):
        self._foreign_platform_cnt = value
    @property
    def internal_platform(self):
        return self._internal_platform

    @internal_platform.setter
    def internal_platform(self, value):
        self._internal_platform = value
    @property
    def internal_platform_cnt(self):
        return self._internal_platform_cnt

    @internal_platform_cnt.setter
    def internal_platform_cnt(self, value):
        self._internal_platform_cnt = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaTorchreplayleftstatiQueryResponse, self).parse_response_content(response_content)
        if 'country_cnt' in response:
            self.country_cnt = response['country_cnt']
        if 'foreign_platform' in response:
            self.foreign_platform = response['foreign_platform']
        if 'foreign_platform_cnt' in response:
            self.foreign_platform_cnt = response['foreign_platform_cnt']
        if 'internal_platform' in response:
            self.internal_platform = response['internal_platform']
        if 'internal_platform_cnt' in response:
            self.internal_platform_cnt = response['internal_platform_cnt']
