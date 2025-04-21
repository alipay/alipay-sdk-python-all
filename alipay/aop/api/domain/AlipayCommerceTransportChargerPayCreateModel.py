#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportChargerPayCreateModel(object):

    def __init__(self):
        self._discount_amount = None
        self._elec_money = None
        self._end_time = None
        self._open_id = None
        self._out_trade_no = None
        self._pay_amount = None
        self._real_elec_money = None
        self._real_service_money = None
        self._reserved_money = None
        self._service_money = None
        self._soc = None
        self._start_time = None
        self._stop_reason = None
        self._total_amount = None
        self._total_power = None
        self._user_id = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
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
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def real_elec_money(self):
        return self._real_elec_money

    @real_elec_money.setter
    def real_elec_money(self, value):
        self._real_elec_money = value
    @property
    def real_service_money(self):
        return self._real_service_money

    @real_service_money.setter
    def real_service_money(self, value):
        self._real_service_money = value
    @property
    def reserved_money(self):
        return self._reserved_money

    @reserved_money.setter
    def reserved_money(self, value):
        self._reserved_money = value
    @property
    def service_money(self):
        return self._service_money

    @service_money.setter
    def service_money(self, value):
        self._service_money = value
    @property
    def soc(self):
        return self._soc

    @soc.setter
    def soc(self, value):
        self._soc = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def stop_reason(self):
        return self._stop_reason

    @stop_reason.setter
    def stop_reason(self, value):
        self._stop_reason = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
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
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.real_elec_money:
            if hasattr(self.real_elec_money, 'to_alipay_dict'):
                params['real_elec_money'] = self.real_elec_money.to_alipay_dict()
            else:
                params['real_elec_money'] = self.real_elec_money
        if self.real_service_money:
            if hasattr(self.real_service_money, 'to_alipay_dict'):
                params['real_service_money'] = self.real_service_money.to_alipay_dict()
            else:
                params['real_service_money'] = self.real_service_money
        if self.reserved_money:
            if hasattr(self.reserved_money, 'to_alipay_dict'):
                params['reserved_money'] = self.reserved_money.to_alipay_dict()
            else:
                params['reserved_money'] = self.reserved_money
        if self.service_money:
            if hasattr(self.service_money, 'to_alipay_dict'):
                params['service_money'] = self.service_money.to_alipay_dict()
            else:
                params['service_money'] = self.service_money
        if self.soc:
            if hasattr(self.soc, 'to_alipay_dict'):
                params['soc'] = self.soc.to_alipay_dict()
            else:
                params['soc'] = self.soc
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.stop_reason:
            if hasattr(self.stop_reason, 'to_alipay_dict'):
                params['stop_reason'] = self.stop_reason.to_alipay_dict()
            else:
                params['stop_reason'] = self.stop_reason
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportChargerPayCreateModel()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'elec_money' in d:
            o.elec_money = d['elec_money']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'real_elec_money' in d:
            o.real_elec_money = d['real_elec_money']
        if 'real_service_money' in d:
            o.real_service_money = d['real_service_money']
        if 'reserved_money' in d:
            o.reserved_money = d['reserved_money']
        if 'service_money' in d:
            o.service_money = d['service_money']
        if 'soc' in d:
            o.soc = d['soc']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'stop_reason' in d:
            o.stop_reason = d['stop_reason']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_power' in d:
            o.total_power = d['total_power']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


