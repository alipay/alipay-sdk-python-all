#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CredentialsFraudData import CredentialsFraudData


class AlipayPayCodecApplepayCredentialsGetModel(object):

    def __init__(self):
        self._apple_signature = None
        self._encryption_public_key_hash = None
        self._fraud_data = None
        self._has_zero_qr_codes = None
        self._last_used_credential_identifier = None
        self._number_to_fetch = None
        self._payment_credential_type = None
        self._provisioning_bundle_identifier = None

    @property
    def apple_signature(self):
        return self._apple_signature

    @apple_signature.setter
    def apple_signature(self, value):
        self._apple_signature = value
    @property
    def encryption_public_key_hash(self):
        return self._encryption_public_key_hash

    @encryption_public_key_hash.setter
    def encryption_public_key_hash(self, value):
        self._encryption_public_key_hash = value
    @property
    def fraud_data(self):
        return self._fraud_data

    @fraud_data.setter
    def fraud_data(self, value):
        if isinstance(value, CredentialsFraudData):
            self._fraud_data = value
        else:
            self._fraud_data = CredentialsFraudData.from_alipay_dict(value)
    @property
    def has_zero_qr_codes(self):
        return self._has_zero_qr_codes

    @has_zero_qr_codes.setter
    def has_zero_qr_codes(self, value):
        self._has_zero_qr_codes = value
    @property
    def last_used_credential_identifier(self):
        return self._last_used_credential_identifier

    @last_used_credential_identifier.setter
    def last_used_credential_identifier(self, value):
        self._last_used_credential_identifier = value
    @property
    def number_to_fetch(self):
        return self._number_to_fetch

    @number_to_fetch.setter
    def number_to_fetch(self, value):
        self._number_to_fetch = value
    @property
    def payment_credential_type(self):
        return self._payment_credential_type

    @payment_credential_type.setter
    def payment_credential_type(self, value):
        self._payment_credential_type = value
    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.apple_signature:
            if hasattr(self.apple_signature, 'to_alipay_dict'):
                params['apple_signature'] = self.apple_signature.to_alipay_dict()
            else:
                params['apple_signature'] = self.apple_signature
        if self.encryption_public_key_hash:
            if hasattr(self.encryption_public_key_hash, 'to_alipay_dict'):
                params['encryption_public_key_hash'] = self.encryption_public_key_hash.to_alipay_dict()
            else:
                params['encryption_public_key_hash'] = self.encryption_public_key_hash
        if self.fraud_data:
            if hasattr(self.fraud_data, 'to_alipay_dict'):
                params['fraud_data'] = self.fraud_data.to_alipay_dict()
            else:
                params['fraud_data'] = self.fraud_data
        if self.has_zero_qr_codes:
            if hasattr(self.has_zero_qr_codes, 'to_alipay_dict'):
                params['has_zero_qr_codes'] = self.has_zero_qr_codes.to_alipay_dict()
            else:
                params['has_zero_qr_codes'] = self.has_zero_qr_codes
        if self.last_used_credential_identifier:
            if hasattr(self.last_used_credential_identifier, 'to_alipay_dict'):
                params['last_used_credential_identifier'] = self.last_used_credential_identifier.to_alipay_dict()
            else:
                params['last_used_credential_identifier'] = self.last_used_credential_identifier
        if self.number_to_fetch:
            if hasattr(self.number_to_fetch, 'to_alipay_dict'):
                params['number_to_fetch'] = self.number_to_fetch.to_alipay_dict()
            else:
                params['number_to_fetch'] = self.number_to_fetch
        if self.payment_credential_type:
            if hasattr(self.payment_credential_type, 'to_alipay_dict'):
                params['payment_credential_type'] = self.payment_credential_type.to_alipay_dict()
            else:
                params['payment_credential_type'] = self.payment_credential_type
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayCodecApplepayCredentialsGetModel()
        if 'apple_signature' in d:
            o.apple_signature = d['apple_signature']
        if 'encryption_public_key_hash' in d:
            o.encryption_public_key_hash = d['encryption_public_key_hash']
        if 'fraud_data' in d:
            o.fraud_data = d['fraud_data']
        if 'has_zero_qr_codes' in d:
            o.has_zero_qr_codes = d['has_zero_qr_codes']
        if 'last_used_credential_identifier' in d:
            o.last_used_credential_identifier = d['last_used_credential_identifier']
        if 'number_to_fetch' in d:
            o.number_to_fetch = d['number_to_fetch']
        if 'payment_credential_type' in d:
            o.payment_credential_type = d['payment_credential_type']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        return o


