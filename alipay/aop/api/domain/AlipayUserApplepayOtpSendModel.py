#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserApplepayOtpSendModel(object):

    def __init__(self):
        self._provisioning_bundle_identifier = None
        self._resolution_method_identifier = None

    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
    @property
    def resolution_method_identifier(self):
        return self._resolution_method_identifier

    @resolution_method_identifier.setter
    def resolution_method_identifier(self, value):
        self._resolution_method_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        if self.resolution_method_identifier:
            if hasattr(self.resolution_method_identifier, 'to_alipay_dict'):
                params['resolution_method_identifier'] = self.resolution_method_identifier.to_alipay_dict()
            else:
                params['resolution_method_identifier'] = self.resolution_method_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserApplepayOtpSendModel()
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'resolution_method_identifier' in d:
            o.resolution_method_identifier = d['resolution_method_identifier']
        return o


