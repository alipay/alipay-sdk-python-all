#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliverySingleMaterial import DeliverySingleMaterial


class DeliveryMaterial(object):

    def __init__(self):
        self._delivery_single_material = None
        self._material_id_list = None

    @property
    def delivery_single_material(self):
        return self._delivery_single_material

    @delivery_single_material.setter
    def delivery_single_material(self, value):
        if isinstance(value, DeliverySingleMaterial):
            self._delivery_single_material = value
        else:
            self._delivery_single_material = DeliverySingleMaterial.from_alipay_dict(value)
    @property
    def material_id_list(self):
        return self._material_id_list

    @material_id_list.setter
    def material_id_list(self, value):
        if isinstance(value, list):
            self._material_id_list = list()
            for i in value:
                self._material_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_single_material:
            if hasattr(self.delivery_single_material, 'to_alipay_dict'):
                params['delivery_single_material'] = self.delivery_single_material.to_alipay_dict()
            else:
                params['delivery_single_material'] = self.delivery_single_material
        if self.material_id_list:
            if isinstance(self.material_id_list, list):
                for i in range(0, len(self.material_id_list)):
                    element = self.material_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_id_list[i] = element.to_alipay_dict()
            if hasattr(self.material_id_list, 'to_alipay_dict'):
                params['material_id_list'] = self.material_id_list.to_alipay_dict()
            else:
                params['material_id_list'] = self.material_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMaterial()
        if 'delivery_single_material' in d:
            o.delivery_single_material = d['delivery_single_material']
        if 'material_id_list' in d:
            o.material_id_list = d['material_id_list']
        return o


