#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiShopMallMemberIdentifyModel(object):

    def __init__(self):
        self._mall_id = None
        self._user_id = None

    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
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
        o = KoubeiShopMallMemberIdentifyModel()
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


