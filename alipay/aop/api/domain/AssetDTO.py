#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetDTO(object):

    def __init__(self):
        self._author_name = None
        self._index_id = None
        self._issue_name = None
        self._mini_image_url = None
        self._nft_id = None
        self._sku_id = None

    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        self._author_name = value
    @property
    def index_id(self):
        return self._index_id

    @index_id.setter
    def index_id(self, value):
        self._index_id = value
    @property
    def issue_name(self):
        return self._issue_name

    @issue_name.setter
    def issue_name(self, value):
        self._issue_name = value
    @property
    def mini_image_url(self):
        return self._mini_image_url

    @mini_image_url.setter
    def mini_image_url(self, value):
        self._mini_image_url = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.author_name:
            if hasattr(self.author_name, 'to_alipay_dict'):
                params['author_name'] = self.author_name.to_alipay_dict()
            else:
                params['author_name'] = self.author_name
        if self.index_id:
            if hasattr(self.index_id, 'to_alipay_dict'):
                params['index_id'] = self.index_id.to_alipay_dict()
            else:
                params['index_id'] = self.index_id
        if self.issue_name:
            if hasattr(self.issue_name, 'to_alipay_dict'):
                params['issue_name'] = self.issue_name.to_alipay_dict()
            else:
                params['issue_name'] = self.issue_name
        if self.mini_image_url:
            if hasattr(self.mini_image_url, 'to_alipay_dict'):
                params['mini_image_url'] = self.mini_image_url.to_alipay_dict()
            else:
                params['mini_image_url'] = self.mini_image_url
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDTO()
        if 'author_name' in d:
            o.author_name = d['author_name']
        if 'index_id' in d:
            o.index_id = d['index_id']
        if 'issue_name' in d:
            o.issue_name = d['issue_name']
        if 'mini_image_url' in d:
            o.mini_image_url = d['mini_image_url']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


