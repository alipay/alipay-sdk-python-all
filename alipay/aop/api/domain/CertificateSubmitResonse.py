#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateSubmitResonse(object):

    def __init__(self):
        self._card_id = None
        self._deduction_order_id = None
        self._desc = None
        self._serial_no = None
        self._success = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def deduction_order_id(self):
        return self._deduction_order_id

    @deduction_order_id.setter
    def deduction_order_id(self, value):
        self._deduction_order_id = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.deduction_order_id:
            if hasattr(self.deduction_order_id, 'to_alipay_dict'):
                params['deduction_order_id'] = self.deduction_order_id.to_alipay_dict()
            else:
                params['deduction_order_id'] = self.deduction_order_id
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateSubmitResonse()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'deduction_order_id' in d:
            o.deduction_order_id = d['deduction_order_id']
        if 'desc' in d:
            o.desc = d['desc']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'success' in d:
            o.success = d['success']
        return o


