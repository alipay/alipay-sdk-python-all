#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCreditAutofinanceLoanCloseModel(object):

    def __init__(self):
        self._applyno = None
        self._orgcode = None
        self._outorderno = None
        self._reson = None
        self._type = None

    @property
    def applyno(self):
        return self._applyno

    @applyno.setter
    def applyno(self, value):
        self._applyno = value
    @property
    def orgcode(self):
        return self._orgcode

    @orgcode.setter
    def orgcode(self, value):
        self._orgcode = value
    @property
    def outorderno(self):
        return self._outorderno

    @outorderno.setter
    def outorderno(self, value):
        self._outorderno = value
    @property
    def reson(self):
        return self._reson

    @reson.setter
    def reson(self, value):
        self._reson = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.applyno:
            if hasattr(self.applyno, 'to_alipay_dict'):
                params['applyno'] = self.applyno.to_alipay_dict()
            else:
                params['applyno'] = self.applyno
        if self.orgcode:
            if hasattr(self.orgcode, 'to_alipay_dict'):
                params['orgcode'] = self.orgcode.to_alipay_dict()
            else:
                params['orgcode'] = self.orgcode
        if self.outorderno:
            if hasattr(self.outorderno, 'to_alipay_dict'):
                params['outorderno'] = self.outorderno.to_alipay_dict()
            else:
                params['outorderno'] = self.outorderno
        if self.reson:
            if hasattr(self.reson, 'to_alipay_dict'):
                params['reson'] = self.reson.to_alipay_dict()
            else:
                params['reson'] = self.reson
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCreditAutofinanceLoanCloseModel()
        if 'applyno' in d:
            o.applyno = d['applyno']
        if 'orgcode' in d:
            o.orgcode = d['orgcode']
        if 'outorderno' in d:
            o.outorderno = d['outorderno']
        if 'reson' in d:
            o.reson = d['reson']
        if 'type' in d:
            o.type = d['type']
        return o


