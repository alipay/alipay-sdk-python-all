#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignQueryResult(object):

    def __init__(self):
        self._alipay_user_id = None
        self._bind_results = None
        self._freeze_amount = None
        self._open_id = None
        self._request_no = None
        self._sign_time = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def bind_results(self):
        return self._bind_results

    @bind_results.setter
    def bind_results(self, value):
        self._bind_results = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.bind_results:
            if hasattr(self.bind_results, 'to_alipay_dict'):
                params['bind_results'] = self.bind_results.to_alipay_dict()
            else:
                params['bind_results'] = self.bind_results
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
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
        o = SignQueryResult()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'bind_results' in d:
            o.bind_results = d['bind_results']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        return o


