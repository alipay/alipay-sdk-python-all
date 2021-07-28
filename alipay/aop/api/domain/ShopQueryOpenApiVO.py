#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.ShopBusinessTime import ShopBusinessTime


class ShopQueryOpenApiVO(object):

    def __init__(self):
        self._business_address = None
        self._business_time = None
        self._contact_mobile = None
        self._contact_phone = None
        self._shop_category = None
        self._shop_id = None
        self._shop_name = None
        self._shop_status = None
        self._shop_type = None
        self._store_id = None

    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, AddressInfo):
            self._business_address = value
        else:
            self._business_address = AddressInfo.from_alipay_dict(value)
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, ShopBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(ShopBusinessTime.from_alipay_dict(i))
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopQueryOpenApiVO()
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


