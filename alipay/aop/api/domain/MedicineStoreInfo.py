#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicineTagInfo import MedicineTagInfo


class MedicineStoreInfo(object):

    def __init__(self):
        self._address = None
        self._app_store_id = None
        self._city_code = None
        self._city_name = None
        self._distance = None
        self._free_shipping_price = None
        self._latitude = None
        self._logo_image = None
        self._longitude = None
        self._medical_org_no = None
        self._province_code = None
        self._province_name = None
        self._shipping_fee = None
        self._shipping_price = None
        self._store_name = None
        self._tag_list = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def app_store_id(self):
        return self._app_store_id

    @app_store_id.setter
    def app_store_id(self, value):
        self._app_store_id = value
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
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def free_shipping_price(self):
        return self._free_shipping_price

    @free_shipping_price.setter
    def free_shipping_price(self, value):
        self._free_shipping_price = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logo_image(self):
        return self._logo_image

    @logo_image.setter
    def logo_image(self, value):
        self._logo_image = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def medical_org_no(self):
        return self._medical_org_no

    @medical_org_no.setter
    def medical_org_no(self, value):
        self._medical_org_no = value
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
    def shipping_fee(self):
        return self._shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        self._shipping_fee = value
    @property
    def shipping_price(self):
        return self._shipping_price

    @shipping_price.setter
    def shipping_price(self, value):
        self._shipping_price = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                if isinstance(i, MedicineTagInfo):
                    self._tag_list.append(i)
                else:
                    self._tag_list.append(MedicineTagInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.app_store_id:
            if hasattr(self.app_store_id, 'to_alipay_dict'):
                params['app_store_id'] = self.app_store_id.to_alipay_dict()
            else:
                params['app_store_id'] = self.app_store_id
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
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.free_shipping_price:
            if hasattr(self.free_shipping_price, 'to_alipay_dict'):
                params['free_shipping_price'] = self.free_shipping_price.to_alipay_dict()
            else:
                params['free_shipping_price'] = self.free_shipping_price
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logo_image:
            if hasattr(self.logo_image, 'to_alipay_dict'):
                params['logo_image'] = self.logo_image.to_alipay_dict()
            else:
                params['logo_image'] = self.logo_image
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.medical_org_no:
            if hasattr(self.medical_org_no, 'to_alipay_dict'):
                params['medical_org_no'] = self.medical_org_no.to_alipay_dict()
            else:
                params['medical_org_no'] = self.medical_org_no
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
        if self.shipping_fee:
            if hasattr(self.shipping_fee, 'to_alipay_dict'):
                params['shipping_fee'] = self.shipping_fee.to_alipay_dict()
            else:
                params['shipping_fee'] = self.shipping_fee
        if self.shipping_price:
            if hasattr(self.shipping_price, 'to_alipay_dict'):
                params['shipping_price'] = self.shipping_price.to_alipay_dict()
            else:
                params['shipping_price'] = self.shipping_price
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicineStoreInfo()
        if 'address' in d:
            o.address = d['address']
        if 'app_store_id' in d:
            o.app_store_id = d['app_store_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'distance' in d:
            o.distance = d['distance']
        if 'free_shipping_price' in d:
            o.free_shipping_price = d['free_shipping_price']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logo_image' in d:
            o.logo_image = d['logo_image']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'medical_org_no' in d:
            o.medical_org_no = d['medical_org_no']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'shipping_fee' in d:
            o.shipping_fee = d['shipping_fee']
        if 'shipping_price' in d:
            o.shipping_price = d['shipping_price']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        return o


