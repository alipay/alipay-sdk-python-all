#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderItem(object):

    def __init__(self):
        self._address = None
        self._brand_name = None
        self._category = None
        self._city = None
        self._city_code = None
        self._commodity_id = None
        self._contacts = None
        self._creator = None
        self._expire_date = None
        self._merchant_name = None
        self._merchant_pid = None
        self._mini_app_id = None
        self._mini_app_name = None
        self._online_time = None
        self._order_status = None
        self._phone_no = None
        self._province = None
        self._shop_id = None
        self._shop_name = None
        self._shop_status = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def commodity_id(self):
        return self._commodity_id

    @commodity_id.setter
    def commodity_id(self, value):
        self._commodity_id = value
    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        self._contacts = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def online_time(self):
        return self._online_time

    @online_time.setter
    def online_time(self, value):
        self._online_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
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
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.commodity_id:
            if hasattr(self.commodity_id, 'to_alipay_dict'):
                params['commodity_id'] = self.commodity_id.to_alipay_dict()
            else:
                params['commodity_id'] = self.commodity_id
        if self.contacts:
            if hasattr(self.contacts, 'to_alipay_dict'):
                params['contacts'] = self.contacts.to_alipay_dict()
            else:
                params['contacts'] = self.contacts
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.online_time:
            if hasattr(self.online_time, 'to_alipay_dict'):
                params['online_time'] = self.online_time.to_alipay_dict()
            else:
                params['online_time'] = self.online_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
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
        o = OrderItem()
        if 'address' in d:
            o.address = d['address']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'category' in d:
            o.category = d['category']
        if 'city' in d:
            o.city = d['city']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'commodity_id' in d:
            o.commodity_id = d['commodity_id']
        if 'contacts' in d:
            o.contacts = d['contacts']
        if 'creator' in d:
            o.creator = d['creator']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'online_time' in d:
            o.online_time = d['online_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'province' in d:
            o.province = d['province']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        if 'status' in d:
            o.status = d['status']
        return o


