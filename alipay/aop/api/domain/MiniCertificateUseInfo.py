#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniCertificateUseInfo(object):

    def __init__(self):
        self._amount = None
        self._certificate_id = None
        self._certificate_sequence_id = None
        self._shop_id = None
        self._shop_name = None
        self._use_time = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_sequence_id(self):
        return self._certificate_sequence_id

    @certificate_sequence_id.setter
    def certificate_sequence_id(self, value):
        self._certificate_sequence_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_sequence_id:
            if hasattr(self.certificate_sequence_id, 'to_alipay_dict'):
                params['certificate_sequence_id'] = self.certificate_sequence_id.to_alipay_dict()
            else:
                params['certificate_sequence_id'] = self.certificate_sequence_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.use_time:
            if hasattr(self.use_time, 'to_alipay_dict'):
                params['use_time'] = self.use_time.to_alipay_dict()
            else:
                params['use_time'] = self.use_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniCertificateUseInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_sequence_id' in d:
            o.certificate_sequence_id = d['certificate_sequence_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'use_time' in d:
            o.use_time = d['use_time']
        return o


