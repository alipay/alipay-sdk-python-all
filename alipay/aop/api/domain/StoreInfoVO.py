#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessDateDTO import BusinessDateDTO


class StoreInfoVO(object):

    def __init__(self):
        self._address = None
        self._business_category = None
        self._business_dates = None
        self._city_name = None
        self._contact_tel = None
        self._delivery_way = None
        self._env_img_list = None
        self._facade_img = None
        self._gmt_create = None
        self._gmt_modified = None
        self._latitude = None
        self._longitude = None
        self._mi_code = None
        self._mi_name = None
        self._mi_state = None
        self._status = None
        self._store_code = None
        self._store_logo = None
        self._store_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def business_category(self):
        return self._business_category

    @business_category.setter
    def business_category(self, value):
        self._business_category = value
    @property
    def business_dates(self):
        return self._business_dates

    @business_dates.setter
    def business_dates(self, value):
        if isinstance(value, BusinessDateDTO):
            self._business_dates = value
        else:
            self._business_dates = BusinessDateDTO.from_alipay_dict(value)
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def contact_tel(self):
        return self._contact_tel

    @contact_tel.setter
    def contact_tel(self, value):
        self._contact_tel = value
    @property
    def delivery_way(self):
        return self._delivery_way

    @delivery_way.setter
    def delivery_way(self, value):
        self._delivery_way = value
    @property
    def env_img_list(self):
        return self._env_img_list

    @env_img_list.setter
    def env_img_list(self, value):
        if isinstance(value, list):
            self._env_img_list = list()
            for i in value:
                self._env_img_list.append(i)
    @property
    def facade_img(self):
        return self._facade_img

    @facade_img.setter
    def facade_img(self, value):
        self._facade_img = value
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
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mi_code(self):
        return self._mi_code

    @mi_code.setter
    def mi_code(self, value):
        self._mi_code = value
    @property
    def mi_name(self):
        return self._mi_name

    @mi_name.setter
    def mi_name(self, value):
        self._mi_name = value
    @property
    def mi_state(self):
        return self._mi_state

    @mi_state.setter
    def mi_state(self, value):
        self._mi_state = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value
    @property
    def store_logo(self):
        return self._store_logo

    @store_logo.setter
    def store_logo(self, value):
        self._store_logo = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.business_category:
            if hasattr(self.business_category, 'to_alipay_dict'):
                params['business_category'] = self.business_category.to_alipay_dict()
            else:
                params['business_category'] = self.business_category
        if self.business_dates:
            if hasattr(self.business_dates, 'to_alipay_dict'):
                params['business_dates'] = self.business_dates.to_alipay_dict()
            else:
                params['business_dates'] = self.business_dates
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.contact_tel:
            if hasattr(self.contact_tel, 'to_alipay_dict'):
                params['contact_tel'] = self.contact_tel.to_alipay_dict()
            else:
                params['contact_tel'] = self.contact_tel
        if self.delivery_way:
            if hasattr(self.delivery_way, 'to_alipay_dict'):
                params['delivery_way'] = self.delivery_way.to_alipay_dict()
            else:
                params['delivery_way'] = self.delivery_way
        if self.env_img_list:
            if isinstance(self.env_img_list, list):
                for i in range(0, len(self.env_img_list)):
                    element = self.env_img_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.env_img_list[i] = element.to_alipay_dict()
            if hasattr(self.env_img_list, 'to_alipay_dict'):
                params['env_img_list'] = self.env_img_list.to_alipay_dict()
            else:
                params['env_img_list'] = self.env_img_list
        if self.facade_img:
            if hasattr(self.facade_img, 'to_alipay_dict'):
                params['facade_img'] = self.facade_img.to_alipay_dict()
            else:
                params['facade_img'] = self.facade_img
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
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mi_code:
            if hasattr(self.mi_code, 'to_alipay_dict'):
                params['mi_code'] = self.mi_code.to_alipay_dict()
            else:
                params['mi_code'] = self.mi_code
        if self.mi_name:
            if hasattr(self.mi_name, 'to_alipay_dict'):
                params['mi_name'] = self.mi_name.to_alipay_dict()
            else:
                params['mi_name'] = self.mi_name
        if self.mi_state:
            if hasattr(self.mi_state, 'to_alipay_dict'):
                params['mi_state'] = self.mi_state.to_alipay_dict()
            else:
                params['mi_state'] = self.mi_state
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        if self.store_logo:
            if hasattr(self.store_logo, 'to_alipay_dict'):
                params['store_logo'] = self.store_logo.to_alipay_dict()
            else:
                params['store_logo'] = self.store_logo
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StoreInfoVO()
        if 'address' in d:
            o.address = d['address']
        if 'business_category' in d:
            o.business_category = d['business_category']
        if 'business_dates' in d:
            o.business_dates = d['business_dates']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'contact_tel' in d:
            o.contact_tel = d['contact_tel']
        if 'delivery_way' in d:
            o.delivery_way = d['delivery_way']
        if 'env_img_list' in d:
            o.env_img_list = d['env_img_list']
        if 'facade_img' in d:
            o.facade_img = d['facade_img']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mi_code' in d:
            o.mi_code = d['mi_code']
        if 'mi_name' in d:
            o.mi_name = d['mi_name']
        if 'mi_state' in d:
            o.mi_state = d['mi_state']
        if 'status' in d:
            o.status = d['status']
        if 'store_code' in d:
            o.store_code = d['store_code']
        if 'store_logo' in d:
            o.store_logo = d['store_logo']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


