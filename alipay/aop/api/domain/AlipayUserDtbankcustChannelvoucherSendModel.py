#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserDtbankcustChannelvoucherSendModel(object):

    def __init__(self):
        self._activity_id = None
        self._logon_id = None
        self._out_biz_no = None
        self._phone_id = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone_id(self):
        return self._phone_id

    @phone_id.setter
    def phone_id(self, value):
        self._phone_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone_id:
            if hasattr(self.phone_id, 'to_alipay_dict'):
                params['phone_id'] = self.phone_id.to_alipay_dict()
            else:
                params['phone_id'] = self.phone_id
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
        o = AlipayUserDtbankcustChannelvoucherSendModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_id' in d:
            o.phone_id = d['phone_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


