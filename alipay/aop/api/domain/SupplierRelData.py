#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierRelData(object):

    def __init__(self):
        self._material_id = None
        self._material_name = None
        self._out_supplier_id = None
        self._out_supplier_name = None
        self._supplier_material_id = None
        self._supplier_material_name = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def out_supplier_id(self):
        return self._out_supplier_id

    @out_supplier_id.setter
    def out_supplier_id(self, value):
        self._out_supplier_id = value
    @property
    def out_supplier_name(self):
        return self._out_supplier_name

    @out_supplier_name.setter
    def out_supplier_name(self, value):
        self._out_supplier_name = value
    @property
    def supplier_material_id(self):
        return self._supplier_material_id

    @supplier_material_id.setter
    def supplier_material_id(self, value):
        self._supplier_material_id = value
    @property
    def supplier_material_name(self):
        return self._supplier_material_name

    @supplier_material_name.setter
    def supplier_material_name(self, value):
        self._supplier_material_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.out_supplier_id:
            if hasattr(self.out_supplier_id, 'to_alipay_dict'):
                params['out_supplier_id'] = self.out_supplier_id.to_alipay_dict()
            else:
                params['out_supplier_id'] = self.out_supplier_id
        if self.out_supplier_name:
            if hasattr(self.out_supplier_name, 'to_alipay_dict'):
                params['out_supplier_name'] = self.out_supplier_name.to_alipay_dict()
            else:
                params['out_supplier_name'] = self.out_supplier_name
        if self.supplier_material_id:
            if hasattr(self.supplier_material_id, 'to_alipay_dict'):
                params['supplier_material_id'] = self.supplier_material_id.to_alipay_dict()
            else:
                params['supplier_material_id'] = self.supplier_material_id
        if self.supplier_material_name:
            if hasattr(self.supplier_material_name, 'to_alipay_dict'):
                params['supplier_material_name'] = self.supplier_material_name.to_alipay_dict()
            else:
                params['supplier_material_name'] = self.supplier_material_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierRelData()
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'out_supplier_id' in d:
            o.out_supplier_id = d['out_supplier_id']
        if 'out_supplier_name' in d:
            o.out_supplier_name = d['out_supplier_name']
        if 'supplier_material_id' in d:
            o.supplier_material_id = d['supplier_material_id']
        if 'supplier_material_name' in d:
            o.supplier_material_name = d['supplier_material_name']
        return o


