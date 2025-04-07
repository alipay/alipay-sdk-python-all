#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountTaobaoBindQueryModel(object):

    def __init__(self):
        self._havana_id = None
        self._umid = None
        self._user_token = None

    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def user_token(self):
        return self._user_token

    @user_token.setter
    def user_token(self, value):
        self._user_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = self.umid.to_alipay_dict()
            else:
                params['umid'] = self.umid
        if self.user_token:
            if hasattr(self.user_token, 'to_alipay_dict'):
                params['user_token'] = self.user_token.to_alipay_dict()
            else:
                params['user_token'] = self.user_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountTaobaoBindQueryModel()
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'umid' in d:
            o.umid = d['umid']
        if 'user_token' in d:
            o.user_token = d['user_token']
        return o


