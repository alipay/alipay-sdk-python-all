#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyFinleaseTokenQueryModel(object):

    def __init__(self):
        self._alipay_id = None
        self._biz_context = None
        self._biz_sence = None
        self._ip_id = None
        self._ip_role_id = None
        self._open_id = None
        self._option_type = None
        self._request_date = None
        self._request_id = None

    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def biz_context(self):
        return self._biz_context

    @biz_context.setter
    def biz_context(self, value):
        self._biz_context = value
    @property
    def biz_sence(self):
        return self._biz_sence

    @biz_sence.setter
    def biz_sence(self, value):
        self._biz_sence = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def option_type(self):
        return self._option_type

    @option_type.setter
    def option_type(self, value):
        self._option_type = value
    @property
    def request_date(self):
        return self._request_date

    @request_date.setter
    def request_date(self, value):
        self._request_date = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.biz_context:
            if hasattr(self.biz_context, 'to_alipay_dict'):
                params['biz_context'] = self.biz_context.to_alipay_dict()
            else:
                params['biz_context'] = self.biz_context
        if self.biz_sence:
            if hasattr(self.biz_sence, 'to_alipay_dict'):
                params['biz_sence'] = self.biz_sence.to_alipay_dict()
            else:
                params['biz_sence'] = self.biz_sence
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.option_type:
            if hasattr(self.option_type, 'to_alipay_dict'):
                params['option_type'] = self.option_type.to_alipay_dict()
            else:
                params['option_type'] = self.option_type
        if self.request_date:
            if hasattr(self.request_date, 'to_alipay_dict'):
                params['request_date'] = self.request_date.to_alipay_dict()
            else:
                params['request_date'] = self.request_date
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyFinleaseTokenQueryModel()
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'biz_context' in d:
            o.biz_context = d['biz_context']
        if 'biz_sence' in d:
            o.biz_sence = d['biz_sence']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'option_type' in d:
            o.option_type = d['option_type']
        if 'request_date' in d:
            o.request_date = d['request_date']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


