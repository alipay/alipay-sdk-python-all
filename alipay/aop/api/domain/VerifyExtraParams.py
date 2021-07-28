#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifyExtraParams(object):

    def __init__(self):
        self._idfa = None
        self._imei = None
        self._imsi = None
        self._oaid = None
        self._umid = None
        self._utdid = None

    @property
    def idfa(self):
        return self._idfa

    @idfa.setter
    def idfa(self, value):
        self._idfa = value
    @property
    def imei(self):
        return self._imei

    @imei.setter
    def imei(self, value):
        self._imei = value
    @property
    def imsi(self):
        return self._imsi

    @imsi.setter
    def imsi(self, value):
        self._imsi = value
    @property
    def oaid(self):
        return self._oaid

    @oaid.setter
    def oaid(self, value):
        self._oaid = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def utdid(self):
        return self._utdid

    @utdid.setter
    def utdid(self, value):
        self._utdid = value


    def to_alipay_dict(self):
        params = dict()
        if self.idfa:
            if hasattr(self.idfa, 'to_alipay_dict'):
                params['idfa'] = self.idfa.to_alipay_dict()
            else:
                params['idfa'] = self.idfa
        if self.imei:
            if hasattr(self.imei, 'to_alipay_dict'):
                params['imei'] = self.imei.to_alipay_dict()
            else:
                params['imei'] = self.imei
        if self.imsi:
            if hasattr(self.imsi, 'to_alipay_dict'):
                params['imsi'] = self.imsi.to_alipay_dict()
            else:
                params['imsi'] = self.imsi
        if self.oaid:
            if hasattr(self.oaid, 'to_alipay_dict'):
                params['oaid'] = self.oaid.to_alipay_dict()
            else:
                params['oaid'] = self.oaid
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = self.umid.to_alipay_dict()
            else:
                params['umid'] = self.umid
        if self.utdid:
            if hasattr(self.utdid, 'to_alipay_dict'):
                params['utdid'] = self.utdid.to_alipay_dict()
            else:
                params['utdid'] = self.utdid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyExtraParams()
        if 'idfa' in d:
            o.idfa = d['idfa']
        if 'imei' in d:
            o.imei = d['imei']
        if 'imsi' in d:
            o.imsi = d['imsi']
        if 'oaid' in d:
            o.oaid = d['oaid']
        if 'umid' in d:
            o.umid = d['umid']
        if 'utdid' in d:
            o.utdid = d['utdid']
        return o


