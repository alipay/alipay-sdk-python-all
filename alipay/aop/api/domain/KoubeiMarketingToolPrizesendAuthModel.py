#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingToolPrizesendAuthModel(object):

    def __init__(self):
        self._prize_id = None
        self._req_id = None
        self._user_id = None

    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
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
        o = KoubeiMarketingToolPrizesendAuthModel()
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'req_id' in d:
            o.req_id = d['req_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


