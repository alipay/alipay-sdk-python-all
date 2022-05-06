#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccountBaseInfoVO(object):

    def __init__(self):
        self._act_no = None
        self._act_status = None
        self._act_type = None

    @property
    def act_no(self):
        return self._act_no

    @act_no.setter
    def act_no(self, value):
        self._act_no = value
    @property
    def act_status(self):
        return self._act_status

    @act_status.setter
    def act_status(self, value):
        self._act_status = value
    @property
    def act_type(self):
        return self._act_type

    @act_type.setter
    def act_type(self, value):
        self._act_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.act_no:
            if hasattr(self.act_no, 'to_alipay_dict'):
                params['act_no'] = self.act_no.to_alipay_dict()
            else:
                params['act_no'] = self.act_no
        if self.act_status:
            if hasattr(self.act_status, 'to_alipay_dict'):
                params['act_status'] = self.act_status.to_alipay_dict()
            else:
                params['act_status'] = self.act_status
        if self.act_type:
            if hasattr(self.act_type, 'to_alipay_dict'):
                params['act_type'] = self.act_type.to_alipay_dict()
            else:
                params['act_type'] = self.act_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccountBaseInfoVO()
        if 'act_no' in d:
            o.act_no = d['act_no']
        if 'act_status' in d:
            o.act_status = d['act_status']
        if 'act_type' in d:
            o.act_type = d['act_type']
        return o


