#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillServiceInfo(object):

    def __init__(self):
        self._address = None
        self._billkey_type = None
        self._cipher_billkey = None
        self._current_ladder = None
        self._end_time = None
        self._out_biz_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def billkey_type(self):
        return self._billkey_type

    @billkey_type.setter
    def billkey_type(self, value):
        self._billkey_type = value
    @property
    def cipher_billkey(self):
        return self._cipher_billkey

    @cipher_billkey.setter
    def cipher_billkey(self, value):
        self._cipher_billkey = value
    @property
    def current_ladder(self):
        return self._current_ladder

    @current_ladder.setter
    def current_ladder(self, value):
        self._current_ladder = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.billkey_type:
            if hasattr(self.billkey_type, 'to_alipay_dict'):
                params['billkey_type'] = self.billkey_type.to_alipay_dict()
            else:
                params['billkey_type'] = self.billkey_type
        if self.cipher_billkey:
            if hasattr(self.cipher_billkey, 'to_alipay_dict'):
                params['cipher_billkey'] = self.cipher_billkey.to_alipay_dict()
            else:
                params['cipher_billkey'] = self.cipher_billkey
        if self.current_ladder:
            if hasattr(self.current_ladder, 'to_alipay_dict'):
                params['current_ladder'] = self.current_ladder.to_alipay_dict()
            else:
                params['current_ladder'] = self.current_ladder
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillServiceInfo()
        if 'address' in d:
            o.address = d['address']
        if 'billkey_type' in d:
            o.billkey_type = d['billkey_type']
        if 'cipher_billkey' in d:
            o.cipher_billkey = d['cipher_billkey']
        if 'current_ladder' in d:
            o.current_ladder = d['current_ladder']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        return o


