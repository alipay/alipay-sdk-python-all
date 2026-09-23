#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftNftidOwnerQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftNftidOwnerQueryResponse, self).__init__()
        self._mold_hash = None
        self._mold_time = None
        self._nft_id = None
        self._receive_time = None
        self._third_id = None

    @property
    def mold_hash(self):
        return self._mold_hash

    @mold_hash.setter
    def mold_hash(self, value):
        self._mold_hash = value
    @property
    def mold_time(self):
        return self._mold_time

    @mold_time.setter
    def mold_time(self, value):
        self._mold_time = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def receive_time(self):
        return self._receive_time

    @receive_time.setter
    def receive_time(self, value):
        self._receive_time = value
    @property
    def third_id(self):
        return self._third_id

    @third_id.setter
    def third_id(self, value):
        self._third_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftNftidOwnerQueryResponse, self).parse_response_content(response_content)
        if 'mold_hash' in response:
            self.mold_hash = response['mold_hash']
        if 'mold_time' in response:
            self.mold_time = response['mold_time']
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
        if 'receive_time' in response:
            self.receive_time = response['receive_time']
        if 'third_id' in response:
            self.third_id = response['third_id']
