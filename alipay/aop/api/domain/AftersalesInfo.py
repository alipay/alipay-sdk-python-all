#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersalesInfo(object):

    def __init__(self):
        self._aftersales_id = None
        self._aftersales_status = None
        self._card_id = None
        self._consult_damages_cash = None
        self._consult_refund_cash = None
        self._create_time = None
        self._damages_cash = None
        self._desc = None
        self._proofs = None
        self._reason = None

    @property
    def aftersales_id(self):
        return self._aftersales_id

    @aftersales_id.setter
    def aftersales_id(self, value):
        self._aftersales_id = value
    @property
    def aftersales_status(self):
        return self._aftersales_status

    @aftersales_status.setter
    def aftersales_status(self, value):
        self._aftersales_status = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def consult_damages_cash(self):
        return self._consult_damages_cash

    @consult_damages_cash.setter
    def consult_damages_cash(self, value):
        self._consult_damages_cash = value
    @property
    def consult_refund_cash(self):
        return self._consult_refund_cash

    @consult_refund_cash.setter
    def consult_refund_cash(self, value):
        self._consult_refund_cash = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def damages_cash(self):
        return self._damages_cash

    @damages_cash.setter
    def damages_cash(self, value):
        self._damages_cash = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def proofs(self):
        return self._proofs

    @proofs.setter
    def proofs(self, value):
        if isinstance(value, list):
            self._proofs = list()
            for i in value:
                self._proofs.append(i)
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersales_id:
            if hasattr(self.aftersales_id, 'to_alipay_dict'):
                params['aftersales_id'] = self.aftersales_id.to_alipay_dict()
            else:
                params['aftersales_id'] = self.aftersales_id
        if self.aftersales_status:
            if hasattr(self.aftersales_status, 'to_alipay_dict'):
                params['aftersales_status'] = self.aftersales_status.to_alipay_dict()
            else:
                params['aftersales_status'] = self.aftersales_status
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.consult_damages_cash:
            if hasattr(self.consult_damages_cash, 'to_alipay_dict'):
                params['consult_damages_cash'] = self.consult_damages_cash.to_alipay_dict()
            else:
                params['consult_damages_cash'] = self.consult_damages_cash
        if self.consult_refund_cash:
            if hasattr(self.consult_refund_cash, 'to_alipay_dict'):
                params['consult_refund_cash'] = self.consult_refund_cash.to_alipay_dict()
            else:
                params['consult_refund_cash'] = self.consult_refund_cash
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.damages_cash:
            if hasattr(self.damages_cash, 'to_alipay_dict'):
                params['damages_cash'] = self.damages_cash.to_alipay_dict()
            else:
                params['damages_cash'] = self.damages_cash
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.proofs:
            if isinstance(self.proofs, list):
                for i in range(0, len(self.proofs)):
                    element = self.proofs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.proofs[i] = element.to_alipay_dict()
            if hasattr(self.proofs, 'to_alipay_dict'):
                params['proofs'] = self.proofs.to_alipay_dict()
            else:
                params['proofs'] = self.proofs
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersalesInfo()
        if 'aftersales_id' in d:
            o.aftersales_id = d['aftersales_id']
        if 'aftersales_status' in d:
            o.aftersales_status = d['aftersales_status']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'consult_damages_cash' in d:
            o.consult_damages_cash = d['consult_damages_cash']
        if 'consult_refund_cash' in d:
            o.consult_refund_cash = d['consult_refund_cash']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'damages_cash' in d:
            o.damages_cash = d['damages_cash']
        if 'desc' in d:
            o.desc = d['desc']
        if 'proofs' in d:
            o.proofs = d['proofs']
        if 'reason' in d:
            o.reason = d['reason']
        return o


