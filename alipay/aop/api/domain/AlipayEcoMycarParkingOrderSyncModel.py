#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingOrderSyncModel(object):

    def __init__(self):
        self._agent_pid = None
        self._car_number = None
        self._card_number = None
        self._in_duration = None
        self._in_time = None
        self._order_no = None
        self._order_status = None
        self._order_time = None
        self._out_order_no = None
        self._out_parking_id = None
        self._out_time = None
        self._parking_id = None
        self._parking_name = None
        self._parking_record_id = None
        self._pay_money = None
        self._pay_scene = None
        self._pay_time = None
        self._pay_type = None
        self._smid = None
        self._user_id = None

    @property
    def agent_pid(self):
        return self._agent_pid

    @agent_pid.setter
    def agent_pid(self, value):
        self._agent_pid = value
    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, value):
        self._card_number = value
    @property
    def in_duration(self):
        return self._in_duration

    @in_duration.setter
    def in_duration(self, value):
        self._in_duration = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_parking_id(self):
        return self._out_parking_id

    @out_parking_id.setter
    def out_parking_id(self, value):
        self._out_parking_id = value
    @property
    def out_time(self):
        return self._out_time

    @out_time.setter
    def out_time(self, value):
        self._out_time = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def parking_name(self):
        return self._parking_name

    @parking_name.setter
    def parking_name(self, value):
        self._parking_name = value
    @property
    def parking_record_id(self):
        return self._parking_record_id

    @parking_record_id.setter
    def parking_record_id(self, value):
        self._parking_record_id = value
    @property
    def pay_money(self):
        return self._pay_money

    @pay_money.setter
    def pay_money(self, value):
        self._pay_money = value
    @property
    def pay_scene(self):
        return self._pay_scene

    @pay_scene.setter
    def pay_scene(self, value):
        self._pay_scene = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_pid:
            if hasattr(self.agent_pid, 'to_alipay_dict'):
                params['agent_pid'] = self.agent_pid.to_alipay_dict()
            else:
                params['agent_pid'] = self.agent_pid
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.card_number:
            if hasattr(self.card_number, 'to_alipay_dict'):
                params['card_number'] = self.card_number.to_alipay_dict()
            else:
                params['card_number'] = self.card_number
        if self.in_duration:
            if hasattr(self.in_duration, 'to_alipay_dict'):
                params['in_duration'] = self.in_duration.to_alipay_dict()
            else:
                params['in_duration'] = self.in_duration
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_parking_id:
            if hasattr(self.out_parking_id, 'to_alipay_dict'):
                params['out_parking_id'] = self.out_parking_id.to_alipay_dict()
            else:
                params['out_parking_id'] = self.out_parking_id
        if self.out_time:
            if hasattr(self.out_time, 'to_alipay_dict'):
                params['out_time'] = self.out_time.to_alipay_dict()
            else:
                params['out_time'] = self.out_time
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.parking_name:
            if hasattr(self.parking_name, 'to_alipay_dict'):
                params['parking_name'] = self.parking_name.to_alipay_dict()
            else:
                params['parking_name'] = self.parking_name
        if self.parking_record_id:
            if hasattr(self.parking_record_id, 'to_alipay_dict'):
                params['parking_record_id'] = self.parking_record_id.to_alipay_dict()
            else:
                params['parking_record_id'] = self.parking_record_id
        if self.pay_money:
            if hasattr(self.pay_money, 'to_alipay_dict'):
                params['pay_money'] = self.pay_money.to_alipay_dict()
            else:
                params['pay_money'] = self.pay_money
        if self.pay_scene:
            if hasattr(self.pay_scene, 'to_alipay_dict'):
                params['pay_scene'] = self.pay_scene.to_alipay_dict()
            else:
                params['pay_scene'] = self.pay_scene
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
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
        o = AlipayEcoMycarParkingOrderSyncModel()
        if 'agent_pid' in d:
            o.agent_pid = d['agent_pid']
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'card_number' in d:
            o.card_number = d['card_number']
        if 'in_duration' in d:
            o.in_duration = d['in_duration']
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_parking_id' in d:
            o.out_parking_id = d['out_parking_id']
        if 'out_time' in d:
            o.out_time = d['out_time']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'parking_name' in d:
            o.parking_name = d['parking_name']
        if 'parking_record_id' in d:
            o.parking_record_id = d['parking_record_id']
        if 'pay_money' in d:
            o.pay_money = d['pay_money']
        if 'pay_scene' in d:
            o.pay_scene = d['pay_scene']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


