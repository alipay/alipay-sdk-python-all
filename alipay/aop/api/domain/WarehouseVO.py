#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WarehouseVO(object):

    def __init__(self):
        self._address = None
        self._area_code = None
        self._area_name = None
        self._biz_status = None
        self._cainiao_code = None
        self._city_code = None
        self._city_name = None
        self._contact = None
        self._lat = None
        self._lon = None
        self._owner_id = None
        self._phone = None
        self._province_code = None
        self._province_name = None
        self._shop_id = None
        self._warehouse_code = None
        self._warehouse_name = None
        self._warehouse_type = None

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
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def cainiao_code(self):
        return self._cainiao_code

    @cainiao_code.setter
    def cainiao_code(self, value):
        self._cainiao_code = value
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
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value
    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value
    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value
    @property
    def warehouse_name(self):
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, value):
        self._warehouse_name = value
    @property
    def warehouse_type(self):
        return self._warehouse_type

    @warehouse_type.setter
    def warehouse_type(self, value):
        self._warehouse_type = value


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
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.cainiao_code:
            if hasattr(self.cainiao_code, 'to_alipay_dict'):
                params['cainiao_code'] = self.cainiao_code.to_alipay_dict()
            else:
                params['cainiao_code'] = self.cainiao_code
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
        if self.contact:
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.lat:
            if hasattr(self.lat, 'to_alipay_dict'):
                params['lat'] = self.lat.to_alipay_dict()
            else:
                params['lat'] = self.lat
        if self.lon:
            if hasattr(self.lon, 'to_alipay_dict'):
                params['lon'] = self.lon.to_alipay_dict()
            else:
                params['lon'] = self.lon
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        if self.warehouse_name:
            if hasattr(self.warehouse_name, 'to_alipay_dict'):
                params['warehouse_name'] = self.warehouse_name.to_alipay_dict()
            else:
                params['warehouse_name'] = self.warehouse_name
        if self.warehouse_type:
            if hasattr(self.warehouse_type, 'to_alipay_dict'):
                params['warehouse_type'] = self.warehouse_type.to_alipay_dict()
            else:
                params['warehouse_type'] = self.warehouse_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WarehouseVO()
        if 'address' in d:
            o.address = d['address']
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'cainiao_code' in d:
            o.cainiao_code = d['cainiao_code']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'contact' in d:
            o.contact = d['contact']
        if 'lat' in d:
            o.lat = d['lat']
        if 'lon' in d:
            o.lon = d['lon']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'phone' in d:
            o.phone = d['phone']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        if 'warehouse_name' in d:
            o.warehouse_name = d['warehouse_name']
        if 'warehouse_type' in d:
            o.warehouse_type = d['warehouse_type']
        return o


