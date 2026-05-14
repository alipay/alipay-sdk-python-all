#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayAgentPaymentVerifyModel(object):

    def __init__(self):
        self._client_session = None
        self._payment_proof = None
        self._trade_no = None

    @property
    def client_session(self):
        return self._client_session

    @client_session.setter
    def client_session(self, value):
        self._client_session = value
    @property
    def payment_proof(self):
        return self._payment_proof

    @payment_proof.setter
    def payment_proof(self, value):
        self._payment_proof = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_session:
            if hasattr(self.client_session, 'to_alipay_dict'):
                params['client_session'] = self.client_session.to_alipay_dict()
            else:
                params['client_session'] = self.client_session
        if self.payment_proof:
            if hasattr(self.payment_proof, 'to_alipay_dict'):
                params['payment_proof'] = self.payment_proof.to_alipay_dict()
            else:
                params['payment_proof'] = self.payment_proof
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayAgentPaymentVerifyModel()
        if 'client_session' in d:
            o.client_session = d['client_session']
        if 'payment_proof' in d:
            o.payment_proof = d['payment_proof']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


