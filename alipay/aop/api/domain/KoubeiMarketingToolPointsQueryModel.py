#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingToolPointsQueryModel(object):

    def __init__(self):
        self._activity_account = None
        self._user_id = None

    @property
    def activity_account(self):
        return self._activity_account

    @activity_account.setter
    def activity_account(self, value):
        self._activity_account = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_account:
            if hasattr(self.activity_account, 'to_alipay_dict'):
                params['activity_account'] = self.activity_account.to_alipay_dict()
            else:
                params['activity_account'] = self.activity_account
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
        o = KoubeiMarketingToolPointsQueryModel()
        if 'activity_account' in d:
            o.activity_account = d['activity_account']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


