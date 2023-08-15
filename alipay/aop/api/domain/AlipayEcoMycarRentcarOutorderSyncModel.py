#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarRentcarOutorderSyncModel(object):

    def __init__(self):
        self._carlife_vehicle_id = None
        self._drop_off_store_name = None
        self._drop_off_time = None
        self._order_id = None
        self._order_status = None
        self._out_order_id = None
        self._out_order_time = None
        self._pick_up_store_name = None
        self._pick_up_time = None
        self._total_amount = None
        self._user_id = None
        self._user_open_id = None

    @property
    def carlife_vehicle_id(self):
        return self._carlife_vehicle_id

    @carlife_vehicle_id.setter
    def carlife_vehicle_id(self, value):
        self._carlife_vehicle_id = value
    @property
    def drop_off_store_name(self):
        return self._drop_off_store_name

    @drop_off_store_name.setter
    def drop_off_store_name(self, value):
        self._drop_off_store_name = value
    @property
    def drop_off_time(self):
        return self._drop_off_time

    @drop_off_time.setter
    def drop_off_time(self, value):
        self._drop_off_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_order_time(self):
        return self._out_order_time

    @out_order_time.setter
    def out_order_time(self, value):
        self._out_order_time = value
    @property
    def pick_up_store_name(self):
        return self._pick_up_store_name

    @pick_up_store_name.setter
    def pick_up_store_name(self, value):
        self._pick_up_store_name = value
    @property
    def pick_up_time(self):
        return self._pick_up_time

    @pick_up_time.setter
    def pick_up_time(self, value):
        self._pick_up_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.carlife_vehicle_id:
            if hasattr(self.carlife_vehicle_id, 'to_alipay_dict'):
                params['carlife_vehicle_id'] = self.carlife_vehicle_id.to_alipay_dict()
            else:
                params['carlife_vehicle_id'] = self.carlife_vehicle_id
        if self.drop_off_store_name:
            if hasattr(self.drop_off_store_name, 'to_alipay_dict'):
                params['drop_off_store_name'] = self.drop_off_store_name.to_alipay_dict()
            else:
                params['drop_off_store_name'] = self.drop_off_store_name
        if self.drop_off_time:
            if hasattr(self.drop_off_time, 'to_alipay_dict'):
                params['drop_off_time'] = self.drop_off_time.to_alipay_dict()
            else:
                params['drop_off_time'] = self.drop_off_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_order_time:
            if hasattr(self.out_order_time, 'to_alipay_dict'):
                params['out_order_time'] = self.out_order_time.to_alipay_dict()
            else:
                params['out_order_time'] = self.out_order_time
        if self.pick_up_store_name:
            if hasattr(self.pick_up_store_name, 'to_alipay_dict'):
                params['pick_up_store_name'] = self.pick_up_store_name.to_alipay_dict()
            else:
                params['pick_up_store_name'] = self.pick_up_store_name
        if self.pick_up_time:
            if hasattr(self.pick_up_time, 'to_alipay_dict'):
                params['pick_up_time'] = self.pick_up_time.to_alipay_dict()
            else:
                params['pick_up_time'] = self.pick_up_time
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarRentcarOutorderSyncModel()
        if 'carlife_vehicle_id' in d:
            o.carlife_vehicle_id = d['carlife_vehicle_id']
        if 'drop_off_store_name' in d:
            o.drop_off_store_name = d['drop_off_store_name']
        if 'drop_off_time' in d:
            o.drop_off_time = d['drop_off_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_order_time' in d:
            o.out_order_time = d['out_order_time']
        if 'pick_up_store_name' in d:
            o.pick_up_store_name = d['pick_up_store_name']
        if 'pick_up_time' in d:
            o.pick_up_time = d['pick_up_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


