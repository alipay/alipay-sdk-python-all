#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizAreaDTO(object):

    def __init__(self):
        self._address = None
        self._biz_area_code = None
        self._biz_area_english_name = None
        self._biz_area_name = None
        self._biz_area_type = None
        self._biz_area_version = None
        self._city_code = None
        self._city_name = None
        self._coords = None
        self._country_code = None
        self._country_name = None
        self._description = None
        self._ext_info = None
        self._ge_biz_area_code = None
        self._gmt_create = None
        self._gmt_modified = None
        self._latitude = None
        self._logo = None
        self._longitude = None
        self._operator = None
        self._origin_flag = None
        self._shop_count = None
        self._show_name = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_area_code(self):
        return self._biz_area_code

    @biz_area_code.setter
    def biz_area_code(self, value):
        self._biz_area_code = value
    @property
    def biz_area_english_name(self):
        return self._biz_area_english_name

    @biz_area_english_name.setter
    def biz_area_english_name(self, value):
        self._biz_area_english_name = value
    @property
    def biz_area_name(self):
        return self._biz_area_name

    @biz_area_name.setter
    def biz_area_name(self, value):
        self._biz_area_name = value
    @property
    def biz_area_type(self):
        return self._biz_area_type

    @biz_area_type.setter
    def biz_area_type(self, value):
        self._biz_area_type = value
    @property
    def biz_area_version(self):
        return self._biz_area_version

    @biz_area_version.setter
    def biz_area_version(self, value):
        self._biz_area_version = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value
    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, value):
        self._country_code = value
    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, value):
        self._country_name = value
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
    def ge_biz_area_code(self):
        return self._ge_biz_area_code

    @ge_biz_area_code.setter
    def ge_biz_area_code(self, value):
        self._ge_biz_area_code = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def origin_flag(self):
        return self._origin_flag

    @origin_flag.setter
    def origin_flag(self, value):
        self._origin_flag = value
    @property
    def shop_count(self):
        return self._shop_count

    @shop_count.setter
    def shop_count(self, value):
        self._shop_count = value
    @property
    def show_name(self):
        return self._show_name

    @show_name.setter
    def show_name(self, value):
        self._show_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_area_code:
            if hasattr(self.biz_area_code, 'to_alipay_dict'):
                params['biz_area_code'] = self.biz_area_code.to_alipay_dict()
            else:
                params['biz_area_code'] = self.biz_area_code
        if self.biz_area_english_name:
            if hasattr(self.biz_area_english_name, 'to_alipay_dict'):
                params['biz_area_english_name'] = self.biz_area_english_name.to_alipay_dict()
            else:
                params['biz_area_english_name'] = self.biz_area_english_name
        if self.biz_area_name:
            if hasattr(self.biz_area_name, 'to_alipay_dict'):
                params['biz_area_name'] = self.biz_area_name.to_alipay_dict()
            else:
                params['biz_area_name'] = self.biz_area_name
        if self.biz_area_type:
            if hasattr(self.biz_area_type, 'to_alipay_dict'):
                params['biz_area_type'] = self.biz_area_type.to_alipay_dict()
            else:
                params['biz_area_type'] = self.biz_area_type
        if self.biz_area_version:
            if hasattr(self.biz_area_version, 'to_alipay_dict'):
                params['biz_area_version'] = self.biz_area_version.to_alipay_dict()
            else:
                params['biz_area_version'] = self.biz_area_version
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.coords:
            if hasattr(self.coords, 'to_alipay_dict'):
                params['coords'] = self.coords.to_alipay_dict()
            else:
                params['coords'] = self.coords
        if self.country_code:
            if hasattr(self.country_code, 'to_alipay_dict'):
                params['country_code'] = self.country_code.to_alipay_dict()
            else:
                params['country_code'] = self.country_code
        if self.country_name:
            if hasattr(self.country_name, 'to_alipay_dict'):
                params['country_name'] = self.country_name.to_alipay_dict()
            else:
                params['country_name'] = self.country_name
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
        if self.ge_biz_area_code:
            if hasattr(self.ge_biz_area_code, 'to_alipay_dict'):
                params['ge_biz_area_code'] = self.ge_biz_area_code.to_alipay_dict()
            else:
                params['ge_biz_area_code'] = self.ge_biz_area_code
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.origin_flag:
            if hasattr(self.origin_flag, 'to_alipay_dict'):
                params['origin_flag'] = self.origin_flag.to_alipay_dict()
            else:
                params['origin_flag'] = self.origin_flag
        if self.shop_count:
            if hasattr(self.shop_count, 'to_alipay_dict'):
                params['shop_count'] = self.shop_count.to_alipay_dict()
            else:
                params['shop_count'] = self.shop_count
        if self.show_name:
            if hasattr(self.show_name, 'to_alipay_dict'):
                params['show_name'] = self.show_name.to_alipay_dict()
            else:
                params['show_name'] = self.show_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizAreaDTO()
        if 'address' in d:
            o.address = d['address']
        if 'biz_area_code' in d:
            o.biz_area_code = d['biz_area_code']
        if 'biz_area_english_name' in d:
            o.biz_area_english_name = d['biz_area_english_name']
        if 'biz_area_name' in d:
            o.biz_area_name = d['biz_area_name']
        if 'biz_area_type' in d:
            o.biz_area_type = d['biz_area_type']
        if 'biz_area_version' in d:
            o.biz_area_version = d['biz_area_version']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'coords' in d:
            o.coords = d['coords']
        if 'country_code' in d:
            o.country_code = d['country_code']
        if 'country_name' in d:
            o.country_name = d['country_name']
        if 'description' in d:
            o.description = d['description']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'ge_biz_area_code' in d:
            o.ge_biz_area_code = d['ge_biz_area_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logo' in d:
            o.logo = d['logo']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'operator' in d:
            o.operator = d['operator']
        if 'origin_flag' in d:
            o.origin_flag = d['origin_flag']
        if 'shop_count' in d:
            o.shop_count = d['shop_count']
        if 'show_name' in d:
            o.show_name = d['show_name']
        if 'status' in d:
            o.status = d['status']
        return o


