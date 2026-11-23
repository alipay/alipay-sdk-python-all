#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAiguideItemsyncSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAiguideItemsyncSyncResponse, self).__init__()
        self._afts_url = None
        self._n_device_id = None
        self._sn = None

    @property
    def afts_url(self):
        return self._afts_url

    @afts_url.setter
    def afts_url(self, value):
        self._afts_url = value
    @property
    def n_device_id(self):
        return self._n_device_id

    @n_device_id.setter
    def n_device_id(self, value):
        self._n_device_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAiguideItemsyncSyncResponse, self).parse_response_content(response_content)
        if 'afts_url' in response:
            self.afts_url = response['afts_url']
        if 'n_device_id' in response:
            self.n_device_id = response['n_device_id']
        if 'sn' in response:
            self.sn = response['sn']
