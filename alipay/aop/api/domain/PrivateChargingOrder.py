#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrivateChargingOrder(object):

    def __init__(self):
        self._current_a = None
        self._current_b = None
        self._current_c = None
        self._elec_money = None
        self._end_time = None
        self._equip_id = None
        self._open_id = None
        self._operator_id = None
        self._operator_uid = None
        self._sample_time = None
        self._soc = None
        self._start_charge_seq = None
        self._start_charge_seq_stat = None
        self._start_time = None
        self._total_power = None
        self._user_id = None
        self._voltage_a = None
        self._voltage_b = None
        self._voltage_c = None

    @property
    def current_a(self):
        return self._current_a

    @current_a.setter
    def current_a(self, value):
        self._current_a = value
    @property
    def current_b(self):
        return self._current_b

    @current_b.setter
    def current_b(self, value):
        self._current_b = value
    @property
    def current_c(self):
        return self._current_c

    @current_c.setter
    def current_c(self, value):
        self._current_c = value
    @property
    def elec_money(self):
        return self._elec_money

    @elec_money.setter
    def elec_money(self, value):
        self._elec_money = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def equip_id(self):
        return self._equip_id

    @equip_id.setter
    def equip_id(self, value):
        self._equip_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_uid(self):
        return self._operator_uid

    @operator_uid.setter
    def operator_uid(self, value):
        self._operator_uid = value
    @property
    def sample_time(self):
        return self._sample_time

    @sample_time.setter
    def sample_time(self, value):
        self._sample_time = value
    @property
    def soc(self):
        return self._soc

    @soc.setter
    def soc(self, value):
        self._soc = value
    @property
    def start_charge_seq(self):
        return self._start_charge_seq

    @start_charge_seq.setter
    def start_charge_seq(self, value):
        self._start_charge_seq = value
    @property
    def start_charge_seq_stat(self):
        return self._start_charge_seq_stat

    @start_charge_seq_stat.setter
    def start_charge_seq_stat(self, value):
        self._start_charge_seq_stat = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_power(self):
        return self._total_power

    @total_power.setter
    def total_power(self, value):
        self._total_power = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voltage_a(self):
        return self._voltage_a

    @voltage_a.setter
    def voltage_a(self, value):
        self._voltage_a = value
    @property
    def voltage_b(self):
        return self._voltage_b

    @voltage_b.setter
    def voltage_b(self, value):
        self._voltage_b = value
    @property
    def voltage_c(self):
        return self._voltage_c

    @voltage_c.setter
    def voltage_c(self, value):
        self._voltage_c = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_a:
            if hasattr(self.current_a, 'to_alipay_dict'):
                params['current_a'] = self.current_a.to_alipay_dict()
            else:
                params['current_a'] = self.current_a
        if self.current_b:
            if hasattr(self.current_b, 'to_alipay_dict'):
                params['current_b'] = self.current_b.to_alipay_dict()
            else:
                params['current_b'] = self.current_b
        if self.current_c:
            if hasattr(self.current_c, 'to_alipay_dict'):
                params['current_c'] = self.current_c.to_alipay_dict()
            else:
                params['current_c'] = self.current_c
        if self.elec_money:
            if hasattr(self.elec_money, 'to_alipay_dict'):
                params['elec_money'] = self.elec_money.to_alipay_dict()
            else:
                params['elec_money'] = self.elec_money
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.equip_id:
            if hasattr(self.equip_id, 'to_alipay_dict'):
                params['equip_id'] = self.equip_id.to_alipay_dict()
            else:
                params['equip_id'] = self.equip_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_uid:
            if hasattr(self.operator_uid, 'to_alipay_dict'):
                params['operator_uid'] = self.operator_uid.to_alipay_dict()
            else:
                params['operator_uid'] = self.operator_uid
        if self.sample_time:
            if hasattr(self.sample_time, 'to_alipay_dict'):
                params['sample_time'] = self.sample_time.to_alipay_dict()
            else:
                params['sample_time'] = self.sample_time
        if self.soc:
            if hasattr(self.soc, 'to_alipay_dict'):
                params['soc'] = self.soc.to_alipay_dict()
            else:
                params['soc'] = self.soc
        if self.start_charge_seq:
            if hasattr(self.start_charge_seq, 'to_alipay_dict'):
                params['start_charge_seq'] = self.start_charge_seq.to_alipay_dict()
            else:
                params['start_charge_seq'] = self.start_charge_seq
        if self.start_charge_seq_stat:
            if hasattr(self.start_charge_seq_stat, 'to_alipay_dict'):
                params['start_charge_seq_stat'] = self.start_charge_seq_stat.to_alipay_dict()
            else:
                params['start_charge_seq_stat'] = self.start_charge_seq_stat
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.total_power:
            if hasattr(self.total_power, 'to_alipay_dict'):
                params['total_power'] = self.total_power.to_alipay_dict()
            else:
                params['total_power'] = self.total_power
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voltage_a:
            if hasattr(self.voltage_a, 'to_alipay_dict'):
                params['voltage_a'] = self.voltage_a.to_alipay_dict()
            else:
                params['voltage_a'] = self.voltage_a
        if self.voltage_b:
            if hasattr(self.voltage_b, 'to_alipay_dict'):
                params['voltage_b'] = self.voltage_b.to_alipay_dict()
            else:
                params['voltage_b'] = self.voltage_b
        if self.voltage_c:
            if hasattr(self.voltage_c, 'to_alipay_dict'):
                params['voltage_c'] = self.voltage_c.to_alipay_dict()
            else:
                params['voltage_c'] = self.voltage_c
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrivateChargingOrder()
        if 'current_a' in d:
            o.current_a = d['current_a']
        if 'current_b' in d:
            o.current_b = d['current_b']
        if 'current_c' in d:
            o.current_c = d['current_c']
        if 'elec_money' in d:
            o.elec_money = d['elec_money']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'equip_id' in d:
            o.equip_id = d['equip_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_uid' in d:
            o.operator_uid = d['operator_uid']
        if 'sample_time' in d:
            o.sample_time = d['sample_time']
        if 'soc' in d:
            o.soc = d['soc']
        if 'start_charge_seq' in d:
            o.start_charge_seq = d['start_charge_seq']
        if 'start_charge_seq_stat' in d:
            o.start_charge_seq_stat = d['start_charge_seq_stat']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_power' in d:
            o.total_power = d['total_power']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voltage_a' in d:
            o.voltage_a = d['voltage_a']
        if 'voltage_b' in d:
            o.voltage_b = d['voltage_b']
        if 'voltage_c' in d:
            o.voltage_c = d['voltage_c']
        return o


