#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudDevopsDeviceConditionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudDevopsDeviceConditionQueryResponse, self).__init__()
        self._abi = None
        self._brand_product = None
        self._dpi = None
        self._os_version = None
        self._resolution = None

    @property
    def abi(self):
        return self._abi

    @abi.setter
    def abi(self, value):
        self._abi = value
    @property
    def brand_product(self):
        return self._brand_product

    @brand_product.setter
    def brand_product(self, value):
        self._brand_product = value
    @property
    def dpi(self):
        return self._dpi

    @dpi.setter
    def dpi(self, value):
        self._dpi = value
    @property
    def os_version(self):
        return self._os_version

    @os_version.setter
    def os_version(self, value):
        self._os_version = value
    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        self._resolution = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudDevopsDeviceConditionQueryResponse, self).parse_response_content(response_content)
        if 'abi' in response:
            self.abi = response['abi']
        if 'brand_product' in response:
            self.brand_product = response['brand_product']
        if 'dpi' in response:
            self.dpi = response['dpi']
        if 'os_version' in response:
            self.os_version = response['os_version']
        if 'resolution' in response:
            self.resolution = response['resolution']
