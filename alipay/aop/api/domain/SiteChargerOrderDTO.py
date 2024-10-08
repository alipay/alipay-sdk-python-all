#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SiteChargerOrderDTO(object):

    def __init__(self):
        self._connector_id = None
        self._end_time = None
        self._open_id = None
        self._operator_id = None
        self._operator_name = None
        self._pay_channel = None
        self._payment_trade_no = None
        self._start_charge_seq = None
        self._start_time = None
        self._station_id = None
        self._station_name = None
        self._total_elec_money = None
        self._total_money = None
        self._total_power = None
        self._total_real_elec_money = None
        self._total_real_service_money = None
        self._total_service_money = None
        self._user_id = None

    @property
    def connector_id(self):
        return self._connector_id

    @connector_id.setter
    def connector_id(self, value):
        self._connector_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
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
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def payment_trade_no(self):
        return self._payment_trade_no

    @payment_trade_no.setter
    def payment_trade_no(self, value):
        self._payment_trade_no = value
    @property
    def start_charge_seq(self):
        return self._start_charge_seq

    @start_charge_seq.setter
    def start_charge_seq(self, value):
        self._start_charge_seq = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, value):
        self._station_id = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def total_elec_money(self):
        return self._total_elec_money

    @total_elec_money.setter
    def total_elec_money(self, value):
        self._total_elec_money = value
    @property
    def total_money(self):
        return self._total_money

    @total_money.setter
    def total_money(self, value):
        self._total_money = value
    @property
    def total_power(self):
        return self._total_power

    @total_power.setter
    def total_power(self, value):
        self._total_power = value
    @property
    def total_real_elec_money(self):
        return self._total_real_elec_money

    @total_real_elec_money.setter
    def total_real_elec_money(self, value):
        self._total_real_elec_money = value
    @property
    def total_real_service_money(self):
        return self._total_real_service_money

    @total_real_service_money.setter
    def total_real_service_money(self, value):
        self._total_real_service_money = value
    @property
    def total_service_money(self):
        return self._total_service_money

    @total_service_money.setter
    def total_service_money(self, value):
        self._total_service_money = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.connector_id:
            if hasattr(self.connector_id, 'to_alipay_dict'):
                params['connector_id'] = self.connector_id.to_alipay_dict()
            else:
                params['connector_id'] = self.connector_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
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
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.payment_trade_no:
            if hasattr(self.payment_trade_no, 'to_alipay_dict'):
                params['payment_trade_no'] = self.payment_trade_no.to_alipay_dict()
            else:
                params['payment_trade_no'] = self.payment_trade_no
        if self.start_charge_seq:
            if hasattr(self.start_charge_seq, 'to_alipay_dict'):
                params['start_charge_seq'] = self.start_charge_seq.to_alipay_dict()
            else:
                params['start_charge_seq'] = self.start_charge_seq
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.station_id:
            if hasattr(self.station_id, 'to_alipay_dict'):
                params['station_id'] = self.station_id.to_alipay_dict()
            else:
                params['station_id'] = self.station_id
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.total_elec_money:
            if hasattr(self.total_elec_money, 'to_alipay_dict'):
                params['total_elec_money'] = self.total_elec_money.to_alipay_dict()
            else:
                params['total_elec_money'] = self.total_elec_money
        if self.total_money:
            if hasattr(self.total_money, 'to_alipay_dict'):
                params['total_money'] = self.total_money.to_alipay_dict()
            else:
                params['total_money'] = self.total_money
        if self.total_power:
            if hasattr(self.total_power, 'to_alipay_dict'):
                params['total_power'] = self.total_power.to_alipay_dict()
            else:
                params['total_power'] = self.total_power
        if self.total_real_elec_money:
            if hasattr(self.total_real_elec_money, 'to_alipay_dict'):
                params['total_real_elec_money'] = self.total_real_elec_money.to_alipay_dict()
            else:
                params['total_real_elec_money'] = self.total_real_elec_money
        if self.total_real_service_money:
            if hasattr(self.total_real_service_money, 'to_alipay_dict'):
                params['total_real_service_money'] = self.total_real_service_money.to_alipay_dict()
            else:
                params['total_real_service_money'] = self.total_real_service_money
        if self.total_service_money:
            if hasattr(self.total_service_money, 'to_alipay_dict'):
                params['total_service_money'] = self.total_service_money.to_alipay_dict()
            else:
                params['total_service_money'] = self.total_service_money
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
        o = SiteChargerOrderDTO()
        if 'connector_id' in d:
            o.connector_id = d['connector_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'payment_trade_no' in d:
            o.payment_trade_no = d['payment_trade_no']
        if 'start_charge_seq' in d:
            o.start_charge_seq = d['start_charge_seq']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'station_id' in d:
            o.station_id = d['station_id']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'total_elec_money' in d:
            o.total_elec_money = d['total_elec_money']
        if 'total_money' in d:
            o.total_money = d['total_money']
        if 'total_power' in d:
            o.total_power = d['total_power']
        if 'total_real_elec_money' in d:
            o.total_real_elec_money = d['total_real_elec_money']
        if 'total_real_service_money' in d:
            o.total_real_service_money = d['total_real_service_money']
        if 'total_service_money' in d:
            o.total_service_money = d['total_service_money']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


