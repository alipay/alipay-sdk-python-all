#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiPassStatus(object):

    def __init__(self):
        self._provisioning_bundle_identifier = None
        self._state = None

    @property
    def provisioning_bundle_identifier(self):
        return self._provisioning_bundle_identifier

    @provisioning_bundle_identifier.setter
    def provisioning_bundle_identifier(self, value):
        self._provisioning_bundle_identifier = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.provisioning_bundle_identifier:
            if hasattr(self.provisioning_bundle_identifier, 'to_alipay_dict'):
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier.to_alipay_dict()
            else:
                params['provisioning_bundle_identifier'] = self.provisioning_bundle_identifier
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPassStatus()
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'state' in d:
            o.state = d['state']
        return o


