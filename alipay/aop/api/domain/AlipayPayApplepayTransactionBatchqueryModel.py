#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayApplepayTransactionBatchqueryModel(object):

    def __init__(self):
        self._authorization = None
        self._device_identifier = None
        self._provisioning_bundle_identifier = None
        self._tag = None

    @property
    def authorization(self):
        return self._authorization

    @authorization.setter
    def authorization(self, value):
        self._authorization = value
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
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization:
            if hasattr(self.authorization, 'to_alipay_dict'):
                params['authorization'] = self.authorization.to_alipay_dict()
            else:
                params['authorization'] = self.authorization
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
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayApplepayTransactionBatchqueryModel()
        if 'authorization' in d:
            o.authorization = d['authorization']
        if 'device_identifier' in d:
            o.device_identifier = d['device_identifier']
        if 'provisioning_bundle_identifier' in d:
            o.provisioning_bundle_identifier = d['provisioning_bundle_identifier']
        if 'tag' in d:
            o.tag = d['tag']
        return o


