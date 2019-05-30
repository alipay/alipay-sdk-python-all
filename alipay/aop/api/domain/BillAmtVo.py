#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO


class BillAmtVo(object):

    def __init__(self):
        self._int_amt = None
        self._ovd_int_amt = None
        self._ovd_prin_amt = None
        self._pen_int_amt = None
        self._pen_prin_amt = None
        self._prin_amt = None

    @property
    def int_amt(self):
        return self._int_amt

    @int_amt.setter
    def int_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._int_amt = value
        else:
            self._int_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def ovd_int_amt(self):
        return self._ovd_int_amt

    @ovd_int_amt.setter
    def ovd_int_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._ovd_int_amt = value
        else:
            self._ovd_int_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def ovd_prin_amt(self):
        return self._ovd_prin_amt

    @ovd_prin_amt.setter
    def ovd_prin_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._ovd_prin_amt = value
        else:
            self._ovd_prin_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def pen_int_amt(self):
        return self._pen_int_amt

    @pen_int_amt.setter
    def pen_int_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._pen_int_amt = value
        else:
            self._pen_int_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def pen_prin_amt(self):
        return self._pen_prin_amt

    @pen_prin_amt.setter
    def pen_prin_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._pen_prin_amt = value
        else:
            self._pen_prin_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)
    @property
    def prin_amt(self):
        return self._prin_amt

    @prin_amt.setter
    def prin_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._prin_amt = value
        else:
            self._prin_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.int_amt:
            if hasattr(self.int_amt, 'to_alipay_dict'):
                params['int_amt'] = self.int_amt.to_alipay_dict()
            else:
                params['int_amt'] = self.int_amt
        if self.ovd_int_amt:
            if hasattr(self.ovd_int_amt, 'to_alipay_dict'):
                params['ovd_int_amt'] = self.ovd_int_amt.to_alipay_dict()
            else:
                params['ovd_int_amt'] = self.ovd_int_amt
        if self.ovd_prin_amt:
            if hasattr(self.ovd_prin_amt, 'to_alipay_dict'):
                params['ovd_prin_amt'] = self.ovd_prin_amt.to_alipay_dict()
            else:
                params['ovd_prin_amt'] = self.ovd_prin_amt
        if self.pen_int_amt:
            if hasattr(self.pen_int_amt, 'to_alipay_dict'):
                params['pen_int_amt'] = self.pen_int_amt.to_alipay_dict()
            else:
                params['pen_int_amt'] = self.pen_int_amt
        if self.pen_prin_amt:
            if hasattr(self.pen_prin_amt, 'to_alipay_dict'):
                params['pen_prin_amt'] = self.pen_prin_amt.to_alipay_dict()
            else:
                params['pen_prin_amt'] = self.pen_prin_amt
        if self.prin_amt:
            if hasattr(self.prin_amt, 'to_alipay_dict'):
                params['prin_amt'] = self.prin_amt.to_alipay_dict()
            else:
                params['prin_amt'] = self.prin_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillAmtVo()
        if 'int_amt' in d:
            o.int_amt = d['int_amt']
        if 'ovd_int_amt' in d:
            o.ovd_int_amt = d['ovd_int_amt']
        if 'ovd_prin_amt' in d:
            o.ovd_prin_amt = d['ovd_prin_amt']
        if 'pen_int_amt' in d:
            o.pen_int_amt = d['pen_int_amt']
        if 'pen_prin_amt' in d:
            o.pen_prin_amt = d['pen_prin_amt']
        if 'prin_amt' in d:
            o.prin_amt = d['prin_amt']
        return o


