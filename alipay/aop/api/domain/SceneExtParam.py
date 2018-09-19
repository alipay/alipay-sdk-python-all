#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneExtParam(object):

    def __init__(self):
        self._apply_reason = None
        self._contract_no = None
        self._discountamt = None
        self._firstpayamt = None
        self._interestrate = None
        self._lastpayamt = None
        self._monthpayamt = None
        self._remark = None

    @property
    def apply_reason(self):
        return self._apply_reason

    @apply_reason.setter
    def apply_reason(self, value):
        self._apply_reason = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def discountamt(self):
        return self._discountamt

    @discountamt.setter
    def discountamt(self, value):
        self._discountamt = value
    @property
    def firstpayamt(self):
        return self._firstpayamt

    @firstpayamt.setter
    def firstpayamt(self, value):
        self._firstpayamt = value
    @property
    def interestrate(self):
        return self._interestrate

    @interestrate.setter
    def interestrate(self, value):
        self._interestrate = value
    @property
    def lastpayamt(self):
        return self._lastpayamt

    @lastpayamt.setter
    def lastpayamt(self, value):
        self._lastpayamt = value
    @property
    def monthpayamt(self):
        return self._monthpayamt

    @monthpayamt.setter
    def monthpayamt(self, value):
        self._monthpayamt = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_reason:
            if hasattr(self.apply_reason, 'to_alipay_dict'):
                params['apply_reason'] = self.apply_reason.to_alipay_dict()
            else:
                params['apply_reason'] = self.apply_reason
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.discountamt:
            if hasattr(self.discountamt, 'to_alipay_dict'):
                params['discountamt'] = self.discountamt.to_alipay_dict()
            else:
                params['discountamt'] = self.discountamt
        if self.firstpayamt:
            if hasattr(self.firstpayamt, 'to_alipay_dict'):
                params['firstpayamt'] = self.firstpayamt.to_alipay_dict()
            else:
                params['firstpayamt'] = self.firstpayamt
        if self.interestrate:
            if hasattr(self.interestrate, 'to_alipay_dict'):
                params['interestrate'] = self.interestrate.to_alipay_dict()
            else:
                params['interestrate'] = self.interestrate
        if self.lastpayamt:
            if hasattr(self.lastpayamt, 'to_alipay_dict'):
                params['lastpayamt'] = self.lastpayamt.to_alipay_dict()
            else:
                params['lastpayamt'] = self.lastpayamt
        if self.monthpayamt:
            if hasattr(self.monthpayamt, 'to_alipay_dict'):
                params['monthpayamt'] = self.monthpayamt.to_alipay_dict()
            else:
                params['monthpayamt'] = self.monthpayamt
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneExtParam()
        if 'apply_reason' in d:
            o.apply_reason = d['apply_reason']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'discountamt' in d:
            o.discountamt = d['discountamt']
        if 'firstpayamt' in d:
            o.firstpayamt = d['firstpayamt']
        if 'interestrate' in d:
            o.interestrate = d['interestrate']
        if 'lastpayamt' in d:
            o.lastpayamt = d['lastpayamt']
        if 'monthpayamt' in d:
            o.monthpayamt = d['monthpayamt']
        if 'remark' in d:
            o.remark = d['remark']
        return o


