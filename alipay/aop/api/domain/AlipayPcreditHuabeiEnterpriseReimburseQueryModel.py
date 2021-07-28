#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiEnterpriseReimburseQueryModel(object):

    def __init__(self):
        self._partner_id = None
        self._record_code = None
        self._user_id = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def record_code(self):
        return self._record_code

    @record_code.setter
    def record_code(self, value):
        self._record_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.record_code:
            if hasattr(self.record_code, 'to_alipay_dict'):
                params['record_code'] = self.record_code.to_alipay_dict()
            else:
                params['record_code'] = self.record_code
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
        o = AlipayPcreditHuabeiEnterpriseReimburseQueryModel()
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'record_code' in d:
            o.record_code = d['record_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


