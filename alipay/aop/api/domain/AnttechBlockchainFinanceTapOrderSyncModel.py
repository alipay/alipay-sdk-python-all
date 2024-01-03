#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceTapOrderSyncModel(object):

    def __init__(self):
        self._battery_life = None
        self._battery_special = None
        self._book_end_time = None
        self._book_start_time = None
        self._city_name = None
        self._complete_price = None
        self._complete_time = None
        self._create_time = None
        self._data_info = None
        self._detail_address = None
        self._district_name = None
        self._isv_order_id = None
        self._notify_type = None
        self._open_id = None
        self._order_id = None
        self._province_name = None
        self._status = None
        self._user_id = None

    @property
    def battery_life(self):
        return self._battery_life

    @battery_life.setter
    def battery_life(self, value):
        self._battery_life = value
    @property
    def battery_special(self):
        return self._battery_special

    @battery_special.setter
    def battery_special(self, value):
        self._battery_special = value
    @property
    def book_end_time(self):
        return self._book_end_time

    @book_end_time.setter
    def book_end_time(self, value):
        self._book_end_time = value
    @property
    def book_start_time(self):
        return self._book_start_time

    @book_start_time.setter
    def book_start_time(self, value):
        self._book_start_time = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def complete_price(self):
        return self._complete_price

    @complete_price.setter
    def complete_price(self, value):
        self._complete_price = value
    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def data_info(self):
        return self._data_info

    @data_info.setter
    def data_info(self, value):
        self._data_info = value
    @property
    def detail_address(self):
        return self._detail_address

    @detail_address.setter
    def detail_address(self, value):
        self._detail_address = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def isv_order_id(self):
        return self._isv_order_id

    @isv_order_id.setter
    def isv_order_id(self, value):
        self._isv_order_id = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.battery_life:
            if hasattr(self.battery_life, 'to_alipay_dict'):
                params['battery_life'] = self.battery_life.to_alipay_dict()
            else:
                params['battery_life'] = self.battery_life
        if self.battery_special:
            if hasattr(self.battery_special, 'to_alipay_dict'):
                params['battery_special'] = self.battery_special.to_alipay_dict()
            else:
                params['battery_special'] = self.battery_special
        if self.book_end_time:
            if hasattr(self.book_end_time, 'to_alipay_dict'):
                params['book_end_time'] = self.book_end_time.to_alipay_dict()
            else:
                params['book_end_time'] = self.book_end_time
        if self.book_start_time:
            if hasattr(self.book_start_time, 'to_alipay_dict'):
                params['book_start_time'] = self.book_start_time.to_alipay_dict()
            else:
                params['book_start_time'] = self.book_start_time
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.complete_price:
            if hasattr(self.complete_price, 'to_alipay_dict'):
                params['complete_price'] = self.complete_price.to_alipay_dict()
            else:
                params['complete_price'] = self.complete_price
        if self.complete_time:
            if hasattr(self.complete_time, 'to_alipay_dict'):
                params['complete_time'] = self.complete_time.to_alipay_dict()
            else:
                params['complete_time'] = self.complete_time
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.data_info:
            if hasattr(self.data_info, 'to_alipay_dict'):
                params['data_info'] = self.data_info.to_alipay_dict()
            else:
                params['data_info'] = self.data_info
        if self.detail_address:
            if hasattr(self.detail_address, 'to_alipay_dict'):
                params['detail_address'] = self.detail_address.to_alipay_dict()
            else:
                params['detail_address'] = self.detail_address
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.isv_order_id:
            if hasattr(self.isv_order_id, 'to_alipay_dict'):
                params['isv_order_id'] = self.isv_order_id.to_alipay_dict()
            else:
                params['isv_order_id'] = self.isv_order_id
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTapOrderSyncModel()
        if 'battery_life' in d:
            o.battery_life = d['battery_life']
        if 'battery_special' in d:
            o.battery_special = d['battery_special']
        if 'book_end_time' in d:
            o.book_end_time = d['book_end_time']
        if 'book_start_time' in d:
            o.book_start_time = d['book_start_time']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'complete_price' in d:
            o.complete_price = d['complete_price']
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'data_info' in d:
            o.data_info = d['data_info']
        if 'detail_address' in d:
            o.detail_address = d['detail_address']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'isv_order_id' in d:
            o.isv_order_id = d['isv_order_id']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


