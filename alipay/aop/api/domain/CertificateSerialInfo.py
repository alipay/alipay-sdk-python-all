#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInstanceAmountInfo import CertificateInstanceAmountInfo


class CertificateSerialInfo(object):

    def __init__(self):
        self._amount_info = None
        self._serial_no = None
        self._status = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, CertificateInstanceAmountInfo):
            self._amount_info = value
        else:
            self._amount_info = CertificateInstanceAmountInfo.from_alipay_dict(value)
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_info:
            if hasattr(self.amount_info, 'to_alipay_dict'):
                params['amount_info'] = self.amount_info.to_alipay_dict()
            else:
                params['amount_info'] = self.amount_info
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
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
        o = CertificateSerialInfo()
        if 'amount_info' in d:
            o.amount_info = d['amount_info']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'status' in d:
            o.status = d['status']
        return o


