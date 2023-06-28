#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationOpenbizmockTestcertificateQueryModel(object):

    def __init__(self):
        self._hahaha = None
        self._keykey = None
        self._keykey_openid = None
        self._lalala = None
        self._open_id = None
        self._uid = None

    @property
    def hahaha(self):
        return self._hahaha

    @hahaha.setter
    def hahaha(self, value):
        self._hahaha = value
    @property
    def keykey(self):
        return self._keykey

    @keykey.setter
    def keykey(self, value):
        self._keykey = value
    @property
    def keykey_openid(self):
        return self._keykey_openid

    @keykey_openid.setter
    def keykey_openid(self, value):
        self._keykey_openid = value
    @property
    def lalala(self):
        return self._lalala

    @lalala.setter
    def lalala(self, value):
        self._lalala = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.hahaha:
            if hasattr(self.hahaha, 'to_alipay_dict'):
                params['hahaha'] = self.hahaha.to_alipay_dict()
            else:
                params['hahaha'] = self.hahaha
        if self.keykey:
            if hasattr(self.keykey, 'to_alipay_dict'):
                params['keykey'] = self.keykey.to_alipay_dict()
            else:
                params['keykey'] = self.keykey
        if self.keykey_openid:
            if hasattr(self.keykey_openid, 'to_alipay_dict'):
                params['keykey_openid'] = self.keykey_openid.to_alipay_dict()
            else:
                params['keykey_openid'] = self.keykey_openid
        if self.lalala:
            if hasattr(self.lalala, 'to_alipay_dict'):
                params['lalala'] = self.lalala.to_alipay_dict()
            else:
                params['lalala'] = self.lalala
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationOpenbizmockTestcertificateQueryModel()
        if 'hahaha' in d:
            o.hahaha = d['hahaha']
        if 'keykey' in d:
            o.keykey = d['keykey']
        if 'keykey_openid' in d:
            o.keykey_openid = d['keykey_openid']
        if 'lalala' in d:
            o.lalala = d['lalala']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


