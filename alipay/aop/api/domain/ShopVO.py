#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopVO(object):

    def __init__(self):
        self._auth_state = None
        self._purchaser_id = None
        self._shop_code = None
        self._shop_name = None

    @property
    def auth_state(self):
        return self._auth_state

    @auth_state.setter
    def auth_state(self, value):
        self._auth_state = value
    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_state:
            if hasattr(self.auth_state, 'to_alipay_dict'):
                params['auth_state'] = self.auth_state.to_alipay_dict()
            else:
                params['auth_state'] = self.auth_state
        if self.purchaser_id:
            if hasattr(self.purchaser_id, 'to_alipay_dict'):
                params['purchaser_id'] = self.purchaser_id.to_alipay_dict()
            else:
                params['purchaser_id'] = self.purchaser_id
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopVO()
        if 'auth_state' in d:
            o.auth_state = d['auth_state']
        if 'purchaser_id' in d:
            o.purchaser_id = d['purchaser_id']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


