#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Money import Money
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult


class AlipayOverseasTuitionSchoolcreditConfirmModel(object):

    def __init__(self):
        self._alipay_payment_id = None
        self._confirm_amount = None
        self._confirm_result = None
        self._confirm_time = None
        self._isv_payment_id = None
        self._isv_pid = None
        self._pass_through_info = None
        self._school_pid = None

    @property
    def alipay_payment_id(self):
        return self._alipay_payment_id

    @alipay_payment_id.setter
    def alipay_payment_id(self, value):
        self._alipay_payment_id = value
    @property
    def confirm_amount(self):
        return self._confirm_amount

    @confirm_amount.setter
    def confirm_amount(self, value):
        if isinstance(value, Money):
            self._confirm_amount = value
        else:
            self._confirm_amount = Money.from_alipay_dict(value)
    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        if isinstance(value, TuitionISVResult):
            self._confirm_result = value
        else:
            self._confirm_result = TuitionISVResult.from_alipay_dict(value)
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def isv_payment_id(self):
        return self._isv_payment_id

    @isv_payment_id.setter
    def isv_payment_id(self, value):
        self._isv_payment_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_payment_id:
            if hasattr(self.alipay_payment_id, 'to_alipay_dict'):
                params['alipay_payment_id'] = self.alipay_payment_id.to_alipay_dict()
            else:
                params['alipay_payment_id'] = self.alipay_payment_id
        if self.confirm_amount:
            if hasattr(self.confirm_amount, 'to_alipay_dict'):
                params['confirm_amount'] = self.confirm_amount.to_alipay_dict()
            else:
                params['confirm_amount'] = self.confirm_amount
        if self.confirm_result:
            if hasattr(self.confirm_result, 'to_alipay_dict'):
                params['confirm_result'] = self.confirm_result.to_alipay_dict()
            else:
                params['confirm_result'] = self.confirm_result
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.isv_payment_id:
            if hasattr(self.isv_payment_id, 'to_alipay_dict'):
                params['isv_payment_id'] = self.isv_payment_id.to_alipay_dict()
            else:
                params['isv_payment_id'] = self.isv_payment_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTuitionSchoolcreditConfirmModel()
        if 'alipay_payment_id' in d:
            o.alipay_payment_id = d['alipay_payment_id']
        if 'confirm_amount' in d:
            o.confirm_amount = d['confirm_amount']
        if 'confirm_result' in d:
            o.confirm_result = d['confirm_result']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'isv_payment_id' in d:
            o.isv_payment_id = d['isv_payment_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        return o


