#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCreditAutofinanceLoanPlanQueryModel(object):

    def __init__(self):
        self._extparam = None
        self._orgcode = None
        self._productcode = None
        self._seqno = None
        self._uid = None

    @property
    def extparam(self):
        return self._extparam

    @extparam.setter
    def extparam(self, value):
        self._extparam = value
    @property
    def orgcode(self):
        return self._orgcode

    @orgcode.setter
    def orgcode(self, value):
        self._orgcode = value
    @property
    def productcode(self):
        return self._productcode

    @productcode.setter
    def productcode(self, value):
        self._productcode = value
    @property
    def seqno(self):
        return self._seqno

    @seqno.setter
    def seqno(self, value):
        self._seqno = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.extparam:
            if hasattr(self.extparam, 'to_alipay_dict'):
                params['extparam'] = self.extparam.to_alipay_dict()
            else:
                params['extparam'] = self.extparam
        if self.orgcode:
            if hasattr(self.orgcode, 'to_alipay_dict'):
                params['orgcode'] = self.orgcode.to_alipay_dict()
            else:
                params['orgcode'] = self.orgcode
        if self.productcode:
            if hasattr(self.productcode, 'to_alipay_dict'):
                params['productcode'] = self.productcode.to_alipay_dict()
            else:
                params['productcode'] = self.productcode
        if self.seqno:
            if hasattr(self.seqno, 'to_alipay_dict'):
                params['seqno'] = self.seqno.to_alipay_dict()
            else:
                params['seqno'] = self.seqno
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
        o = AlipayCreditAutofinanceLoanPlanQueryModel()
        if 'extparam' in d:
            o.extparam = d['extparam']
        if 'orgcode' in d:
            o.orgcode = d['orgcode']
        if 'productcode' in d:
            o.productcode = d['productcode']
        if 'seqno' in d:
            o.seqno = d['seqno']
        if 'uid' in d:
            o.uid = d['uid']
        return o


