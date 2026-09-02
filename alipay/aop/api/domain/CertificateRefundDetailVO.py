#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateRefundDetailVO(object):

    def __init__(self):
        self._certificate_id = None
        self._refund_cash = None
        self._refund_status = None
        self._serial_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        if self.refund_status:
            if hasattr(self.refund_status, 'to_alipay_dict'):
                params['refund_status'] = self.refund_status.to_alipay_dict()
            else:
                params['refund_status'] = self.refund_status
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateRefundDetailVO()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        if 'refund_status' in d:
            o.refund_status = d['refund_status']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


