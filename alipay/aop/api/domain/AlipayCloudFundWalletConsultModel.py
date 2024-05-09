#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudFundWalletConsultModel(object):

    def __init__(self):
        self._search_type = None
        self._user_wallet_id = None

    @property
    def search_type(self):
        return self._search_type

    @search_type.setter
    def search_type(self, value):
        self._search_type = value
    @property
    def user_wallet_id(self):
        return self._user_wallet_id

    @user_wallet_id.setter
    def user_wallet_id(self, value):
        self._user_wallet_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.search_type:
            if hasattr(self.search_type, 'to_alipay_dict'):
                params['search_type'] = self.search_type.to_alipay_dict()
            else:
                params['search_type'] = self.search_type
        if self.user_wallet_id:
            if hasattr(self.user_wallet_id, 'to_alipay_dict'):
                params['user_wallet_id'] = self.user_wallet_id.to_alipay_dict()
            else:
                params['user_wallet_id'] = self.user_wallet_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudFundWalletConsultModel()
        if 'search_type' in d:
            o.search_type = d['search_type']
        if 'user_wallet_id' in d:
            o.user_wallet_id = d['user_wallet_id']
        return o


