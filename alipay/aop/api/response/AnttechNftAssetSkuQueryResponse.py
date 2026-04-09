#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftAssetSkuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftAssetSkuQueryResponse, self).__init__()
        self._author = None
        self._issuer = None
        self._nft_id = None
        self._sku_hash = None
        self._sku_id = None
        self._sku_label_color = None
        self._sku_name = None
        self._thumbnail = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
    @property
    def issuer(self):
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        self._issuer = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def sku_hash(self):
        return self._sku_hash

    @sku_hash.setter
    def sku_hash(self, value):
        self._sku_hash = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_label_color(self):
        return self._sku_label_color

    @sku_label_color.setter
    def sku_label_color(self, value):
        self._sku_label_color = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftAssetSkuQueryResponse, self).parse_response_content(response_content)
        if 'author' in response:
            self.author = response['author']
        if 'issuer' in response:
            self.issuer = response['issuer']
        if 'nft_id' in response:
            self.nft_id = response['nft_id']
        if 'sku_hash' in response:
            self.sku_hash = response['sku_hash']
        if 'sku_id' in response:
            self.sku_id = response['sku_id']
        if 'sku_label_color' in response:
            self.sku_label_color = response['sku_label_color']
        if 'sku_name' in response:
            self.sku_name = response['sku_name']
        if 'thumbnail' in response:
            self.thumbnail = response['thumbnail']
