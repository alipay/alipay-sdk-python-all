#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EncryptedPaymentCredential import EncryptedPaymentCredential


class PaymentCredential(object):

    def __init__(self):
        self._expiration_timestamp = None
        self._identifier = None
        self._payment_credential_type = None
        self._value = None

    @property
    def expiration_timestamp(self):
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, value):
        self._expiration_timestamp = value
    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = value
    @property
    def payment_credential_type(self):
        return self._payment_credential_type

    @payment_credential_type.setter
    def payment_credential_type(self, value):
        self._payment_credential_type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, EncryptedPaymentCredential):
            self._value = value
        else:
            self._value = EncryptedPaymentCredential.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.expiration_timestamp:
            if hasattr(self.expiration_timestamp, 'to_alipay_dict'):
                params['expiration_timestamp'] = self.expiration_timestamp.to_alipay_dict()
            else:
                params['expiration_timestamp'] = self.expiration_timestamp
        if self.identifier:
            if hasattr(self.identifier, 'to_alipay_dict'):
                params['identifier'] = self.identifier.to_alipay_dict()
            else:
                params['identifier'] = self.identifier
        if self.payment_credential_type:
            if hasattr(self.payment_credential_type, 'to_alipay_dict'):
                params['payment_credential_type'] = self.payment_credential_type.to_alipay_dict()
            else:
                params['payment_credential_type'] = self.payment_credential_type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentCredential()
        if 'expiration_timestamp' in d:
            o.expiration_timestamp = d['expiration_timestamp']
        if 'identifier' in d:
            o.identifier = d['identifier']
        if 'payment_credential_type' in d:
            o.payment_credential_type = d['payment_credential_type']
        if 'value' in d:
            o.value = d['value']
        return o


