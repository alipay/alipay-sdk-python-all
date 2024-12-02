#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DamagesConsultInfo(object):

    def __init__(self):
        self._can_close = None
        self._damages_cash = None
        self._damages_rate = None
        self._damages_type = None
        self._need_damages = None
        self._refund_cash = None
        self._refuse_close_reason = None

    @property
    def can_close(self):
        return self._can_close

    @can_close.setter
    def can_close(self, value):
        self._can_close = value
    @property
    def damages_cash(self):
        return self._damages_cash

    @damages_cash.setter
    def damages_cash(self, value):
        self._damages_cash = value
    @property
    def damages_rate(self):
        return self._damages_rate

    @damages_rate.setter
    def damages_rate(self, value):
        self._damages_rate = value
    @property
    def damages_type(self):
        return self._damages_type

    @damages_type.setter
    def damages_type(self, value):
        self._damages_type = value
    @property
    def need_damages(self):
        return self._need_damages

    @need_damages.setter
    def need_damages(self, value):
        self._need_damages = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def refuse_close_reason(self):
        return self._refuse_close_reason

    @refuse_close_reason.setter
    def refuse_close_reason(self, value):
        self._refuse_close_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_close:
            if hasattr(self.can_close, 'to_alipay_dict'):
                params['can_close'] = self.can_close.to_alipay_dict()
            else:
                params['can_close'] = self.can_close
        if self.damages_cash:
            if hasattr(self.damages_cash, 'to_alipay_dict'):
                params['damages_cash'] = self.damages_cash.to_alipay_dict()
            else:
                params['damages_cash'] = self.damages_cash
        if self.damages_rate:
            if hasattr(self.damages_rate, 'to_alipay_dict'):
                params['damages_rate'] = self.damages_rate.to_alipay_dict()
            else:
                params['damages_rate'] = self.damages_rate
        if self.damages_type:
            if hasattr(self.damages_type, 'to_alipay_dict'):
                params['damages_type'] = self.damages_type.to_alipay_dict()
            else:
                params['damages_type'] = self.damages_type
        if self.need_damages:
            if hasattr(self.need_damages, 'to_alipay_dict'):
                params['need_damages'] = self.need_damages.to_alipay_dict()
            else:
                params['need_damages'] = self.need_damages
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.refuse_close_reason:
            if hasattr(self.refuse_close_reason, 'to_alipay_dict'):
                params['refuse_close_reason'] = self.refuse_close_reason.to_alipay_dict()
            else:
                params['refuse_close_reason'] = self.refuse_close_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DamagesConsultInfo()
        if 'can_close' in d:
            o.can_close = d['can_close']
        if 'damages_cash' in d:
            o.damages_cash = d['damages_cash']
        if 'damages_rate' in d:
            o.damages_rate = d['damages_rate']
        if 'damages_type' in d:
            o.damages_type = d['damages_type']
        if 'need_damages' in d:
            o.need_damages = d['need_damages']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'refuse_close_reason' in d:
            o.refuse_close_reason = d['refuse_close_reason']
        return o


