#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeBillRepayQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._auth_ar_no = None
        self._open_id = None
        self._repay_request_no = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auth_ar_no(self):
        return self._auth_ar_no

    @auth_ar_no.setter
    def auth_ar_no(self, value):
        self._auth_ar_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def repay_request_no(self):
        return self._repay_request_no

    @repay_request_no.setter
    def repay_request_no(self, value):
        self._repay_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.auth_ar_no:
            if hasattr(self.auth_ar_no, 'to_alipay_dict'):
                params['auth_ar_no'] = self.auth_ar_no.to_alipay_dict()
            else:
                params['auth_ar_no'] = self.auth_ar_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.repay_request_no:
            if hasattr(self.repay_request_no, 'to_alipay_dict'):
                params['repay_request_no'] = self.repay_request_no.to_alipay_dict()
            else:
                params['repay_request_no'] = self.repay_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeBillRepayQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'auth_ar_no' in d:
            o.auth_ar_no = d['auth_ar_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'repay_request_no' in d:
            o.repay_request_no = d['repay_request_no']
        return o


