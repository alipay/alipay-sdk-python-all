#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtraInfoVO(object):

    def __init__(self):
        self._maomao_friend = None
        self._maomao_register = None
        self._taobao_id = None

    @property
    def maomao_friend(self):
        return self._maomao_friend

    @maomao_friend.setter
    def maomao_friend(self, value):
        self._maomao_friend = value
    @property
    def maomao_register(self):
        return self._maomao_register

    @maomao_register.setter
    def maomao_register(self, value):
        self._maomao_register = value
    @property
    def taobao_id(self):
        return self._taobao_id

    @taobao_id.setter
    def taobao_id(self, value):
        self._taobao_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.maomao_friend:
            if hasattr(self.maomao_friend, 'to_alipay_dict'):
                params['maomao_friend'] = self.maomao_friend.to_alipay_dict()
            else:
                params['maomao_friend'] = self.maomao_friend
        if self.maomao_register:
            if hasattr(self.maomao_register, 'to_alipay_dict'):
                params['maomao_register'] = self.maomao_register.to_alipay_dict()
            else:
                params['maomao_register'] = self.maomao_register
        if self.taobao_id:
            if hasattr(self.taobao_id, 'to_alipay_dict'):
                params['taobao_id'] = self.taobao_id.to_alipay_dict()
            else:
                params['taobao_id'] = self.taobao_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtraInfoVO()
        if 'maomao_friend' in d:
            o.maomao_friend = d['maomao_friend']
        if 'maomao_register' in d:
            o.maomao_register = d['maomao_register']
        if 'taobao_id' in d:
            o.taobao_id = d['taobao_id']
        return o


