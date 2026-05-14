#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalStoreVirtualstoreCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStoreVirtualstoreCreateResponse, self).__init__()
        self._store_id = None

    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStoreVirtualstoreCreateResponse, self).parse_response_content(response_content)
        if 'store_id' in response:
            self.store_id = response['store_id']
