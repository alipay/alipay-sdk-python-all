#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniRefundCertificateDTO(object):

    def __init__(self):
        self._certificate_id = None
        self._serial_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
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
        o = MiniRefundCertificateDTO()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


