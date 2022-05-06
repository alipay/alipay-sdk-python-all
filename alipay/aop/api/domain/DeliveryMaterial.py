#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliverySingleMaterial import DeliverySingleMaterial


class DeliveryMaterial(object):

    def __init__(self):
        self._delivery_single_material = None

    @property
    def delivery_single_material(self):
        return self._delivery_single_material

    @delivery_single_material.setter
    def delivery_single_material(self, value):
        if isinstance(value, DeliverySingleMaterial):
            self._delivery_single_material = value
        else:
            self._delivery_single_material = DeliverySingleMaterial.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_single_material:
            if hasattr(self.delivery_single_material, 'to_alipay_dict'):
                params['delivery_single_material'] = self.delivery_single_material.to_alipay_dict()
            else:
                params['delivery_single_material'] = self.delivery_single_material
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryMaterial()
        if 'delivery_single_material' in d:
            o.delivery_single_material = d['delivery_single_material']
        return o


