#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SerialInfo(object):

    def __init__(self):
        self._claim_result = None
        self._reject_reason = None
        self._serial_number = None

    @property
    def claim_result(self):
        return self._claim_result

    @claim_result.setter
    def claim_result(self, value):
        self._claim_result = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_result:
            if hasattr(self.claim_result, 'to_alipay_dict'):
                params['claim_result'] = self.claim_result.to_alipay_dict()
            else:
                params['claim_result'] = self.claim_result
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SerialInfo()
        if 'claim_result' in d:
            o.claim_result = d['claim_result']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        return o


