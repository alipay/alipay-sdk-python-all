#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentFundAuthFreezeInfoVO(object):

    def __init__(self):
        self._auth_no = None
        self._freeze_notify_url = None
        self._payee_user_id = None
        self._risk_assessment_price = None
        self._sign_status = None
        self._sign_time = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def freeze_notify_url(self):
        return self._freeze_notify_url

    @freeze_notify_url.setter
    def freeze_notify_url(self, value):
        self._freeze_notify_url = value
    @property
    def payee_user_id(self):
        return self._payee_user_id

    @payee_user_id.setter
    def payee_user_id(self, value):
        self._payee_user_id = value
    @property
    def risk_assessment_price(self):
        return self._risk_assessment_price

    @risk_assessment_price.setter
    def risk_assessment_price(self, value):
        self._risk_assessment_price = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.freeze_notify_url:
            if hasattr(self.freeze_notify_url, 'to_alipay_dict'):
                params['freeze_notify_url'] = self.freeze_notify_url.to_alipay_dict()
            else:
                params['freeze_notify_url'] = self.freeze_notify_url
        if self.payee_user_id:
            if hasattr(self.payee_user_id, 'to_alipay_dict'):
                params['payee_user_id'] = self.payee_user_id.to_alipay_dict()
            else:
                params['payee_user_id'] = self.payee_user_id
        if self.risk_assessment_price:
            if hasattr(self.risk_assessment_price, 'to_alipay_dict'):
                params['risk_assessment_price'] = self.risk_assessment_price.to_alipay_dict()
            else:
                params['risk_assessment_price'] = self.risk_assessment_price
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentFundAuthFreezeInfoVO()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'freeze_notify_url' in d:
            o.freeze_notify_url = d['freeze_notify_url']
        if 'payee_user_id' in d:
            o.payee_user_id = d['payee_user_id']
        if 'risk_assessment_price' in d:
            o.risk_assessment_price = d['risk_assessment_price']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        return o


