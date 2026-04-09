#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTagClaimAddModel(object):

    def __init__(self):
        self._alipay_account = None
        self._qrcode_list = None
        self._store_id = None
        self._store_id_type = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def qrcode_list(self):
        return self._qrcode_list

    @qrcode_list.setter
    def qrcode_list(self, value):
        if isinstance(value, list):
            self._qrcode_list = list()
            for i in value:
                self._qrcode_list.append(i)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_id_type(self):
        return self._store_id_type

    @store_id_type.setter
    def store_id_type(self, value):
        self._store_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.qrcode_list:
            if isinstance(self.qrcode_list, list):
                for i in range(0, len(self.qrcode_list)):
                    element = self.qrcode_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qrcode_list[i] = element.to_alipay_dict()
            if hasattr(self.qrcode_list, 'to_alipay_dict'):
                params['qrcode_list'] = self.qrcode_list.to_alipay_dict()
            else:
                params['qrcode_list'] = self.qrcode_list
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_id_type:
            if hasattr(self.store_id_type, 'to_alipay_dict'):
                params['store_id_type'] = self.store_id_type.to_alipay_dict()
            else:
                params['store_id_type'] = self.store_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTagClaimAddModel()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'qrcode_list' in d:
            o.qrcode_list = d['qrcode_list']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_id_type' in d:
            o.store_id_type = d['store_id_type']
        return o


