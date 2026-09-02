#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandGroupEntrysignQueryModel(object):

    def __init__(self):
        self._entry_sign_open_id = None
        self._user_id = None

    @property
    def entry_sign_open_id(self):
        return self._entry_sign_open_id

    @entry_sign_open_id.setter
    def entry_sign_open_id(self, value):
        self._entry_sign_open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.entry_sign_open_id:
            if hasattr(self.entry_sign_open_id, 'to_alipay_dict'):
                params['entry_sign_open_id'] = self.entry_sign_open_id.to_alipay_dict()
            else:
                params['entry_sign_open_id'] = self.entry_sign_open_id
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
        o = AntMerchantExpandGroupEntrysignQueryModel()
        if 'entry_sign_open_id' in d:
            o.entry_sign_open_id = d['entry_sign_open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


