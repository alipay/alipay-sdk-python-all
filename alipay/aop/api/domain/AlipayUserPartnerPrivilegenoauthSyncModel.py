#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPartnerPrivilegenoauthSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._butler_use_flag = None
        self._car_use_flag = None
        self._city = None
        self._compartment_number = None
        self._current_count = None
        self._grade = None
        self._grade_expired_time = None
        self._max_count = None
        self._open_id = None
        self._out_biz_no = None
        self._out_partner_id = None
        self._phone_number = None
        self._privilege_id = None
        self._register_channel = None
        self._scene = None
        self._service_phone = None
        self._station = None
        self._status = None
        self._title = None
        self._train_number = None
        self._trans_quantum = None
        self._travel_time = None
        self._user_id = None
        self._user_name = None
        self._user_pay_amount = None
        self._vendor = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def butler_use_flag(self):
        return self._butler_use_flag

    @butler_use_flag.setter
    def butler_use_flag(self, value):
        self._butler_use_flag = value
    @property
    def car_use_flag(self):
        return self._car_use_flag

    @car_use_flag.setter
    def car_use_flag(self, value):
        self._car_use_flag = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def compartment_number(self):
        return self._compartment_number

    @compartment_number.setter
    def compartment_number(self, value):
        self._compartment_number = value
    @property
    def current_count(self):
        return self._current_count

    @current_count.setter
    def current_count(self, value):
        self._current_count = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def grade_expired_time(self):
        return self._grade_expired_time

    @grade_expired_time.setter
    def grade_expired_time(self, value):
        self._grade_expired_time = value
    @property
    def max_count(self):
        return self._max_count

    @max_count.setter
    def max_count(self, value):
        self._max_count = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_partner_id(self):
        return self._out_partner_id

    @out_partner_id.setter
    def out_partner_id(self, value):
        self._out_partner_id = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def privilege_id(self):
        return self._privilege_id

    @privilege_id.setter
    def privilege_id(self, value):
        self._privilege_id = value
    @property
    def register_channel(self):
        return self._register_channel

    @register_channel.setter
    def register_channel(self, value):
        self._register_channel = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def station(self):
        return self._station

    @station.setter
    def station(self, value):
        self._station = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def train_number(self):
        return self._train_number

    @train_number.setter
    def train_number(self, value):
        self._train_number = value
    @property
    def trans_quantum(self):
        return self._trans_quantum

    @trans_quantum.setter
    def trans_quantum(self, value):
        self._trans_quantum = value
    @property
    def travel_time(self):
        return self._travel_time

    @travel_time.setter
    def travel_time(self, value):
        self._travel_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_pay_amount(self):
        return self._user_pay_amount

    @user_pay_amount.setter
    def user_pay_amount(self, value):
        self._user_pay_amount = value
    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        self._vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.butler_use_flag:
            if hasattr(self.butler_use_flag, 'to_alipay_dict'):
                params['butler_use_flag'] = self.butler_use_flag.to_alipay_dict()
            else:
                params['butler_use_flag'] = self.butler_use_flag
        if self.car_use_flag:
            if hasattr(self.car_use_flag, 'to_alipay_dict'):
                params['car_use_flag'] = self.car_use_flag.to_alipay_dict()
            else:
                params['car_use_flag'] = self.car_use_flag
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.compartment_number:
            if hasattr(self.compartment_number, 'to_alipay_dict'):
                params['compartment_number'] = self.compartment_number.to_alipay_dict()
            else:
                params['compartment_number'] = self.compartment_number
        if self.current_count:
            if hasattr(self.current_count, 'to_alipay_dict'):
                params['current_count'] = self.current_count.to_alipay_dict()
            else:
                params['current_count'] = self.current_count
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.grade_expired_time:
            if hasattr(self.grade_expired_time, 'to_alipay_dict'):
                params['grade_expired_time'] = self.grade_expired_time.to_alipay_dict()
            else:
                params['grade_expired_time'] = self.grade_expired_time
        if self.max_count:
            if hasattr(self.max_count, 'to_alipay_dict'):
                params['max_count'] = self.max_count.to_alipay_dict()
            else:
                params['max_count'] = self.max_count
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_partner_id:
            if hasattr(self.out_partner_id, 'to_alipay_dict'):
                params['out_partner_id'] = self.out_partner_id.to_alipay_dict()
            else:
                params['out_partner_id'] = self.out_partner_id
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.privilege_id:
            if hasattr(self.privilege_id, 'to_alipay_dict'):
                params['privilege_id'] = self.privilege_id.to_alipay_dict()
            else:
                params['privilege_id'] = self.privilege_id
        if self.register_channel:
            if hasattr(self.register_channel, 'to_alipay_dict'):
                params['register_channel'] = self.register_channel.to_alipay_dict()
            else:
                params['register_channel'] = self.register_channel
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.station:
            if hasattr(self.station, 'to_alipay_dict'):
                params['station'] = self.station.to_alipay_dict()
            else:
                params['station'] = self.station
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.train_number:
            if hasattr(self.train_number, 'to_alipay_dict'):
                params['train_number'] = self.train_number.to_alipay_dict()
            else:
                params['train_number'] = self.train_number
        if self.trans_quantum:
            if hasattr(self.trans_quantum, 'to_alipay_dict'):
                params['trans_quantum'] = self.trans_quantum.to_alipay_dict()
            else:
                params['trans_quantum'] = self.trans_quantum
        if self.travel_time:
            if hasattr(self.travel_time, 'to_alipay_dict'):
                params['travel_time'] = self.travel_time.to_alipay_dict()
            else:
                params['travel_time'] = self.travel_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_pay_amount:
            if hasattr(self.user_pay_amount, 'to_alipay_dict'):
                params['user_pay_amount'] = self.user_pay_amount.to_alipay_dict()
            else:
                params['user_pay_amount'] = self.user_pay_amount
        if self.vendor:
            if hasattr(self.vendor, 'to_alipay_dict'):
                params['vendor'] = self.vendor.to_alipay_dict()
            else:
                params['vendor'] = self.vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPartnerPrivilegenoauthSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'butler_use_flag' in d:
            o.butler_use_flag = d['butler_use_flag']
        if 'car_use_flag' in d:
            o.car_use_flag = d['car_use_flag']
        if 'city' in d:
            o.city = d['city']
        if 'compartment_number' in d:
            o.compartment_number = d['compartment_number']
        if 'current_count' in d:
            o.current_count = d['current_count']
        if 'grade' in d:
            o.grade = d['grade']
        if 'grade_expired_time' in d:
            o.grade_expired_time = d['grade_expired_time']
        if 'max_count' in d:
            o.max_count = d['max_count']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_partner_id' in d:
            o.out_partner_id = d['out_partner_id']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'privilege_id' in d:
            o.privilege_id = d['privilege_id']
        if 'register_channel' in d:
            o.register_channel = d['register_channel']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'station' in d:
            o.station = d['station']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'train_number' in d:
            o.train_number = d['train_number']
        if 'trans_quantum' in d:
            o.trans_quantum = d['trans_quantum']
        if 'travel_time' in d:
            o.travel_time = d['travel_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_pay_amount' in d:
            o.user_pay_amount = d['user_pay_amount']
        if 'vendor' in d:
            o.vendor = d['vendor']
        return o


