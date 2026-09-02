#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLifeserviceUnifiedshopModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceUnifiedshopModifyResponse, self).__init__()
        self._copy_id = None
        self._status = None
        self._store_id = None

    @property
    def copy_id(self):
        return self._copy_id

    @copy_id.setter
    def copy_id(self, value):
        self._copy_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceUnifiedshopModifyResponse, self).parse_response_content(response_content)
        if 'copy_id' in response:
            self.copy_id = response['copy_id']
        if 'status' in response:
            self.status = response['status']
        if 'store_id' in response:
            self.store_id = response['store_id']
