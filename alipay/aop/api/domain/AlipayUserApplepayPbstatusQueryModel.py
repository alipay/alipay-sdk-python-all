#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserApplepayPbstatusQueryModel(object):

    def __init__(self):
        self._current_state = None
        self._device_accept_language = None
        self._provisioning_bundle_identifier = None
        self._reference_identifier = None

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, value):
        self._current_state = value
    @property
    def device_accept_language(self):
        return self._device_accept_language

    @device_accept_language.setter
    def device_accept_language(self, value):
        self._device_accept_language = value
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
        if self.current_state:
            if hasattr(self.current_state, 'to_alipay_dict'):
                params['current_state'] = self.current_state.to_alipay_dict()
            else:
                params['current_state'] = self.current_state
        if self.device_accept_language:
            if hasattr(self.device_accept_language, 'to_alipay_dict'):
                params['device_accept_language'] = self.device_accept_language.to_alipay_dict()
            else:
                params['device_accept_language'] = self.device_accept_language
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
        o = AlipayUserApplepayPbstatusQueryModel()
        if 'current_state' in d:
            o.current_state = d['current_state']
        if 'device_accept_language' in d:
            o.device_accept_language = d['device_accept_language']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'reference_identifier' in d:
            o.reference_identifier = d['reference_identifier']
        return o


