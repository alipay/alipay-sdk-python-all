#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundIdentitypayOrganizationModifyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._latitude = None
        self._longitude = None
        self._member_count = None
        self._out_org_address = None
        self._out_org_area = None
        self._out_org_city = None
        self._out_org_id = None
        self._out_org_name = None
        self._out_org_province = None
        self._out_org_street = None
        self._product_code = None
        self._sub_biz_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
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
    def member_count(self):
        return self._member_count

    @member_count.setter
    def member_count(self, value):
        self._member_count = value
    @property
    def out_org_address(self):
        return self._out_org_address

    @out_org_address.setter
    def out_org_address(self, value):
        self._out_org_address = value
    @property
    def out_org_area(self):
        return self._out_org_area

    @out_org_area.setter
    def out_org_area(self, value):
        self._out_org_area = value
    @property
    def out_org_city(self):
        return self._out_org_city

    @out_org_city.setter
    def out_org_city(self, value):
        self._out_org_city = value
    @property
    def out_org_id(self):
        return self._out_org_id

    @out_org_id.setter
    def out_org_id(self, value):
        self._out_org_id = value
    @property
    def out_org_name(self):
        return self._out_org_name

    @out_org_name.setter
    def out_org_name(self, value):
        self._out_org_name = value
    @property
    def out_org_province(self):
        return self._out_org_province

    @out_org_province.setter
    def out_org_province(self, value):
        self._out_org_province = value
    @property
    def out_org_street(self):
        return self._out_org_street

    @out_org_street.setter
    def out_org_street(self, value):
        self._out_org_street = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
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
        if self.member_count:
            if hasattr(self.member_count, 'to_alipay_dict'):
                params['member_count'] = self.member_count.to_alipay_dict()
            else:
                params['member_count'] = self.member_count
        if self.out_org_address:
            if hasattr(self.out_org_address, 'to_alipay_dict'):
                params['out_org_address'] = self.out_org_address.to_alipay_dict()
            else:
                params['out_org_address'] = self.out_org_address
        if self.out_org_area:
            if hasattr(self.out_org_area, 'to_alipay_dict'):
                params['out_org_area'] = self.out_org_area.to_alipay_dict()
            else:
                params['out_org_area'] = self.out_org_area
        if self.out_org_city:
            if hasattr(self.out_org_city, 'to_alipay_dict'):
                params['out_org_city'] = self.out_org_city.to_alipay_dict()
            else:
                params['out_org_city'] = self.out_org_city
        if self.out_org_id:
            if hasattr(self.out_org_id, 'to_alipay_dict'):
                params['out_org_id'] = self.out_org_id.to_alipay_dict()
            else:
                params['out_org_id'] = self.out_org_id
        if self.out_org_name:
            if hasattr(self.out_org_name, 'to_alipay_dict'):
                params['out_org_name'] = self.out_org_name.to_alipay_dict()
            else:
                params['out_org_name'] = self.out_org_name
        if self.out_org_province:
            if hasattr(self.out_org_province, 'to_alipay_dict'):
                params['out_org_province'] = self.out_org_province.to_alipay_dict()
            else:
                params['out_org_province'] = self.out_org_province
        if self.out_org_street:
            if hasattr(self.out_org_street, 'to_alipay_dict'):
                params['out_org_street'] = self.out_org_street.to_alipay_dict()
            else:
                params['out_org_street'] = self.out_org_street
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundIdentitypayOrganizationModifyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'member_count' in d:
            o.member_count = d['member_count']
        if 'out_org_address' in d:
            o.out_org_address = d['out_org_address']
        if 'out_org_area' in d:
            o.out_org_area = d['out_org_area']
        if 'out_org_city' in d:
            o.out_org_city = d['out_org_city']
        if 'out_org_id' in d:
            o.out_org_id = d['out_org_id']
        if 'out_org_name' in d:
            o.out_org_name = d['out_org_name']
        if 'out_org_province' in d:
            o.out_org_province = d['out_org_province']
        if 'out_org_street' in d:
            o.out_org_street = d['out_org_street']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        return o


