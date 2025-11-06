#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalExchangeRedirectVerifyModel(object):

    def __init__(self):
        self._benefit_id = None
        self._biz_no = None
        self._exchange_code = None
        self._open_id = None
        self._out_service_start_time = None
        self._phone = None
        self._renew = None
        self._service_end_time = None
        self._user_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def exchange_code(self):
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, value):
        self._exchange_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_service_start_time(self):
        return self._out_service_start_time

    @out_service_start_time.setter
    def out_service_start_time(self, value):
        self._out_service_start_time = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def renew(self):
        return self._renew

    @renew.setter
    def renew(self, value):
        self._renew = value
    @property
    def service_end_time(self):
        return self._service_end_time

    @service_end_time.setter
    def service_end_time(self, value):
        self._service_end_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.exchange_code:
            if hasattr(self.exchange_code, 'to_alipay_dict'):
                params['exchange_code'] = self.exchange_code.to_alipay_dict()
            else:
                params['exchange_code'] = self.exchange_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_service_start_time:
            if hasattr(self.out_service_start_time, 'to_alipay_dict'):
                params['out_service_start_time'] = self.out_service_start_time.to_alipay_dict()
            else:
                params['out_service_start_time'] = self.out_service_start_time
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.renew:
            if hasattr(self.renew, 'to_alipay_dict'):
                params['renew'] = self.renew.to_alipay_dict()
            else:
                params['renew'] = self.renew
        if self.service_end_time:
            if hasattr(self.service_end_time, 'to_alipay_dict'):
                params['service_end_time'] = self.service_end_time.to_alipay_dict()
            else:
                params['service_end_time'] = self.service_end_time
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
        o = AlipayCommerceMedicalExchangeRedirectVerifyModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'exchange_code' in d:
            o.exchange_code = d['exchange_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_service_start_time' in d:
            o.out_service_start_time = d['out_service_start_time']
        if 'phone' in d:
            o.phone = d['phone']
        if 'renew' in d:
            o.renew = d['renew']
        if 'service_end_time' in d:
            o.service_end_time = d['service_end_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


