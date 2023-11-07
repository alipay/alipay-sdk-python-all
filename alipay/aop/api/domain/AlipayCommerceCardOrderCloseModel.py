#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCardOrderCloseModel(object):

    def __init__(self):
        self._card_id = None
        self._user_id = None
        self._user_id_open_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_id_open_id(self):
        return self._user_id_open_id

    @user_id_open_id.setter
    def user_id_open_id(self, value):
        self._user_id_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_id_open_id:
            if hasattr(self.user_id_open_id, 'to_alipay_dict'):
                params['user_id_open_id'] = self.user_id_open_id.to_alipay_dict()
            else:
                params['user_id_open_id'] = self.user_id_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCardOrderCloseModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_open_id' in d:
            o.user_id_open_id = d['user_id_open_id']
        return o


