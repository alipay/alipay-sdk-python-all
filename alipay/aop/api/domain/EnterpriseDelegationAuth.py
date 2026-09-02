#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseDelegationAuth(object):

    def __init__(self):
        self._agreement_no = None
        self._auth_time = None
        self._licensor = None
        self._licensor_name = None
        self._licensor_open_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value
    @property
    def licensor(self):
        return self._licensor

    @licensor.setter
    def licensor(self, value):
        self._licensor = value
    @property
    def licensor_name(self):
        return self._licensor_name

    @licensor_name.setter
    def licensor_name(self, value):
        self._licensor_name = value
    @property
    def licensor_open_id(self):
        return self._licensor_open_id

    @licensor_open_id.setter
    def licensor_open_id(self, value):
        self._licensor_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        if self.licensor:
            if hasattr(self.licensor, 'to_alipay_dict'):
                params['licensor'] = self.licensor.to_alipay_dict()
            else:
                params['licensor'] = self.licensor
        if self.licensor_name:
            if hasattr(self.licensor_name, 'to_alipay_dict'):
                params['licensor_name'] = self.licensor_name.to_alipay_dict()
            else:
                params['licensor_name'] = self.licensor_name
        if self.licensor_open_id:
            if hasattr(self.licensor_open_id, 'to_alipay_dict'):
                params['licensor_open_id'] = self.licensor_open_id.to_alipay_dict()
            else:
                params['licensor_open_id'] = self.licensor_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseDelegationAuth()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'licensor' in d:
            o.licensor = d['licensor']
        if 'licensor_name' in d:
            o.licensor_name = d['licensor_name']
        if 'licensor_open_id' in d:
            o.licensor_open_id = d['licensor_open_id']
        return o


