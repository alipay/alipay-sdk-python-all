#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServicePackageItem(object):

    def __init__(self):
        self._rights_id = None
        self._rights_name = None
        self._rights_type = None
        self._spec_quantity = None
        self._spec_quantity_left = None
        self._spec_type = None

    @property
    def rights_id(self):
        return self._rights_id

    @rights_id.setter
    def rights_id(self, value):
        self._rights_id = value
    @property
    def rights_name(self):
        return self._rights_name

    @rights_name.setter
    def rights_name(self, value):
        self._rights_name = value
    @property
    def rights_type(self):
        return self._rights_type

    @rights_type.setter
    def rights_type(self, value):
        self._rights_type = value
    @property
    def spec_quantity(self):
        return self._spec_quantity

    @spec_quantity.setter
    def spec_quantity(self, value):
        self._spec_quantity = value
    @property
    def spec_quantity_left(self):
        return self._spec_quantity_left

    @spec_quantity_left.setter
    def spec_quantity_left(self, value):
        self._spec_quantity_left = value
    @property
    def spec_type(self):
        return self._spec_type

    @spec_type.setter
    def spec_type(self, value):
        self._spec_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.rights_id:
            if hasattr(self.rights_id, 'to_alipay_dict'):
                params['rights_id'] = self.rights_id.to_alipay_dict()
            else:
                params['rights_id'] = self.rights_id
        if self.rights_name:
            if hasattr(self.rights_name, 'to_alipay_dict'):
                params['rights_name'] = self.rights_name.to_alipay_dict()
            else:
                params['rights_name'] = self.rights_name
        if self.rights_type:
            if hasattr(self.rights_type, 'to_alipay_dict'):
                params['rights_type'] = self.rights_type.to_alipay_dict()
            else:
                params['rights_type'] = self.rights_type
        if self.spec_quantity:
            if hasattr(self.spec_quantity, 'to_alipay_dict'):
                params['spec_quantity'] = self.spec_quantity.to_alipay_dict()
            else:
                params['spec_quantity'] = self.spec_quantity
        if self.spec_quantity_left:
            if hasattr(self.spec_quantity_left, 'to_alipay_dict'):
                params['spec_quantity_left'] = self.spec_quantity_left.to_alipay_dict()
            else:
                params['spec_quantity_left'] = self.spec_quantity_left
        if self.spec_type:
            if hasattr(self.spec_type, 'to_alipay_dict'):
                params['spec_type'] = self.spec_type.to_alipay_dict()
            else:
                params['spec_type'] = self.spec_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServicePackageItem()
        if 'rights_id' in d:
            o.rights_id = d['rights_id']
        if 'rights_name' in d:
            o.rights_name = d['rights_name']
        if 'rights_type' in d:
            o.rights_type = d['rights_type']
        if 'spec_quantity' in d:
            o.spec_quantity = d['spec_quantity']
        if 'spec_quantity_left' in d:
            o.spec_quantity_left = d['spec_quantity_left']
        if 'spec_type' in d:
            o.spec_type = d['spec_type']
        return o


