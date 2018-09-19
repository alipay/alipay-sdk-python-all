#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertInfo import CertInfo
from alipay.aop.api.domain.OriTxnInfo import OriTxnInfo
from alipay.aop.api.domain.AccPayeeInfo import AccPayeeInfo


class AccTransDetail(object):

    def __init__(self):
        self._alipay_order_no = None
        self._cert_info = None
        self._detail_no = None
        self._ori_txn_info = None
        self._payee_info = None
        self._reach_time = None
        self._remark = None
        self._settlement_currency = None
        self._trans_amount = None
        self._trans_currency = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def cert_info(self):
        return self._cert_info

    @cert_info.setter
    def cert_info(self, value):
        if isinstance(value, CertInfo):
            self._cert_info = value
        else:
            self._cert_info = CertInfo.from_alipay_dict(value)
    @property
    def detail_no(self):
        return self._detail_no

    @detail_no.setter
    def detail_no(self, value):
        self._detail_no = value
    @property
    def ori_txn_info(self):
        return self._ori_txn_info

    @ori_txn_info.setter
    def ori_txn_info(self, value):
        if isinstance(value, OriTxnInfo):
            self._ori_txn_info = value
        else:
            self._ori_txn_info = OriTxnInfo.from_alipay_dict(value)
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, AccPayeeInfo):
            self._payee_info = value
        else:
            self._payee_info = AccPayeeInfo.from_alipay_dict(value)
    @property
    def reach_time(self):
        return self._reach_time

    @reach_time.setter
    def reach_time(self, value):
        self._reach_time = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def settlement_currency(self):
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, value):
        self._settlement_currency = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.cert_info:
            if hasattr(self.cert_info, 'to_alipay_dict'):
                params['cert_info'] = self.cert_info.to_alipay_dict()
            else:
                params['cert_info'] = self.cert_info
        if self.detail_no:
            if hasattr(self.detail_no, 'to_alipay_dict'):
                params['detail_no'] = self.detail_no.to_alipay_dict()
            else:
                params['detail_no'] = self.detail_no
        if self.ori_txn_info:
            if hasattr(self.ori_txn_info, 'to_alipay_dict'):
                params['ori_txn_info'] = self.ori_txn_info.to_alipay_dict()
            else:
                params['ori_txn_info'] = self.ori_txn_info
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.reach_time:
            if hasattr(self.reach_time, 'to_alipay_dict'):
                params['reach_time'] = self.reach_time.to_alipay_dict()
            else:
                params['reach_time'] = self.reach_time
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.settlement_currency:
            if hasattr(self.settlement_currency, 'to_alipay_dict'):
                params['settlement_currency'] = self.settlement_currency.to_alipay_dict()
            else:
                params['settlement_currency'] = self.settlement_currency
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccTransDetail()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'cert_info' in d:
            o.cert_info = d['cert_info']
        if 'detail_no' in d:
            o.detail_no = d['detail_no']
        if 'ori_txn_info' in d:
            o.ori_txn_info = d['ori_txn_info']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'reach_time' in d:
            o.reach_time = d['reach_time']
        if 'remark' in d:
            o.remark = d['remark']
        if 'settlement_currency' in d:
            o.settlement_currency = d['settlement_currency']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        return o


