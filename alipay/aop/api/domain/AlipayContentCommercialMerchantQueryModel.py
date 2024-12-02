#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentCommercialMerchantQueryModel(object):

    def __init__(self):
        self._login_open_id = None
        self._login_user_id = None
        self._owner_open_id = None
        self._owner_user_id = None

    @property
    def login_open_id(self):
        return self._login_open_id

    @login_open_id.setter
    def login_open_id(self, value):
        self._login_open_id = value
    @property
    def login_user_id(self):
        return self._login_user_id

    @login_user_id.setter
    def login_user_id(self, value):
        self._login_user_id = value
    @property
    def owner_open_id(self):
        return self._owner_open_id

    @owner_open_id.setter
    def owner_open_id(self, value):
        self._owner_open_id = value
    @property
    def owner_user_id(self):
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, value):
        self._owner_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_open_id:
            if hasattr(self.login_open_id, 'to_alipay_dict'):
                params['login_open_id'] = self.login_open_id.to_alipay_dict()
            else:
                params['login_open_id'] = self.login_open_id
        if self.login_user_id:
            if hasattr(self.login_user_id, 'to_alipay_dict'):
                params['login_user_id'] = self.login_user_id.to_alipay_dict()
            else:
                params['login_user_id'] = self.login_user_id
        if self.owner_open_id:
            if hasattr(self.owner_open_id, 'to_alipay_dict'):
                params['owner_open_id'] = self.owner_open_id.to_alipay_dict()
            else:
                params['owner_open_id'] = self.owner_open_id
        if self.owner_user_id:
            if hasattr(self.owner_user_id, 'to_alipay_dict'):
                params['owner_user_id'] = self.owner_user_id.to_alipay_dict()
            else:
                params['owner_user_id'] = self.owner_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentCommercialMerchantQueryModel()
        if 'login_open_id' in d:
            o.login_open_id = d['login_open_id']
        if 'login_user_id' in d:
            o.login_user_id = d['login_user_id']
        if 'owner_open_id' in d:
            o.owner_open_id = d['owner_open_id']
        if 'owner_user_id' in d:
            o.owner_user_id = d['owner_user_id']
        return o


