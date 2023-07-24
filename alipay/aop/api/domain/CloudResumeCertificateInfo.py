#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumeCertificateInfo(object):

    def __init__(self):
        self._certificate_cert_level = None
        self._certificate_name = None
        self._certificate_send_card_address = None
        self._certificate_verify_status = None
        self._in_validity_period = None

    @property
    def certificate_cert_level(self):
        return self._certificate_cert_level

    @certificate_cert_level.setter
    def certificate_cert_level(self, value):
        self._certificate_cert_level = value
    @property
    def certificate_name(self):
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, value):
        self._certificate_name = value
    @property
    def certificate_send_card_address(self):
        return self._certificate_send_card_address

    @certificate_send_card_address.setter
    def certificate_send_card_address(self, value):
        self._certificate_send_card_address = value
    @property
    def certificate_verify_status(self):
        return self._certificate_verify_status

    @certificate_verify_status.setter
    def certificate_verify_status(self, value):
        self._certificate_verify_status = value
    @property
    def in_validity_period(self):
        return self._in_validity_period

    @in_validity_period.setter
    def in_validity_period(self, value):
        self._in_validity_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_cert_level:
            if hasattr(self.certificate_cert_level, 'to_alipay_dict'):
                params['certificate_cert_level'] = self.certificate_cert_level.to_alipay_dict()
            else:
                params['certificate_cert_level'] = self.certificate_cert_level
        if self.certificate_name:
            if hasattr(self.certificate_name, 'to_alipay_dict'):
                params['certificate_name'] = self.certificate_name.to_alipay_dict()
            else:
                params['certificate_name'] = self.certificate_name
        if self.certificate_send_card_address:
            if hasattr(self.certificate_send_card_address, 'to_alipay_dict'):
                params['certificate_send_card_address'] = self.certificate_send_card_address.to_alipay_dict()
            else:
                params['certificate_send_card_address'] = self.certificate_send_card_address
        if self.certificate_verify_status:
            if hasattr(self.certificate_verify_status, 'to_alipay_dict'):
                params['certificate_verify_status'] = self.certificate_verify_status.to_alipay_dict()
            else:
                params['certificate_verify_status'] = self.certificate_verify_status
        if self.in_validity_period:
            if hasattr(self.in_validity_period, 'to_alipay_dict'):
                params['in_validity_period'] = self.in_validity_period.to_alipay_dict()
            else:
                params['in_validity_period'] = self.in_validity_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumeCertificateInfo()
        if 'certificate_cert_level' in d:
            o.certificate_cert_level = d['certificate_cert_level']
        if 'certificate_name' in d:
            o.certificate_name = d['certificate_name']
        if 'certificate_send_card_address' in d:
            o.certificate_send_card_address = d['certificate_send_card_address']
        if 'certificate_verify_status' in d:
            o.certificate_verify_status = d['certificate_verify_status']
        if 'in_validity_period' in d:
            o.in_validity_period = d['in_validity_period']
        return o


