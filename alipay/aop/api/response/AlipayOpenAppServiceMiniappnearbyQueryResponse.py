#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppServiceMiniappnearbyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServiceMiniappnearbyQueryResponse, self).__init__()
        self._carrier_code = None
        self._carrier_url = None
        self._detail_desc = None
        self._forward_catalog_id = None
        self._key_word_list = None
        self._service_code = None
        self._service_logo = None
        self._service_name = None
        self._simple_desc = None

    @property
    def carrier_code(self):
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, value):
        self._carrier_code = value
    @property
    def carrier_url(self):
        return self._carrier_url

    @carrier_url.setter
    def carrier_url(self, value):
        self._carrier_url = value
    @property
    def detail_desc(self):
        return self._detail_desc

    @detail_desc.setter
    def detail_desc(self, value):
        self._detail_desc = value
    @property
    def forward_catalog_id(self):
        return self._forward_catalog_id

    @forward_catalog_id.setter
    def forward_catalog_id(self, value):
        self._forward_catalog_id = value
    @property
    def key_word_list(self):
        return self._key_word_list

    @key_word_list.setter
    def key_word_list(self, value):
        self._key_word_list = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_logo(self):
        return self._service_logo

    @service_logo.setter
    def service_logo(self, value):
        self._service_logo = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def simple_desc(self):
        return self._simple_desc

    @simple_desc.setter
    def simple_desc(self, value):
        self._simple_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServiceMiniappnearbyQueryResponse, self).parse_response_content(response_content)
        if 'carrier_code' in response:
            self.carrier_code = response['carrier_code']
        if 'carrier_url' in response:
            self.carrier_url = response['carrier_url']
        if 'detail_desc' in response:
            self.detail_desc = response['detail_desc']
        if 'forward_catalog_id' in response:
            self.forward_catalog_id = response['forward_catalog_id']
        if 'key_word_list' in response:
            self.key_word_list = response['key_word_list']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'service_logo' in response:
            self.service_logo = response['service_logo']
        if 'service_name' in response:
            self.service_name = response['service_name']
        if 'simple_desc' in response:
            self.simple_desc = response['simple_desc']
