#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SecurityScene(object):

    def __init__(self):
        self._access_channel = None
        self._ctu_params = None
        self._product_name = None
        self._product_node = None
        self._security_scene_params = None
        self._system_name = None
        self._total_fee = None

    @property
    def access_channel(self):
        return self._access_channel

    @access_channel.setter
    def access_channel(self, value):
        self._access_channel = value
    @property
    def ctu_params(self):
        return self._ctu_params

    @ctu_params.setter
    def ctu_params(self, value):
        self._ctu_params = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_node(self):
        return self._product_node

    @product_node.setter
    def product_node(self, value):
        self._product_node = value
    @property
    def security_scene_params(self):
        return self._security_scene_params

    @security_scene_params.setter
    def security_scene_params(self, value):
        self._security_scene_params = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_channel:
            if hasattr(self.access_channel, 'to_alipay_dict'):
                params['access_channel'] = self.access_channel.to_alipay_dict()
            else:
                params['access_channel'] = self.access_channel
        if self.ctu_params:
            if hasattr(self.ctu_params, 'to_alipay_dict'):
                params['ctu_params'] = self.ctu_params.to_alipay_dict()
            else:
                params['ctu_params'] = self.ctu_params
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_node:
            if hasattr(self.product_node, 'to_alipay_dict'):
                params['product_node'] = self.product_node.to_alipay_dict()
            else:
                params['product_node'] = self.product_node
        if self.security_scene_params:
            if hasattr(self.security_scene_params, 'to_alipay_dict'):
                params['security_scene_params'] = self.security_scene_params.to_alipay_dict()
            else:
                params['security_scene_params'] = self.security_scene_params
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = self.total_fee.to_alipay_dict()
            else:
                params['total_fee'] = self.total_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SecurityScene()
        if 'access_channel' in d:
            o.access_channel = d['access_channel']
        if 'ctu_params' in d:
            o.ctu_params = d['ctu_params']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_node' in d:
            o.product_node = d['product_node']
        if 'security_scene_params' in d:
            o.security_scene_params = d['security_scene_params']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'total_fee' in d:
            o.total_fee = d['total_fee']
        return o


