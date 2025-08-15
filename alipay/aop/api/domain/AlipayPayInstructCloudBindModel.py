#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayInstructCloudBindModel(object):

    def __init__(self):
        self._n_sn = None
        self._pairing_code = None
        self._pos_id = None
        self._store_name = None

    @property
    def n_sn(self):
        return self._n_sn

    @n_sn.setter
    def n_sn(self, value):
        self._n_sn = value
    @property
    def pairing_code(self):
        return self._pairing_code

    @pairing_code.setter
    def pairing_code(self, value):
        self._pairing_code = value
    @property
    def pos_id(self):
        return self._pos_id

    @pos_id.setter
    def pos_id(self, value):
        self._pos_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.n_sn:
            if hasattr(self.n_sn, 'to_alipay_dict'):
                params['n_sn'] = self.n_sn.to_alipay_dict()
            else:
                params['n_sn'] = self.n_sn
        if self.pairing_code:
            if hasattr(self.pairing_code, 'to_alipay_dict'):
                params['pairing_code'] = self.pairing_code.to_alipay_dict()
            else:
                params['pairing_code'] = self.pairing_code
        if self.pos_id:
            if hasattr(self.pos_id, 'to_alipay_dict'):
                params['pos_id'] = self.pos_id.to_alipay_dict()
            else:
                params['pos_id'] = self.pos_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayInstructCloudBindModel()
        if 'n_sn' in d:
            o.n_sn = d['n_sn']
        if 'pairing_code' in d:
            o.pairing_code = d['pairing_code']
        if 'pos_id' in d:
            o.pos_id = d['pos_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


