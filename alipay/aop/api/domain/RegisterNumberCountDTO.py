#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegisterNumberCountDTO(object):

    def __init__(self):
        self._add_number_flag = None
        self._available_num = None
        self._detail_url = None
        self._fee = None
        self._number_open_time = None
        self._number_status = None
        self._period = None
        self._pre_unit = None
        self._register_id = None

    @property
    def add_number_flag(self):
        return self._add_number_flag

    @add_number_flag.setter
    def add_number_flag(self, value):
        self._add_number_flag = value
    @property
    def available_num(self):
        return self._available_num

    @available_num.setter
    def available_num(self, value):
        self._available_num = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def number_open_time(self):
        return self._number_open_time

    @number_open_time.setter
    def number_open_time(self, value):
        self._number_open_time = value
    @property
    def number_status(self):
        return self._number_status

    @number_status.setter
    def number_status(self, value):
        self._number_status = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def pre_unit(self):
        return self._pre_unit

    @pre_unit.setter
    def pre_unit(self, value):
        self._pre_unit = value
    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, value):
        self._register_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_number_flag:
            if hasattr(self.add_number_flag, 'to_alipay_dict'):
                params['add_number_flag'] = self.add_number_flag.to_alipay_dict()
            else:
                params['add_number_flag'] = self.add_number_flag
        if self.available_num:
            if hasattr(self.available_num, 'to_alipay_dict'):
                params['available_num'] = self.available_num.to_alipay_dict()
            else:
                params['available_num'] = self.available_num
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.number_open_time:
            if hasattr(self.number_open_time, 'to_alipay_dict'):
                params['number_open_time'] = self.number_open_time.to_alipay_dict()
            else:
                params['number_open_time'] = self.number_open_time
        if self.number_status:
            if hasattr(self.number_status, 'to_alipay_dict'):
                params['number_status'] = self.number_status.to_alipay_dict()
            else:
                params['number_status'] = self.number_status
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.pre_unit:
            if hasattr(self.pre_unit, 'to_alipay_dict'):
                params['pre_unit'] = self.pre_unit.to_alipay_dict()
            else:
                params['pre_unit'] = self.pre_unit
        if self.register_id:
            if hasattr(self.register_id, 'to_alipay_dict'):
                params['register_id'] = self.register_id.to_alipay_dict()
            else:
                params['register_id'] = self.register_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegisterNumberCountDTO()
        if 'add_number_flag' in d:
            o.add_number_flag = d['add_number_flag']
        if 'available_num' in d:
            o.available_num = d['available_num']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'fee' in d:
            o.fee = d['fee']
        if 'number_open_time' in d:
            o.number_open_time = d['number_open_time']
        if 'number_status' in d:
            o.number_status = d['number_status']
        if 'period' in d:
            o.period = d['period']
        if 'pre_unit' in d:
            o.pre_unit = d['pre_unit']
        if 'register_id' in d:
            o.register_id = d['register_id']
        return o


