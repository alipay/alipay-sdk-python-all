#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserApplepayProvisioningbundleModifyModel(object):

    def __init__(self):
        self._action = None
        self._otp_value = None
        self._provisioning_bundle_identifier = None
        self._reference_identifier = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def otp_value(self):
        return self._otp_value

    @otp_value.setter
    def otp_value(self, value):
        self._otp_value = value
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
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.otp_value:
            if hasattr(self.otp_value, 'to_alipay_dict'):
                params['otp_value'] = self.otp_value.to_alipay_dict()
            else:
                params['otp_value'] = self.otp_value
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
        o = AlipayUserApplepayProvisioningbundleModifyModel()
        if 'action' in d:
            o.action = d['action']
        if 'otp_value' in d:
            o.otp_value = d['otp_value']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'reference_identifier' in d:
            o.reference_identifier = d['reference_identifier']
        return o


