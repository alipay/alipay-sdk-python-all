#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FraudData import FraudData


class AlipayUserApplepayProvisioningbundleQueryModel(object):

    def __init__(self):
        self._encryption_cert_chain = None
        self._encryption_version = None
        self._fraud_data = None
        self._locale = None
        self._private_encryption_cert_chain = None
        self._provisioning_bundle_identifier = None
        self._reference_identifier = None
        self._x_pod = None

    @property
    def encryption_cert_chain(self):
        return self._encryption_cert_chain

    @encryption_cert_chain.setter
    def encryption_cert_chain(self, value):
        if isinstance(value, list):
            self._encryption_cert_chain = list()
            for i in value:
                self._encryption_cert_chain.append(i)
    @property
    def encryption_version(self):
        return self._encryption_version

    @encryption_version.setter
    def encryption_version(self, value):
        self._encryption_version = value
    @property
    def fraud_data(self):
        return self._fraud_data

    @fraud_data.setter
    def fraud_data(self, value):
        if isinstance(value, FraudData):
            self._fraud_data = value
        else:
            self._fraud_data = FraudData.from_alipay_dict(value)
    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value
    @property
    def private_encryption_cert_chain(self):
        return self._private_encryption_cert_chain

    @private_encryption_cert_chain.setter
    def private_encryption_cert_chain(self, value):
        if isinstance(value, list):
            self._private_encryption_cert_chain = list()
            for i in value:
                self._private_encryption_cert_chain.append(i)
    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
    @property
    def reference_identifier(self):
        return self._reference_identifier

    @reference_identifier.setter
    def reference_identifier(self, value):
        self._reference_identifier = value
    @property
    def x_pod(self):
        return self._x_pod

    @x_pod.setter
    def x_pod(self, value):
        self._x_pod = value


    def to_alipay_dict(self):
        params = dict()
        if self.encryption_cert_chain:
            if isinstance(self.encryption_cert_chain, list):
                for i in range(0, len(self.encryption_cert_chain)):
                    element = self.encryption_cert_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.encryption_cert_chain[i] = element.to_alipay_dict()
            if hasattr(self.encryption_cert_chain, 'to_alipay_dict'):
                params['encryption_cert_chain'] = self.encryption_cert_chain.to_alipay_dict()
            else:
                params['encryption_cert_chain'] = self.encryption_cert_chain
        if self.encryption_version:
            if hasattr(self.encryption_version, 'to_alipay_dict'):
                params['encryption_version'] = self.encryption_version.to_alipay_dict()
            else:
                params['encryption_version'] = self.encryption_version
        if self.fraud_data:
            if hasattr(self.fraud_data, 'to_alipay_dict'):
                params['fraud_data'] = self.fraud_data.to_alipay_dict()
            else:
                params['fraud_data'] = self.fraud_data
        if self.locale:
            if hasattr(self.locale, 'to_alipay_dict'):
                params['locale'] = self.locale.to_alipay_dict()
            else:
                params['locale'] = self.locale
        if self.private_encryption_cert_chain:
            if isinstance(self.private_encryption_cert_chain, list):
                for i in range(0, len(self.private_encryption_cert_chain)):
                    element = self.private_encryption_cert_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.private_encryption_cert_chain[i] = element.to_alipay_dict()
            if hasattr(self.private_encryption_cert_chain, 'to_alipay_dict'):
                params['private_encryption_cert_chain'] = self.private_encryption_cert_chain.to_alipay_dict()
            else:
                params['private_encryption_cert_chain'] = self.private_encryption_cert_chain
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        if self.reference_identifier:
            if hasattr(self.reference_identifier, 'to_alipay_dict'):
                params['reference_identifier'] = self.reference_identifier.to_alipay_dict()
            else:
                params['reference_identifier'] = self.reference_identifier
        if self.x_pod:
            if hasattr(self.x_pod, 'to_alipay_dict'):
                params['x_pod'] = self.x_pod.to_alipay_dict()
            else:
                params['x_pod'] = self.x_pod
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserApplepayProvisioningbundleQueryModel()
        if 'encryption_cert_chain' in d:
            o.encryption_cert_chain = d['encryption_cert_chain']
        if 'encryption_version' in d:
            o.encryption_version = d['encryption_version']
        if 'fraud_data' in d:
            o.fraud_data = d['fraud_data']
        if 'locale' in d:
            o.locale = d['locale']
        if 'private_encryption_cert_chain' in d:
            o.private_encryption_cert_chain = d['private_encryption_cert_chain']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'reference_identifier' in d:
            o.reference_identifier = d['reference_identifier']
        if 'x_pod' in d:
            o.x_pod = d['x_pod']
        return o


