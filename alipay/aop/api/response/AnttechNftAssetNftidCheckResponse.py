#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftAssetNftidCheckResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftAssetNftidCheckResponse, self).__init__()
        self._nft_enable_send = None
        self._own_status = None
        self._receive_time = None

    @property
    def nft_enable_send(self):
        return self._nft_enable_send

    @nft_enable_send.setter
    def nft_enable_send(self, value):
        self._nft_enable_send = value
    @property
    def own_status(self):
        return self._own_status

    @own_status.setter
    def own_status(self, value):
        self._own_status = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftAssetNftidCheckResponse, self).parse_response_content(response_content)
        if 'nft_enable_send' in response:
            self.nft_enable_send = response['nft_enable_send']
        if 'own_status' in response:
            self.own_status = response['own_status']
        if 'receive_time' in response:
            self.receive_time = response['receive_time']
