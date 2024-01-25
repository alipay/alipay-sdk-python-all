#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderAftersaleQueryModel(object):

    def __init__(self):
        self._aftersale_id = None
        self._open_id = None
        self._out_aftersale_id = None
        self._user_id = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersale_id:
            if hasattr(self.aftersale_id, 'to_alipay_dict'):
                params['aftersale_id'] = self.aftersale_id.to_alipay_dict()
            else:
                params['aftersale_id'] = self.aftersale_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_aftersale_id:
            if hasattr(self.out_aftersale_id, 'to_alipay_dict'):
                params['out_aftersale_id'] = self.out_aftersale_id.to_alipay_dict()
            else:
                params['out_aftersale_id'] = self.out_aftersale_id
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
        o = AlipayOpenMiniOrderAftersaleQueryModel()
        if 'aftersale_id' in d:
            o.aftersale_id = d['aftersale_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_aftersale_id' in d:
            o.out_aftersale_id = d['out_aftersale_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


