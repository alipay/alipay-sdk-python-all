#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsIncentivecodeActiveSyncModel(object):

    def __init__(self):
        self._active_area = None
        self._active_city = None
        self._active_code_open_id = None
        self._active_code_user_id = None
        self._active_detail_address = None
        self._active_latitude = None
        self._active_longitude = None
        self._active_out_shop_id = None
        self._active_province = None
        self._active_shop_name = None
        self._active_street = None
        self._active_time = None
        self._active_type = None
        self._incentive_code = None
        self._logistics_code = None
        self._material_type = None

    @property
    def active_area(self):
        return self._active_area

    @active_area.setter
    def active_area(self, value):
        self._active_area = value
    @property
    def active_city(self):
        return self._active_city

    @active_city.setter
    def active_city(self, value):
        self._active_city = value
    @property
    def active_code_open_id(self):
        return self._active_code_open_id

    @active_code_open_id.setter
    def active_code_open_id(self, value):
        self._active_code_open_id = value
    @property
    def active_code_user_id(self):
        return self._active_code_user_id

    @active_code_user_id.setter
    def active_code_user_id(self, value):
        self._active_code_user_id = value
    @property
    def active_detail_address(self):
        return self._active_detail_address

    @active_detail_address.setter
    def active_detail_address(self, value):
        self._active_detail_address = value
    @property
    def active_latitude(self):
        return self._active_latitude

    @active_latitude.setter
    def active_latitude(self, value):
        self._active_latitude = value
    @property
    def active_longitude(self):
        return self._active_longitude

    @active_longitude.setter
    def active_longitude(self, value):
        self._active_longitude = value
    @property
    def active_out_shop_id(self):
        return self._active_out_shop_id

    @active_out_shop_id.setter
    def active_out_shop_id(self, value):
        self._active_out_shop_id = value
    @property
    def active_province(self):
        return self._active_province

    @active_province.setter
    def active_province(self, value):
        self._active_province = value
    @property
    def active_shop_name(self):
        return self._active_shop_name

    @active_shop_name.setter
    def active_shop_name(self, value):
        self._active_shop_name = value
    @property
    def active_street(self):
        return self._active_street

    @active_street.setter
    def active_street(self, value):
        self._active_street = value
    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def active_type(self):
        return self._active_type

    @active_type.setter
    def active_type(self, value):
        self._active_type = value
    @property
    def incentive_code(self):
        return self._incentive_code

    @incentive_code.setter
    def incentive_code(self, value):
        self._incentive_code = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_area:
            if hasattr(self.active_area, 'to_alipay_dict'):
                params['active_area'] = self.active_area.to_alipay_dict()
            else:
                params['active_area'] = self.active_area
        if self.active_city:
            if hasattr(self.active_city, 'to_alipay_dict'):
                params['active_city'] = self.active_city.to_alipay_dict()
            else:
                params['active_city'] = self.active_city
        if self.active_code_open_id:
            if hasattr(self.active_code_open_id, 'to_alipay_dict'):
                params['active_code_open_id'] = self.active_code_open_id.to_alipay_dict()
            else:
                params['active_code_open_id'] = self.active_code_open_id
        if self.active_code_user_id:
            if hasattr(self.active_code_user_id, 'to_alipay_dict'):
                params['active_code_user_id'] = self.active_code_user_id.to_alipay_dict()
            else:
                params['active_code_user_id'] = self.active_code_user_id
        if self.active_detail_address:
            if hasattr(self.active_detail_address, 'to_alipay_dict'):
                params['active_detail_address'] = self.active_detail_address.to_alipay_dict()
            else:
                params['active_detail_address'] = self.active_detail_address
        if self.active_latitude:
            if hasattr(self.active_latitude, 'to_alipay_dict'):
                params['active_latitude'] = self.active_latitude.to_alipay_dict()
            else:
                params['active_latitude'] = self.active_latitude
        if self.active_longitude:
            if hasattr(self.active_longitude, 'to_alipay_dict'):
                params['active_longitude'] = self.active_longitude.to_alipay_dict()
            else:
                params['active_longitude'] = self.active_longitude
        if self.active_out_shop_id:
            if hasattr(self.active_out_shop_id, 'to_alipay_dict'):
                params['active_out_shop_id'] = self.active_out_shop_id.to_alipay_dict()
            else:
                params['active_out_shop_id'] = self.active_out_shop_id
        if self.active_province:
            if hasattr(self.active_province, 'to_alipay_dict'):
                params['active_province'] = self.active_province.to_alipay_dict()
            else:
                params['active_province'] = self.active_province
        if self.active_shop_name:
            if hasattr(self.active_shop_name, 'to_alipay_dict'):
                params['active_shop_name'] = self.active_shop_name.to_alipay_dict()
            else:
                params['active_shop_name'] = self.active_shop_name
        if self.active_street:
            if hasattr(self.active_street, 'to_alipay_dict'):
                params['active_street'] = self.active_street.to_alipay_dict()
            else:
                params['active_street'] = self.active_street
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.active_type:
            if hasattr(self.active_type, 'to_alipay_dict'):
                params['active_type'] = self.active_type.to_alipay_dict()
            else:
                params['active_type'] = self.active_type
        if self.incentive_code:
            if hasattr(self.incentive_code, 'to_alipay_dict'):
                params['incentive_code'] = self.incentive_code.to_alipay_dict()
            else:
                params['incentive_code'] = self.incentive_code
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsIncentivecodeActiveSyncModel()
        if 'active_area' in d:
            o.active_area = d['active_area']
        if 'active_city' in d:
            o.active_city = d['active_city']
        if 'active_code_open_id' in d:
            o.active_code_open_id = d['active_code_open_id']
        if 'active_code_user_id' in d:
            o.active_code_user_id = d['active_code_user_id']
        if 'active_detail_address' in d:
            o.active_detail_address = d['active_detail_address']
        if 'active_latitude' in d:
            o.active_latitude = d['active_latitude']
        if 'active_longitude' in d:
            o.active_longitude = d['active_longitude']
        if 'active_out_shop_id' in d:
            o.active_out_shop_id = d['active_out_shop_id']
        if 'active_province' in d:
            o.active_province = d['active_province']
        if 'active_shop_name' in d:
            o.active_shop_name = d['active_shop_name']
        if 'active_street' in d:
            o.active_street = d['active_street']
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'active_type' in d:
            o.active_type = d['active_type']
        if 'incentive_code' in d:
            o.incentive_code = d['incentive_code']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'material_type' in d:
            o.material_type = d['material_type']
        return o


