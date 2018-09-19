#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAuthOrderUnfreezeModel(object):

    def __init__(self):
        self._amount = None
        self._auth_no = None
        self._extra_param = None
        self._out_request_no = None
        self._remark = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAuthOrderUnfreezeModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'remark' in d:
            o.remark = d['remark']
        return o


