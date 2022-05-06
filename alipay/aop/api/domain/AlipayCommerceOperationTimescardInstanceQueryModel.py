#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTimescardInstanceQueryModel(object):

    def __init__(self):
        self._card_id = None
        self._isv_partner_id = None
        self._partner_id = None
        self._scene_code = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def isv_partner_id(self):
        return self._isv_partner_id

    @isv_partner_id.setter
    def isv_partner_id(self, value):
        self._isv_partner_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.isv_partner_id:
            if hasattr(self.isv_partner_id, 'to_alipay_dict'):
                params['isv_partner_id'] = self.isv_partner_id.to_alipay_dict()
            else:
                params['isv_partner_id'] = self.isv_partner_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
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
        o = AlipayCommerceOperationTimescardInstanceQueryModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'isv_partner_id' in d:
            o.isv_partner_id = d['isv_partner_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


