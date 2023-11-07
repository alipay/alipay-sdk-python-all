#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundMbpcardCardBindModel(object):

    def __init__(self):
        self._alipay_identity_id = None
        self._alipay_identity_type = None
        self._bind_user_name = None
        self._biz_scene = None
        self._card_no = None
        self._card_password = None
        self._open_id = None
        self._product_code = None

    @property
    def alipay_identity_id(self):
        return self._alipay_identity_id

    @alipay_identity_id.setter
    def alipay_identity_id(self, value):
        self._alipay_identity_id = value
    @property
    def alipay_identity_type(self):
        return self._alipay_identity_type

    @alipay_identity_type.setter
    def alipay_identity_type(self, value):
        self._alipay_identity_type = value
    @property
    def bind_user_name(self):
        return self._bind_user_name

    @bind_user_name.setter
    def bind_user_name(self, value):
        self._bind_user_name = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_password(self):
        return self._card_password

    @card_password.setter
    def card_password(self, value):
        self._card_password = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_identity_id:
            if hasattr(self.alipay_identity_id, 'to_alipay_dict'):
                params['alipay_identity_id'] = self.alipay_identity_id.to_alipay_dict()
            else:
                params['alipay_identity_id'] = self.alipay_identity_id
        if self.alipay_identity_type:
            if hasattr(self.alipay_identity_type, 'to_alipay_dict'):
                params['alipay_identity_type'] = self.alipay_identity_type.to_alipay_dict()
            else:
                params['alipay_identity_type'] = self.alipay_identity_type
        if self.bind_user_name:
            if hasattr(self.bind_user_name, 'to_alipay_dict'):
                params['bind_user_name'] = self.bind_user_name.to_alipay_dict()
            else:
                params['bind_user_name'] = self.bind_user_name
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_password:
            if hasattr(self.card_password, 'to_alipay_dict'):
                params['card_password'] = self.card_password.to_alipay_dict()
            else:
                params['card_password'] = self.card_password
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundMbpcardCardBindModel()
        if 'alipay_identity_id' in d:
            o.alipay_identity_id = d['alipay_identity_id']
        if 'alipay_identity_type' in d:
            o.alipay_identity_type = d['alipay_identity_type']
        if 'bind_user_name' in d:
            o.bind_user_name = d['bind_user_name']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_password' in d:
            o.card_password = d['card_password']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


