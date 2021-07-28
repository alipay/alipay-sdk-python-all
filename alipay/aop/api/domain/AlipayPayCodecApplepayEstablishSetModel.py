#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EstablishFraudData import EstablishFraudData


class AlipayPayCodecApplepayEstablishSetModel(object):

    def __init__(self):
        self._apple_signature = None
        self._barcode_encryption_cert_chain = None
        self._device_signature_cert_chain = None
        self._fraud_data = None
        self._provisioning_bundle_identifier = None

    @property
    def apple_signature(self):
        return self._apple_signature

    @apple_signature.setter
    def apple_signature(self, value):
        self._apple_signature = value
    @property
    def barcode_encryption_cert_chain(self):
        return self._barcode_encryption_cert_chain

    @barcode_encryption_cert_chain.setter
    def barcode_encryption_cert_chain(self, value):
        if isinstance(value, list):
            self._barcode_encryption_cert_chain = list()
            for i in value:
                self._barcode_encryption_cert_chain.append(i)
    @property
    def device_signature_cert_chain(self):
        return self._device_signature_cert_chain

    @device_signature_cert_chain.setter
    def device_signature_cert_chain(self, value):
        if isinstance(value, list):
            self._device_signature_cert_chain = list()
            for i in value:
                self._device_signature_cert_chain.append(i)
    @property
    def fraud_data(self):
        return self._fraud_data

    @fraud_data.setter
    def fraud_data(self, value):
        if isinstance(value, EstablishFraudData):
            self._fraud_data = value
        else:
            self._fraud_data = EstablishFraudData.from_alipay_dict(value)
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
        if self.barcode_encryption_cert_chain:
            if isinstance(self.barcode_encryption_cert_chain, list):
                for i in range(0, len(self.barcode_encryption_cert_chain)):
                    element = self.barcode_encryption_cert_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.barcode_encryption_cert_chain[i] = element.to_alipay_dict()
            if hasattr(self.barcode_encryption_cert_chain, 'to_alipay_dict'):
                params['barcode_encryption_cert_chain'] = self.barcode_encryption_cert_chain.to_alipay_dict()
            else:
                params['barcode_encryption_cert_chain'] = self.barcode_encryption_cert_chain
        if self.device_signature_cert_chain:
            if isinstance(self.device_signature_cert_chain, list):
                for i in range(0, len(self.device_signature_cert_chain)):
                    element = self.device_signature_cert_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_signature_cert_chain[i] = element.to_alipay_dict()
            if hasattr(self.device_signature_cert_chain, 'to_alipay_dict'):
                params['device_signature_cert_chain'] = self.device_signature_cert_chain.to_alipay_dict()
            else:
                params['device_signature_cert_chain'] = self.device_signature_cert_chain
        if self.fraud_data:
            if hasattr(self.fraud_data, 'to_alipay_dict'):
                params['fraud_data'] = self.fraud_data.to_alipay_dict()
            else:
                params['fraud_data'] = self.fraud_data
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
        o = AlipayPayCodecApplepayEstablishSetModel()
        if 'apple_signature' in d:
            o.apple_signature = d['apple_signature']
        if 'barcode_encryption_cert_chain' in d:
            o.barcode_encryption_cert_chain = d['barcode_encryption_cert_chain']
        if 'device_signature_cert_chain' in d:
            o.device_signature_cert_chain = d['device_signature_cert_chain']
        if 'fraud_data' in d:
            o.fraud_data = d['fraud_data']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        return o


