#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceServiceBaseVO(object):

    def __init__(self):
        self._alias_name = None
        self._icon = None
        self._node_type = None
        self._product_name = None
        self._status = None
        self._xp_id = None

    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def xp_id(self):
        return self._xp_id

    @xp_id.setter
    def xp_id(self, value):
        self._xp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.xp_id:
            if hasattr(self.xp_id, 'to_alipay_dict'):
                params['xp_id'] = self.xp_id.to_alipay_dict()
            else:
                params['xp_id'] = self.xp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceServiceBaseVO()
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'icon' in d:
            o.icon = d['icon']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'status' in d:
            o.status = d['status']
        if 'xp_id' in d:
            o.xp_id = d['xp_id']
        return o


