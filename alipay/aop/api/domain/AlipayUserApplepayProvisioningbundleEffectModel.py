#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserApplepayProvisioningbundleEffectModel(object):

    def __init__(self):
        self._event_type = None
        self._provisioning_bundle_identifier = None
        self._reference_identifier = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserApplepayProvisioningbundleEffectModel()
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'reference_identifier' in d:
            o.reference_identifier = d['reference_identifier']
        return o


