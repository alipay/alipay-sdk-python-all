#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FqQrCodeExtendParams import FqQrCodeExtendParams


class AlipayPcreditHuabeiFqqrcodeHbfqCreateModel(object):

    def __init__(self):
        self._address = None
        self._area_code = None
        self._city_code = None
        self._code_type = None
        self._fqqr_code_ext_info = None
        self._materials = None
        self._name = None
        self._out_request_no = None
        self._province_code = None
        self._quantity = None
        self._smid = None
        self._source = None
        self._store_id = None
        self._street_code = None
        self._tel = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def fqqr_code_ext_info(self):
        return self._fqqr_code_ext_info

    @fqqr_code_ext_info.setter
    def fqqr_code_ext_info(self, value):
        if isinstance(value, FqQrCodeExtendParams):
            self._fqqr_code_ext_info = value
        else:
            self._fqqr_code_ext_info = FqQrCodeExtendParams.from_alipay_dict(value)
    @property
    def materials(self):
        return self._materials

    @materials.setter
    def materials(self, value):
        self._materials = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def street_code(self):
        return self._street_code

    @street_code.setter
    def street_code(self, value):
        self._street_code = value
    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.fqqr_code_ext_info:
            if hasattr(self.fqqr_code_ext_info, 'to_alipay_dict'):
                params['fqqr_code_ext_info'] = self.fqqr_code_ext_info.to_alipay_dict()
            else:
                params['fqqr_code_ext_info'] = self.fqqr_code_ext_info
        if self.materials:
            if hasattr(self.materials, 'to_alipay_dict'):
                params['materials'] = self.materials.to_alipay_dict()
            else:
                params['materials'] = self.materials
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.street_code:
            if hasattr(self.street_code, 'to_alipay_dict'):
                params['street_code'] = self.street_code.to_alipay_dict()
            else:
                params['street_code'] = self.street_code
        if self.tel:
            if hasattr(self.tel, 'to_alipay_dict'):
                params['tel'] = self.tel.to_alipay_dict()
            else:
                params['tel'] = self.tel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiFqqrcodeHbfqCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'fqqr_code_ext_info' in d:
            o.fqqr_code_ext_info = d['fqqr_code_ext_info']
        if 'materials' in d:
            o.materials = d['materials']
        if 'name' in d:
            o.name = d['name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'smid' in d:
            o.smid = d['smid']
        if 'source' in d:
            o.source = d['source']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'street_code' in d:
            o.street_code = d['street_code']
        if 'tel' in d:
            o.tel = d['tel']
        return o


