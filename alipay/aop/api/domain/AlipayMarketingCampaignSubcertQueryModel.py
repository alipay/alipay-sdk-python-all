#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignSubcertQueryModel(object):

    def __init__(self):
        self._login_id = None
        self._lot_num = None
        self._user_id = None

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def lot_num(self):
        return self._lot_num

    @lot_num.setter
    def lot_num(self, value):
        self._lot_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        if self.lot_num:
            if hasattr(self.lot_num, 'to_alipay_dict'):
                params['lot_num'] = self.lot_num.to_alipay_dict()
            else:
                params['lot_num'] = self.lot_num
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
        o = AlipayMarketingCampaignSubcertQueryModel()
        if 'login_id' in d:
            o.login_id = d['login_id']
        if 'lot_num' in d:
            o.lot_num = d['lot_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


