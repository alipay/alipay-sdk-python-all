#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphonePeriodorderCreateModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_order_no = None
        self._alipay_user_id = None
        self._out_biz_no = None
        self._period_amount = None
        self._step_number = None
        self._user_period_status = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period_amount(self):
        return self._period_amount

    @period_amount.setter
    def period_amount(self, value):
        self._period_amount = value
    @property
    def step_number(self):
        return self._step_number

    @step_number.setter
    def step_number(self, value):
        self._step_number = value
    @property
    def user_period_status(self):
        return self._user_period_status

    @user_period_status.setter
    def user_period_status(self, value):
        self._user_period_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period_amount:
            if hasattr(self.period_amount, 'to_alipay_dict'):
                params['period_amount'] = self.period_amount.to_alipay_dict()
            else:
                params['period_amount'] = self.period_amount
        if self.step_number:
            if hasattr(self.step_number, 'to_alipay_dict'):
                params['step_number'] = self.step_number.to_alipay_dict()
            else:
                params['step_number'] = self.step_number
        if self.user_period_status:
            if hasattr(self.user_period_status, 'to_alipay_dict'):
                params['user_period_status'] = self.user_period_status.to_alipay_dict()
            else:
                params['user_period_status'] = self.user_period_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphonePeriodorderCreateModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period_amount' in d:
            o.period_amount = d['period_amount']
        if 'step_number' in d:
            o.step_number = d['step_number']
        if 'user_period_status' in d:
            o.user_period_status = d['user_period_status']
        return o


