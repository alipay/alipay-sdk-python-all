#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecEntity(object):

    def __init__(self):
        self._id = None
        self._shop_id = None
        self._spec_name = None
        self._system = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.system:
            if hasattr(self.system, 'to_alipay_dict'):
                params['system'] = self.system.to_alipay_dict()
            else:
                params['system'] = self.system
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecEntity()
        if 'id' in d:
            o.id = d['id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'system' in d:
            o.system = d['system']
        return o


