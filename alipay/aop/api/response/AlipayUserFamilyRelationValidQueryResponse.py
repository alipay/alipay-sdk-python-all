#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserFamilyRelationValidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserFamilyRelationValidQueryResponse, self).__init__()
        self._has_family = None
        self._has_valid_family = None

    @property
    def has_family(self):
        return self._has_family

    @has_family.setter
    def has_family(self, value):
        self._has_family = value
    @property
    def has_valid_family(self):
        return self._has_valid_family

    @has_valid_family.setter
    def has_valid_family(self, value):
        self._has_valid_family = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserFamilyRelationValidQueryResponse, self).parse_response_content(response_content)
        if 'has_family' in response:
            self.has_family = response['has_family']
        if 'has_valid_family' in response:
            self.has_valid_family = response['has_valid_family']
