#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransAuctionBalanceQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._inst_id = None
        self._user_id = None
        self._verify_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransAuctionBalanceQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


