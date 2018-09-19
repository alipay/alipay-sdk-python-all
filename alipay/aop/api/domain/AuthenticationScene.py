#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthenticationScene(object):

    def __init__(self):
        self._access_channel = None
        self._biz_name = None
        self._biz_prod_node = None
        self._biz_product = None
        self._scene_params = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_prod_node(self):
        return self._biz_prod_node

    @biz_prod_node.setter
    def biz_prod_node(self, value):
        self._biz_prod_node = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def scene_params(self):
        return self._scene_params

    @scene_params.setter
    def scene_params(self, value):
        self._scene_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.biz_prod_node:
            if hasattr(self.biz_prod_node, 'to_alipay_dict'):
                params['biz_prod_node'] = self.biz_prod_node.to_alipay_dict()
            else:
                params['biz_prod_node'] = self.biz_prod_node
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.scene_params:
            if hasattr(self.scene_params, 'to_alipay_dict'):
                params['scene_params'] = self.scene_params.to_alipay_dict()
            else:
                params['scene_params'] = self.scene_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthenticationScene()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'biz_prod_node' in d:
            o.biz_prod_node = d['biz_prod_node']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'scene_params' in d:
            o.scene_params = d['scene_params']
        return o


