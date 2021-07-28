#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishEstimatedInfo(object):

    def __init__(self):
        self._ds_id = None
        self._ds_type = None
        self._inventory = None
        self._out_shop_id = None
        self._shop_id = None
        self._status = None
        self._update_user = None

    @property
    def ds_id(self):
        return self._ds_id

    @ds_id.setter
    def ds_id(self, value):
        self._ds_id = value
    @property
    def ds_type(self):
        return self._ds_type

    @ds_type.setter
    def ds_type(self, value):
        self._ds_type = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.ds_id:
            if hasattr(self.ds_id, 'to_alipay_dict'):
                params['ds_id'] = self.ds_id.to_alipay_dict()
            else:
                params['ds_id'] = self.ds_id
        if self.ds_type:
            if hasattr(self.ds_type, 'to_alipay_dict'):
                params['ds_type'] = self.ds_type.to_alipay_dict()
            else:
                params['ds_type'] = self.ds_type
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishEstimatedInfo()
        if 'ds_id' in d:
            o.ds_id = d['ds_id']
        if 'ds_type' in d:
            o.ds_type = d['ds_type']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


