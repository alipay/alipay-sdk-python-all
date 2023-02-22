#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinDataserviceRegiongroupMatchResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinDataserviceRegiongroupMatchResponse, self).__init__()
        self._region_group_codes = None
        self._region_group_count_101 = None
        self._region_group_count_115 = None
        self._region_group_count_147 = None

    @property
    def region_group_codes(self):
        return self._region_group_codes

    @region_group_codes.setter
    def region_group_codes(self, value):
        if isinstance(value, list):
            self._region_group_codes = list()
            for i in value:
                self._region_group_codes.append(i)
    @property
    def region_group_count_101(self):
        return self._region_group_count_101

    @region_group_count_101.setter
    def region_group_count_101(self, value):
        self._region_group_count_101 = value
    @property
    def region_group_count_115(self):
        return self._region_group_count_115

    @region_group_count_115.setter
    def region_group_count_115(self, value):
        self._region_group_count_115 = value
    @property
    def region_group_count_147(self):
        return self._region_group_count_147

    @region_group_count_147.setter
    def region_group_count_147(self, value):
        self._region_group_count_147 = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinDataserviceRegiongroupMatchResponse, self).parse_response_content(response_content)
        if 'region_group_codes' in response:
            self.region_group_codes = response['region_group_codes']
        if 'region_group_count_101' in response:
            self.region_group_count_101 = response['region_group_count_101']
        if 'region_group_count_115' in response:
            self.region_group_count_115 = response['region_group_count_115']
        if 'region_group_count_147' in response:
            self.region_group_count_147 = response['region_group_count_147']
