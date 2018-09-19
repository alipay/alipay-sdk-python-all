#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicSettingCategoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicSettingCategoryQueryResponse, self).__init__()
        self._primary_category = None
        self._secondary_category = None

    @property
    def primary_category(self):
        return self._primary_category

    @primary_category.setter
    def primary_category(self, value):
        self._primary_category = value
    @property
    def secondary_category(self):
        return self._secondary_category

    @secondary_category.setter
    def secondary_category(self, value):
        self._secondary_category = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicSettingCategoryQueryResponse, self).parse_response_content(response_content)
        if 'primary_category' in response:
            self.primary_category = response['primary_category']
        if 'secondary_category' in response:
            self.secondary_category = response['secondary_category']
