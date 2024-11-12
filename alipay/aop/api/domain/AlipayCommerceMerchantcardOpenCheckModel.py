#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardOpenCheckModel(object):

    def __init__(self):
        self._card_types = None
        self._mcc_code = None
        self._need_auth = None
        self._pid = None

    @property
    def card_types(self):
        return self._card_types

    @card_types.setter
    def card_types(self, value):
        if isinstance(value, list):
            self._card_types = list()
            for i in value:
                self._card_types.append(i)
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def need_auth(self):
        return self._need_auth

    @need_auth.setter
    def need_auth(self, value):
        self._need_auth = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_types:
            if isinstance(self.card_types, list):
                for i in range(0, len(self.card_types)):
                    element = self.card_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_types[i] = element.to_alipay_dict()
            if hasattr(self.card_types, 'to_alipay_dict'):
                params['card_types'] = self.card_types.to_alipay_dict()
            else:
                params['card_types'] = self.card_types
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.need_auth:
            if hasattr(self.need_auth, 'to_alipay_dict'):
                params['need_auth'] = self.need_auth.to_alipay_dict()
            else:
                params['need_auth'] = self.need_auth
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardOpenCheckModel()
        if 'card_types' in d:
            o.card_types = d['card_types']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'need_auth' in d:
            o.need_auth = d['need_auth']
        if 'pid' in d:
            o.pid = d['pid']
        return o


