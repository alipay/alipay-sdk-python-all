#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessProduceOrder(object):

    def __init__(self):
        self._batch_id = None
        self._produce_order_id = None
        self._produce_quantity = None
        self._stuff_attr_name = None
        self._stuff_material = None
        self._stuff_size = None
        self._stuff_type = None
        self._template_id = None
        self._template_name = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def produce_order_id(self):
        return self._produce_order_id

    @produce_order_id.setter
    def produce_order_id(self, value):
        self._produce_order_id = value
    @property
    def produce_quantity(self):
        return self._produce_quantity

    @produce_quantity.setter
    def produce_quantity(self, value):
        self._produce_quantity = value
    @property
    def stuff_attr_name(self):
        return self._stuff_attr_name

    @stuff_attr_name.setter
    def stuff_attr_name(self, value):
        self._stuff_attr_name = value
    @property
    def stuff_material(self):
        return self._stuff_material

    @stuff_material.setter
    def stuff_material(self, value):
        self._stuff_material = value
    @property
    def stuff_size(self):
        return self._stuff_size

    @stuff_size.setter
    def stuff_size(self, value):
        self._stuff_size = value
    @property
    def stuff_type(self):
        return self._stuff_type

    @stuff_type.setter
    def stuff_type(self, value):
        self._stuff_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.produce_order_id:
            if hasattr(self.produce_order_id, 'to_alipay_dict'):
                params['produce_order_id'] = self.produce_order_id.to_alipay_dict()
            else:
                params['produce_order_id'] = self.produce_order_id
        if self.produce_quantity:
            if hasattr(self.produce_quantity, 'to_alipay_dict'):
                params['produce_quantity'] = self.produce_quantity.to_alipay_dict()
            else:
                params['produce_quantity'] = self.produce_quantity
        if self.stuff_attr_name:
            if hasattr(self.stuff_attr_name, 'to_alipay_dict'):
                params['stuff_attr_name'] = self.stuff_attr_name.to_alipay_dict()
            else:
                params['stuff_attr_name'] = self.stuff_attr_name
        if self.stuff_material:
            if hasattr(self.stuff_material, 'to_alipay_dict'):
                params['stuff_material'] = self.stuff_material.to_alipay_dict()
            else:
                params['stuff_material'] = self.stuff_material
        if self.stuff_size:
            if hasattr(self.stuff_size, 'to_alipay_dict'):
                params['stuff_size'] = self.stuff_size.to_alipay_dict()
            else:
                params['stuff_size'] = self.stuff_size
        if self.stuff_type:
            if hasattr(self.stuff_type, 'to_alipay_dict'):
                params['stuff_type'] = self.stuff_type.to_alipay_dict()
            else:
                params['stuff_type'] = self.stuff_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessProduceOrder()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'produce_order_id' in d:
            o.produce_order_id = d['produce_order_id']
        if 'produce_quantity' in d:
            o.produce_quantity = d['produce_quantity']
        if 'stuff_attr_name' in d:
            o.stuff_attr_name = d['stuff_attr_name']
        if 'stuff_material' in d:
            o.stuff_material = d['stuff_material']
        if 'stuff_size' in d:
            o.stuff_size = d['stuff_size']
        if 'stuff_type' in d:
            o.stuff_type = d['stuff_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        return o


