#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIndirectIotbindQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIndirectIotbindQueryResponse, self).__init__()
        self._bind_status = None
        self._bind_time = None
        self._device_id = None
        self._smid = None
        self._supplier_id = None

    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def bind_time(self):
        return self._bind_time

    @bind_time.setter
    def bind_time(self, value):
        self._bind_time = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIndirectIotbindQueryResponse, self).parse_response_content(response_content)
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'bind_time' in response:
            self.bind_time = response['bind_time']
        if 'device_id' in response:
            self.device_id = response['device_id']
        if 'smid' in response:
            self.smid = response['smid']
        if 'supplier_id' in response:
            self.supplier_id = response['supplier_id']
