#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductionMaterial import ProductionMaterial
from alipay.aop.api.domain.NcoilopenAddressInfo import NcoilopenAddressInfo


class AlipayOpenSpNfcexpoprodOrderCreateModel(object):

    def __init__(self):
        self._order_desc = None
        self._out_biz_no = None
        self._production_material = None
        self._quantity = None
        self._shipping_address = None
        self._solution_id = None
        self._sub_solution_id = None
        self._template_code = None

    @property
    def order_desc(self):
        return self._order_desc

    @order_desc.setter
    def order_desc(self, value):
        self._order_desc = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def production_material(self):
        return self._production_material

    @production_material.setter
    def production_material(self, value):
        if isinstance(value, ProductionMaterial):
            self._production_material = value
        else:
            self._production_material = ProductionMaterial.from_alipay_dict(value)
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def shipping_address(self):
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        if isinstance(value, NcoilopenAddressInfo):
            self._shipping_address = value
        else:
            self._shipping_address = NcoilopenAddressInfo.from_alipay_dict(value)
    @property
    def solution_id(self):
        return self._solution_id

    @solution_id.setter
    def solution_id(self, value):
        self._solution_id = value
    @property
    def sub_solution_id(self):
        return self._sub_solution_id

    @sub_solution_id.setter
    def sub_solution_id(self, value):
        self._sub_solution_id = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_desc:
            if hasattr(self.order_desc, 'to_alipay_dict'):
                params['order_desc'] = self.order_desc.to_alipay_dict()
            else:
                params['order_desc'] = self.order_desc
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.production_material:
            if hasattr(self.production_material, 'to_alipay_dict'):
                params['production_material'] = self.production_material.to_alipay_dict()
            else:
                params['production_material'] = self.production_material
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.shipping_address:
            if hasattr(self.shipping_address, 'to_alipay_dict'):
                params['shipping_address'] = self.shipping_address.to_alipay_dict()
            else:
                params['shipping_address'] = self.shipping_address
        if self.solution_id:
            if hasattr(self.solution_id, 'to_alipay_dict'):
                params['solution_id'] = self.solution_id.to_alipay_dict()
            else:
                params['solution_id'] = self.solution_id
        if self.sub_solution_id:
            if hasattr(self.sub_solution_id, 'to_alipay_dict'):
                params['sub_solution_id'] = self.sub_solution_id.to_alipay_dict()
            else:
                params['sub_solution_id'] = self.sub_solution_id
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNfcexpoprodOrderCreateModel()
        if 'order_desc' in d:
            o.order_desc = d['order_desc']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'production_material' in d:
            o.production_material = d['production_material']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'shipping_address' in d:
            o.shipping_address = d['shipping_address']
        if 'solution_id' in d:
            o.solution_id = d['solution_id']
        if 'sub_solution_id' in d:
            o.sub_solution_id = d['sub_solution_id']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


