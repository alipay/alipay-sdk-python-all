#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayApplepayTransactionauthtokenDeleteModel(object):

    def __init__(self):
        self._device_identifier = None
        self._provisioning_bundle_identifier = None
        self._provisioning_bundle_identifiers = None
        self._push_token = None
        self._reference_identifier = None

    @property
    def device_identifier(self):
        return self._device_identifier

    @device_identifier.setter
    def device_identifier(self, value):
        self._device_identifier = value
    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
    @property
    def provisioning_bundle_identifiers(self):
        return self._provisioning_bundle_identifiers

    @provisioning_bundle_identifiers.setter
    def provisioning_bundle_identifiers(self, value):
        if isinstance(value, list):
            self._provisioning_bundle_identifiers = list()
            for i in value:
                self._provisioning_bundle_identifiers.append(i)
    @property
    def push_token(self):
        return self._push_token

    @push_token.setter
    def push_token(self, value):
        self._push_token = value
    @property
    def reference_identifier(self):
        return self._reference_identifier

    @reference_identifier.setter
    def reference_identifier(self, value):
        self._reference_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_identifier:
            if hasattr(self.device_identifier, 'to_alipay_dict'):
                params['device_identifier'] = self.device_identifier.to_alipay_dict()
            else:
                params['device_identifier'] = self.device_identifier
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        if self.provisioning_bundle_identifiers:
            if isinstance(self.provisioning_bundle_identifiers, list):
                for i in range(0, len(self.provisioning_bundle_identifiers)):
                    element = self.provisioning_bundle_identifiers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.provisioning_bundle_identifiers[i] = element.to_alipay_dict()
            if hasattr(self.provisioning_bundle_identifiers, 'to_alipay_dict'):
                params['provisioning_bundle_identifiers'] = self.provisioning_bundle_identifiers.to_alipay_dict()
            else:
                params['provisioning_bundle_identifiers'] = self.provisioning_bundle_identifiers
        if self.push_token:
            if hasattr(self.push_token, 'to_alipay_dict'):
                params['push_token'] = self.push_token.to_alipay_dict()
            else:
                params['push_token'] = self.push_token
        if self.reference_identifier:
            if hasattr(self.reference_identifier, 'to_alipay_dict'):
                params['reference_identifier'] = self.reference_identifier.to_alipay_dict()
            else:
                params['reference_identifier'] = self.reference_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayApplepayTransactionauthtokenDeleteModel()
        if 'device_identifier' in d:
            o.device_identifier = d['device_identifier']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'provisioning_bundle_identifiers' in d:
            o.provisioning_bundle_identifiers = d['provisioning_bundle_identifiers']
        if 'push_token' in d:
            o.push_token = d['push_token']
        if 'reference_identifier' in d:
            o.reference_identifier = d['reference_identifier']
        return o


