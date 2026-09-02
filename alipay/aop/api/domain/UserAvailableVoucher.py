#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserAvailableVoucher(object):

    def __init__(self):
        self._ac_code = None
        self._active_time = None
        self._arr_airport_code = None
        self._dep_airport_code = None
        self._dep_date = None
        self._expired_time = None
        self._flight_no = None
        self._ota_code = None
        self._pid = None
        self._promo_rules = None
        self._template_id = None
        self._voucher_amount = None
        self._voucher_description = None
        self._voucher_id = None
        self._voucher_source_type = None

    @property
    def ac_code(self):
        return self._ac_code

    @ac_code.setter
    def ac_code(self, value):
        self._ac_code = value
    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def arr_airport_code(self):
        return self._arr_airport_code

    @arr_airport_code.setter
    def arr_airport_code(self, value):
        self._arr_airport_code = value
    @property
    def dep_airport_code(self):
        return self._dep_airport_code

    @dep_airport_code.setter
    def dep_airport_code(self, value):
        self._dep_airport_code = value
    @property
    def dep_date(self):
        return self._dep_date

    @dep_date.setter
    def dep_date(self, value):
        self._dep_date = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def flight_no(self):
        return self._flight_no

    @flight_no.setter
    def flight_no(self, value):
        self._flight_no = value
    @property
    def ota_code(self):
        return self._ota_code

    @ota_code.setter
    def ota_code(self, value):
        self._ota_code = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def promo_rules(self):
        return self._promo_rules

    @promo_rules.setter
    def promo_rules(self, value):
        self._promo_rules = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_amount(self):
        return self._voucher_amount

    @voucher_amount.setter
    def voucher_amount(self, value):
        self._voucher_amount = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_source_type(self):
        return self._voucher_source_type

    @voucher_source_type.setter
    def voucher_source_type(self, value):
        self._voucher_source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ac_code:
            if hasattr(self.ac_code, 'to_alipay_dict'):
                params['ac_code'] = self.ac_code.to_alipay_dict()
            else:
                params['ac_code'] = self.ac_code
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.arr_airport_code:
            if hasattr(self.arr_airport_code, 'to_alipay_dict'):
                params['arr_airport_code'] = self.arr_airport_code.to_alipay_dict()
            else:
                params['arr_airport_code'] = self.arr_airport_code
        if self.dep_airport_code:
            if hasattr(self.dep_airport_code, 'to_alipay_dict'):
                params['dep_airport_code'] = self.dep_airport_code.to_alipay_dict()
            else:
                params['dep_airport_code'] = self.dep_airport_code
        if self.dep_date:
            if hasattr(self.dep_date, 'to_alipay_dict'):
                params['dep_date'] = self.dep_date.to_alipay_dict()
            else:
                params['dep_date'] = self.dep_date
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.flight_no:
            if hasattr(self.flight_no, 'to_alipay_dict'):
                params['flight_no'] = self.flight_no.to_alipay_dict()
            else:
                params['flight_no'] = self.flight_no
        if self.ota_code:
            if hasattr(self.ota_code, 'to_alipay_dict'):
                params['ota_code'] = self.ota_code.to_alipay_dict()
            else:
                params['ota_code'] = self.ota_code
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.promo_rules:
            if hasattr(self.promo_rules, 'to_alipay_dict'):
                params['promo_rules'] = self.promo_rules.to_alipay_dict()
            else:
                params['promo_rules'] = self.promo_rules
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.voucher_amount:
            if hasattr(self.voucher_amount, 'to_alipay_dict'):
                params['voucher_amount'] = self.voucher_amount.to_alipay_dict()
            else:
                params['voucher_amount'] = self.voucher_amount
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_source_type:
            if hasattr(self.voucher_source_type, 'to_alipay_dict'):
                params['voucher_source_type'] = self.voucher_source_type.to_alipay_dict()
            else:
                params['voucher_source_type'] = self.voucher_source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserAvailableVoucher()
        if 'ac_code' in d:
            o.ac_code = d['ac_code']
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'arr_airport_code' in d:
            o.arr_airport_code = d['arr_airport_code']
        if 'dep_airport_code' in d:
            o.dep_airport_code = d['dep_airport_code']
        if 'dep_date' in d:
            o.dep_date = d['dep_date']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'flight_no' in d:
            o.flight_no = d['flight_no']
        if 'ota_code' in d:
            o.ota_code = d['ota_code']
        if 'pid' in d:
            o.pid = d['pid']
        if 'promo_rules' in d:
            o.promo_rules = d['promo_rules']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'voucher_amount' in d:
            o.voucher_amount = d['voucher_amount']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_source_type' in d:
            o.voucher_source_type = d['voucher_source_type']
        return o


