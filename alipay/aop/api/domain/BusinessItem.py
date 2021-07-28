#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessItem(object):

    def __init__(self):
        self._business_appid = None
        self._business_payee_id = None
        self._business_pid = None
        self._business_type = None

    @property
    def business_appid(self):
        return self._business_appid

    @business_appid.setter
    def business_appid(self, value):
        self._business_appid = value
    @property
    def business_payee_id(self):
        return self._business_payee_id

    @business_payee_id.setter
    def business_payee_id(self, value):
        self._business_payee_id = value
    @property
    def business_pid(self):
        return self._business_pid

    @business_pid.setter
    def business_pid(self, value):
        self._business_pid = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_appid:
            if hasattr(self.business_appid, 'to_alipay_dict'):
                params['business_appid'] = self.business_appid.to_alipay_dict()
            else:
                params['business_appid'] = self.business_appid
        if self.business_payee_id:
            if hasattr(self.business_payee_id, 'to_alipay_dict'):
                params['business_payee_id'] = self.business_payee_id.to_alipay_dict()
            else:
                params['business_payee_id'] = self.business_payee_id
        if self.business_pid:
            if hasattr(self.business_pid, 'to_alipay_dict'):
                params['business_pid'] = self.business_pid.to_alipay_dict()
            else:
                params['business_pid'] = self.business_pid
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessItem()
        if 'business_appid' in d:
            o.business_appid = d['business_appid']
        if 'business_payee_id' in d:
            o.business_payee_id = d['business_payee_id']
        if 'business_pid' in d:
            o.business_pid = d['business_pid']
        if 'business_type' in d:
            o.business_type = d['business_type']
        return o


