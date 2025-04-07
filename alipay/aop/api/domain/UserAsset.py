#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAsset(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.author_name:
            if hasattr(self.author_name, 'to_alipay_dict'):
                params['author_name'] = self.author_name.to_alipay_dict()
            else:
                params['author_name'] = self.author_name
        if self.issuer_name:
            if hasattr(self.issuer_name, 'to_alipay_dict'):
                params['issuer_name'] = self.issuer_name.to_alipay_dict()
            else:
                params['issuer_name'] = self.issuer_name
        if self.mini_image_path:
            if hasattr(self.mini_image_path, 'to_alipay_dict'):
                params['mini_image_path'] = self.mini_image_path.to_alipay_dict()
            else:
                params['mini_image_path'] = self.mini_image_path
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAsset()
        if 'author_name' in d:
            o.author_name = d['author_name']
        if 'issuer_name' in d:
            o.issuer_name = d['issuer_name']
        if 'mini_image_path' in d:
            o.mini_image_path = d['mini_image_path']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        return o


