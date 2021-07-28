#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVO(object):

    def __init__(self):
        self._apply_amount = None
        self._apply_date = None
        self._apply_no = None
        self._ccy = None
        self._effect_date = None
        self._ext_info = None
        self._repay_date = None
        self._status = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def ccy(self):
        return self._ccy

    @ccy.setter
    def ccy(self, value):
        self._ccy = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def repay_date(self):
        return self._repay_date

    @repay_date.setter
    def repay_date(self, value):
        self._repay_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.ccy:
            if hasattr(self.ccy, 'to_alipay_dict'):
                params['ccy'] = self.ccy.to_alipay_dict()
            else:
                params['ccy'] = self.ccy
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.repay_date:
            if hasattr(self.repay_date, 'to_alipay_dict'):
                params['repay_date'] = self.repay_date.to_alipay_dict()
            else:
                params['repay_date'] = self.repay_date
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVO()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'ccy' in d:
            o.ccy = d['ccy']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'repay_date' in d:
            o.repay_date = d['repay_date']
        if 'status' in d:
            o.status = d['status']
        return o


