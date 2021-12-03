#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankLogTransferFormNew(object):

    def __init__(self):
        self._charge_amount = None
        self._chargeccy = None
        self._crossccy_flag = None
        self._exchange = None
        self._id = None
        self._inst_id = None
        self._ip_role_id = None
        self._is_recharge_receipt = None
        self._memo = None
        self._target = None
        self._trans_dt = None

    @property
    def charge_amount(self):
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, value):
        self._charge_amount = value
    @property
    def chargeccy(self):
        return self._chargeccy

    @chargeccy.setter
    def chargeccy(self, value):
        self._chargeccy = value
    @property
    def crossccy_flag(self):
        return self._crossccy_flag

    @crossccy_flag.setter
    def crossccy_flag(self, value):
        self._crossccy_flag = value
    @property
    def exchange(self):
        return self._exchange

    @exchange.setter
    def exchange(self, value):
        self._exchange = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def is_recharge_receipt(self):
        return self._is_recharge_receipt

    @is_recharge_receipt.setter
    def is_recharge_receipt(self, value):
        self._is_recharge_receipt = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_amount:
            if hasattr(self.charge_amount, 'to_alipay_dict'):
                params['charge_amount'] = self.charge_amount.to_alipay_dict()
            else:
                params['charge_amount'] = self.charge_amount
        if self.chargeccy:
            if hasattr(self.chargeccy, 'to_alipay_dict'):
                params['chargeccy'] = self.chargeccy.to_alipay_dict()
            else:
                params['chargeccy'] = self.chargeccy
        if self.crossccy_flag:
            if hasattr(self.crossccy_flag, 'to_alipay_dict'):
                params['crossccy_flag'] = self.crossccy_flag.to_alipay_dict()
            else:
                params['crossccy_flag'] = self.crossccy_flag
        if self.exchange:
            if hasattr(self.exchange, 'to_alipay_dict'):
                params['exchange'] = self.exchange.to_alipay_dict()
            else:
                params['exchange'] = self.exchange
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.is_recharge_receipt:
            if hasattr(self.is_recharge_receipt, 'to_alipay_dict'):
                params['is_recharge_receipt'] = self.is_recharge_receipt.to_alipay_dict()
            else:
                params['is_recharge_receipt'] = self.is_recharge_receipt
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankLogTransferFormNew()
        if 'charge_amount' in d:
            o.charge_amount = d['charge_amount']
        if 'chargeccy' in d:
            o.chargeccy = d['chargeccy']
        if 'crossccy_flag' in d:
            o.crossccy_flag = d['crossccy_flag']
        if 'exchange' in d:
            o.exchange = d['exchange']
        if 'id' in d:
            o.id = d['id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'is_recharge_receipt' in d:
            o.is_recharge_receipt = d['is_recharge_receipt']
        if 'memo' in d:
            o.memo = d['memo']
        if 'target' in d:
            o.target = d['target']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        return o


