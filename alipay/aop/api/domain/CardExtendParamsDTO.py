#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardExtendParamsDTO(object):

    def __init__(self):
        self._inst_id = None
        self._inst_name = None
        self._open_wallet = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        if isinstance(value, list):
            self._inst_id = list()
            for i in value:
                self._inst_id.append(i)
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        if isinstance(value, list):
            self._inst_name = list()
            for i in value:
                self._inst_name.append(i)
    @property
    def open_wallet(self):
        return self._open_wallet

    @open_wallet.setter
    def open_wallet(self, value):
        self._open_wallet = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if isinstance(self.inst_id, list):
                for i in range(0, len(self.inst_id)):
                    element = self.inst_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_id[i] = element.to_alipay_dict()
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_name:
            if isinstance(self.inst_name, list):
                for i in range(0, len(self.inst_name)):
                    element = self.inst_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_name[i] = element.to_alipay_dict()
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.open_wallet:
            if hasattr(self.open_wallet, 'to_alipay_dict'):
                params['open_wallet'] = self.open_wallet.to_alipay_dict()
            else:
                params['open_wallet'] = self.open_wallet
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardExtendParamsDTO()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'open_wallet' in d:
            o.open_wallet = d['open_wallet']
        return o


