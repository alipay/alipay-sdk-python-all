#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftTransferApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftTransferApplyResponse, self).__init__()
        self._nft_id = None
        self._req_msg_id = None
        self._sku_id = None

    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftTransferApplyResponse, self).parse_response_content(response_content)
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
        if 'req_msg_id' in response:
            self.req_msg_id = response['req_msg_id']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
