#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdAfsrcWhitehatinfoQueryModel(object):

    def __init__(self):
        self._hid = None
        self._user_id = None

    @property
    def hid(self):
        return self._hid

    @hid.setter
    def hid(self, value):
        self._hid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.hid:
            if hasattr(self.hid, 'to_alipay_dict'):
                params['hid'] = self.hid.to_alipay_dict()
            else:
                params['hid'] = self.hid
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
        o = AlipaySecurityProdAfsrcWhitehatinfoQueryModel()
        if 'hid' in d:
            o.hid = d['hid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


