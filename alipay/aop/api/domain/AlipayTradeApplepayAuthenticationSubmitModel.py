#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthenticationResult import AuthenticationResult


class AlipayTradeApplepayAuthenticationSubmitModel(object):

    def __init__(self):
        self._authentication_results = None
        self._device_identifier = None
        self._dpan_identifier = None
        self._transaction_identifier = None

    @property
    def authentication_results(self):
        return self._authentication_results

    @authentication_results.setter
    def authentication_results(self, value):
        if isinstance(value, list):
            self._authentication_results = list()
            for i in value:
                if isinstance(i, AuthenticationResult):
                    self._authentication_results.append(i)
                else:
                    self._authentication_results.append(AuthenticationResult.from_alipay_dict(i))
    @property
    def device_identifier(self):
        return self._device_identifier

    @device_identifier.setter
    def device_identifier(self, value):
        self._device_identifier = value
    @property
    def dpan_identifier(self):
        return self._dpan_identifier

    @dpan_identifier.setter
    def dpan_identifier(self, value):
        self._dpan_identifier = value
    @property
    def transaction_identifier(self):
        return self._transaction_identifier

    @transaction_identifier.setter
    def transaction_identifier(self, value):
        self._transaction_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_results:
            if isinstance(self.authentication_results, list):
                for i in range(0, len(self.authentication_results)):
                    element = self.authentication_results[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authentication_results[i] = element.to_alipay_dict()
            if hasattr(self.authentication_results, 'to_alipay_dict'):
                params['authentication_results'] = self.authentication_results.to_alipay_dict()
            else:
                params['authentication_results'] = self.authentication_results
        if self.device_identifier:
            if hasattr(self.device_identifier, 'to_alipay_dict'):
                params['device_identifier'] = self.device_identifier.to_alipay_dict()
            else:
                params['device_identifier'] = self.device_identifier
        if self.dpan_identifier:
            if hasattr(self.dpan_identifier, 'to_alipay_dict'):
                params['dpan_identifier'] = self.dpan_identifier.to_alipay_dict()
            else:
                params['dpan_identifier'] = self.dpan_identifier
        if self.transaction_identifier:
            if hasattr(self.transaction_identifier, 'to_alipay_dict'):
                params['transaction_identifier'] = self.transaction_identifier.to_alipay_dict()
            else:
                params['transaction_identifier'] = self.transaction_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeApplepayAuthenticationSubmitModel()
        if 'authentication_results' in d:
            o.authentication_results = d['authentication_results']
        if 'device_identifier' in d:
            o.device_identifier = d['device_identifier']
        if 'dpan_identifier' in d:
            o.dpan_identifier = d['dpan_identifier']
        if 'transaction_identifier' in d:
            o.transaction_identifier = d['transaction_identifier']
        return o


