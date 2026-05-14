#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryInfoParam(object):

    def __init__(self):
        self._gift_num = None
        self._hospital_city = None
        self._hospital_level = None
        self._product_desc = None
        self._product_scene = None
        self._service_desc = None
        self._service_time = None
        self._service_time_unit = None
        self._show_applicability = None
        self._sku_tag = None
        self._supplier = None

    @property
    def gift_num(self):
        return self._gift_num

    @gift_num.setter
    def gift_num(self, value):
        self._gift_num = value
    @property
    def hospital_city(self):
        return self._hospital_city

    @hospital_city.setter
    def hospital_city(self, value):
        self._hospital_city = value
    @property
    def hospital_level(self):
        return self._hospital_level

    @hospital_level.setter
    def hospital_level(self, value):
        self._hospital_level = value
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def product_scene(self):
        return self._product_scene

    @product_scene.setter
    def product_scene(self, value):
        self._product_scene = value
    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_time(self):
        return self._service_time

    @service_time.setter
    def service_time(self, value):
        self._service_time = value
    @property
    def service_time_unit(self):
        return self._service_time_unit

    @service_time_unit.setter
    def service_time_unit(self, value):
        self._service_time_unit = value
    @property
    def show_applicability(self):
        return self._show_applicability

    @show_applicability.setter
    def show_applicability(self, value):
        self._show_applicability = value
    @property
    def sku_tag(self):
        return self._sku_tag

    @sku_tag.setter
    def sku_tag(self, value):
        self._sku_tag = value
    @property
    def supplier(self):
        return self._supplier

    @supplier.setter
    def supplier(self, value):
        self._supplier = value


    def to_alipay_dict(self):
        params = dict()
        if self.gift_num:
            if hasattr(self.gift_num, 'to_alipay_dict'):
                params['gift_num'] = self.gift_num.to_alipay_dict()
            else:
                params['gift_num'] = self.gift_num
        if self.hospital_city:
            if hasattr(self.hospital_city, 'to_alipay_dict'):
                params['hospital_city'] = self.hospital_city.to_alipay_dict()
            else:
                params['hospital_city'] = self.hospital_city
        if self.hospital_level:
            if hasattr(self.hospital_level, 'to_alipay_dict'):
                params['hospital_level'] = self.hospital_level.to_alipay_dict()
            else:
                params['hospital_level'] = self.hospital_level
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.product_scene:
            if hasattr(self.product_scene, 'to_alipay_dict'):
                params['product_scene'] = self.product_scene.to_alipay_dict()
            else:
                params['product_scene'] = self.product_scene
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_time:
            if hasattr(self.service_time, 'to_alipay_dict'):
                params['service_time'] = self.service_time.to_alipay_dict()
            else:
                params['service_time'] = self.service_time
        if self.service_time_unit:
            if hasattr(self.service_time_unit, 'to_alipay_dict'):
                params['service_time_unit'] = self.service_time_unit.to_alipay_dict()
            else:
                params['service_time_unit'] = self.service_time_unit
        if self.show_applicability:
            if hasattr(self.show_applicability, 'to_alipay_dict'):
                params['show_applicability'] = self.show_applicability.to_alipay_dict()
            else:
                params['show_applicability'] = self.show_applicability
        if self.sku_tag:
            if hasattr(self.sku_tag, 'to_alipay_dict'):
                params['sku_tag'] = self.sku_tag.to_alipay_dict()
            else:
                params['sku_tag'] = self.sku_tag
        if self.supplier:
            if hasattr(self.supplier, 'to_alipay_dict'):
                params['supplier'] = self.supplier.to_alipay_dict()
            else:
                params['supplier'] = self.supplier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryInfoParam()
        if 'gift_num' in d:
            o.gift_num = d['gift_num']
        if 'hospital_city' in d:
            o.hospital_city = d['hospital_city']
        if 'hospital_level' in d:
            o.hospital_level = d['hospital_level']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_scene' in d:
            o.product_scene = d['product_scene']
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_time' in d:
            o.service_time = d['service_time']
        if 'service_time_unit' in d:
            o.service_time_unit = d['service_time_unit']
        if 'show_applicability' in d:
            o.show_applicability = d['show_applicability']
        if 'sku_tag' in d:
            o.sku_tag = d['sku_tag']
        if 'supplier' in d:
            o.supplier = d['supplier']
        return o


