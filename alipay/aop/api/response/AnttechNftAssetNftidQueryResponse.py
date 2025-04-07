#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftAssetNftidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftAssetNftidQueryResponse, self).__init__()
        self._author_name = None
        self._issuer_name = None
        self._mini_image_path = None
        self._nft_id = None
        self._sku_id = None
        self._sku_name = None

    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        self._author_name = value
    @property
    def issuer_name(self):
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, value):
        self._issuer_name = value
    @property
    def mini_image_path(self):
        return self._mini_image_path

    @mini_image_path.setter
    def mini_image_path(self, value):
        self._mini_image_path = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftAssetNftidQueryResponse, self).parse_response_content(response_content)
        if 'author_name' in response:
            self.author_name = response['author_name']
        if 'issuer_name' in response:
            self.issuer_name = response['issuer_name']
        if 'mini_image_path' in response:
            self.mini_image_path = response['mini_image_path']
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'sku_name' in response:
            self.sku_name = response['sku_name']
