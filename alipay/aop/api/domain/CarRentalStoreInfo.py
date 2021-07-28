#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessHoursInfo import BusinessHoursInfo
from alipay.aop.api.domain.StoreAddressInfo import StoreAddressInfo
from alipay.aop.api.domain.ExtraInfo import ExtraInfo


class CarRentalStoreInfo(object):

    def __init__(self):
        self._business_hours = None
        self._shop_id = None
        self._store_address_info = None
        self._store_city = None
        self._store_extra_info = None
        self._store_id = None
        self._store_name = None
        self._store_phone = None

    @property
    def business_hours(self):
        return self._business_hours

    @business_hours.setter
    def business_hours(self, value):
        if isinstance(value, BusinessHoursInfo):
            self._business_hours = value
        else:
            self._business_hours = BusinessHoursInfo.from_alipay_dict(value)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_address_info(self):
        return self._store_address_info

    @store_address_info.setter
    def store_address_info(self, value):
        if isinstance(value, StoreAddressInfo):
            self._store_address_info = value
        else:
            self._store_address_info = StoreAddressInfo.from_alipay_dict(value)
    @property
    def store_city(self):
        return self._store_city

    @store_city.setter
    def store_city(self, value):
        self._store_city = value
    @property
    def store_extra_info(self):
        return self._store_extra_info

    @store_extra_info.setter
    def store_extra_info(self, value):
        if isinstance(value, list):
            self._store_extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._store_extra_info.append(i)
                else:
                    self._store_extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def store_phone(self):
        return self._store_phone

    @store_phone.setter
    def store_phone(self, value):
        self._store_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_hours:
            if hasattr(self.business_hours, 'to_alipay_dict'):
                params['business_hours'] = self.business_hours.to_alipay_dict()
            else:
                params['business_hours'] = self.business_hours
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_address_info:
            if hasattr(self.store_address_info, 'to_alipay_dict'):
                params['store_address_info'] = self.store_address_info.to_alipay_dict()
            else:
                params['store_address_info'] = self.store_address_info
        if self.store_city:
            if hasattr(self.store_city, 'to_alipay_dict'):
                params['store_city'] = self.store_city.to_alipay_dict()
            else:
                params['store_city'] = self.store_city
        if self.store_extra_info:
            if isinstance(self.store_extra_info, list):
                for i in range(0, len(self.store_extra_info)):
                    element = self.store_extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.store_extra_info[i] = element.to_alipay_dict()
            if hasattr(self.store_extra_info, 'to_alipay_dict'):
                params['store_extra_info'] = self.store_extra_info.to_alipay_dict()
            else:
                params['store_extra_info'] = self.store_extra_info
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.store_phone:
            if hasattr(self.store_phone, 'to_alipay_dict'):
                params['store_phone'] = self.store_phone.to_alipay_dict()
            else:
                params['store_phone'] = self.store_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarRentalStoreInfo()
        if 'business_hours' in d:
            o.business_hours = d['business_hours']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_address_info' in d:
            o.store_address_info = d['store_address_info']
        if 'store_city' in d:
            o.store_city = d['store_city']
        if 'store_extra_info' in d:
            o.store_extra_info = d['store_extra_info']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'store_phone' in d:
            o.store_phone = d['store_phone']
        return o


