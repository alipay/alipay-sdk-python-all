#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcAssetAuthorizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAssetAuthorizeQueryResponse, self).__init__()
        self._apply_time = None
        self._asset_type = None
        self._available_limit = None
        self._capital_limit = None
        self._expiration_date = None
        self._status = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def available_limit(self):
        return self._available_limit

    @available_limit.setter
    def available_limit(self, value):
        self._available_limit = value
    @property
    def capital_limit(self):
        return self._capital_limit

    @capital_limit.setter
    def capital_limit(self, value):
        self._capital_limit = value
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAssetAuthorizeQueryResponse, self).parse_response_content(response_content)
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'asset_type' in response:
            self.asset_type = response['asset_type']
        if 'available_limit' in response:
            self.available_limit = response['available_limit']
        if 'capital_limit' in response:
            self.capital_limit = response['capital_limit']
        if 'expiration_date' in response:
            self.expiration_date = response['expiration_date']
        if 'status' in response:
            self.status = response['status']
