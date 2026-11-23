#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPointConsultModel(object):

    def __init__(self):
        self._amount = None
        self._open_id = None
        self._promo_scene = None
        self._promo_scene_key = None
        self._scene_code = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def promo_scene(self):
        return self._promo_scene

    @promo_scene.setter
    def promo_scene(self, value):
        self._promo_scene = value
    @property
    def promo_scene_key(self):
        return self._promo_scene_key

    @promo_scene_key.setter
    def promo_scene_key(self, value):
        self._promo_scene_key = value
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
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.promo_scene:
            if hasattr(self.promo_scene, 'to_alipay_dict'):
                params['promo_scene'] = self.promo_scene.to_alipay_dict()
            else:
                params['promo_scene'] = self.promo_scene
        if self.promo_scene_key:
            if hasattr(self.promo_scene_key, 'to_alipay_dict'):
                params['promo_scene_key'] = self.promo_scene_key.to_alipay_dict()
            else:
                params['promo_scene_key'] = self.promo_scene_key
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
        o = AlipayCommerceAcommunicationPointConsultModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'promo_scene' in d:
            o.promo_scene = d['promo_scene']
        if 'promo_scene_key' in d:
            o.promo_scene_key = d['promo_scene_key']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


