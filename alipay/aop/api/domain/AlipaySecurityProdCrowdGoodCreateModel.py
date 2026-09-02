#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdCrowdGoodCreateModel(object):

    def __init__(self):
        self._address = None
        self._batch_number = None
        self._business_id = None
        self._business_id_type = None
        self._city_code = None
        self._description = None
        self._ext_info = None
        self._good_type = None
        self._latitude = None
        self._longitude = None
        self._name = None
        self._operation_mode = None
        self._operator_id = None
        self._out_biz_id = None
        self._place_holder = None
        self._shop_id = None
        self._template_id = None
        self._total = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def batch_number(self):
        return self._batch_number

    @batch_number.setter
    def batch_number(self, value):
        self._batch_number = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def business_id_type(self):
        return self._business_id_type

    @business_id_type.setter
    def business_id_type(self, value):
        self._business_id_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def good_type(self):
        return self._good_type

    @good_type.setter
    def good_type(self, value):
        self._good_type = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operation_mode(self):
        return self._operation_mode

    @operation_mode.setter
    def operation_mode(self, value):
        self._operation_mode = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def place_holder(self):
        return self._place_holder

    @place_holder.setter
    def place_holder(self, value):
        self._place_holder = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.batch_number:
            if hasattr(self.batch_number, 'to_alipay_dict'):
                params['batch_number'] = self.batch_number.to_alipay_dict()
            else:
                params['batch_number'] = self.batch_number
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.business_id_type:
            if hasattr(self.business_id_type, 'to_alipay_dict'):
                params['business_id_type'] = self.business_id_type.to_alipay_dict()
            else:
                params['business_id_type'] = self.business_id_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.good_type:
            if hasattr(self.good_type, 'to_alipay_dict'):
                params['good_type'] = self.good_type.to_alipay_dict()
            else:
                params['good_type'] = self.good_type
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operation_mode:
            if hasattr(self.operation_mode, 'to_alipay_dict'):
                params['operation_mode'] = self.operation_mode.to_alipay_dict()
            else:
                params['operation_mode'] = self.operation_mode
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.place_holder:
            if hasattr(self.place_holder, 'to_alipay_dict'):
                params['place_holder'] = self.place_holder.to_alipay_dict()
            else:
                params['place_holder'] = self.place_holder
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdCrowdGoodCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'batch_number' in d:
            o.batch_number = d['batch_number']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'business_id_type' in d:
            o.business_id_type = d['business_id_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'description' in d:
            o.description = d['description']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'good_type' in d:
            o.good_type = d['good_type']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'name' in d:
            o.name = d['name']
        if 'operation_mode' in d:
            o.operation_mode = d['operation_mode']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'place_holder' in d:
            o.place_holder = d['place_holder']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'total' in d:
            o.total = d['total']
        return o


