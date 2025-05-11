#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NorderTagPositionExtInfo import NorderTagPositionExtInfo


class AlipayOpenSpNordertagPositionCreateModel(object):

    def __init__(self):
        self._address = None
        self._city = None
        self._district = None
        self._ext_info = None
        self._operate = None
        self._position_id = None
        self._province = None
        self._tag_position_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, NorderTagPositionExtInfo):
            self._ext_info = value
        else:
            self._ext_info = NorderTagPositionExtInfo.from_alipay_dict(value)
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def tag_position_name(self):
        return self._tag_position_name

    @tag_position_name.setter
    def tag_position_name(self, value):
        self._tag_position_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.tag_position_name:
            if hasattr(self.tag_position_name, 'to_alipay_dict'):
                params['tag_position_name'] = self.tag_position_name.to_alipay_dict()
            else:
                params['tag_position_name'] = self.tag_position_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordertagPositionCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'city' in d:
            o.city = d['city']
        if 'district' in d:
            o.district = d['district']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'operate' in d:
            o.operate = d['operate']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'province' in d:
            o.province = d['province']
        if 'tag_position_name' in d:
            o.tag_position_name = d['tag_position_name']
        return o


