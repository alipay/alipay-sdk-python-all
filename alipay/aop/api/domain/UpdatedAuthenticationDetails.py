#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UpdatedAuthenticationDetails(object):

    def __init__(self):
        self._authentication_mechanisms = None
        self._nonce = None
        self._partial_transaction_details_signature = None
        self._pin_format = None
        self._signing_key_material = None

    @property
    def authentication_mechanisms(self):
        return self._authentication_mechanisms

    @authentication_mechanisms.setter
    def authentication_mechanisms(self, value):
        if isinstance(value, list):
            self._authentication_mechanisms = list()
            for i in value:
                self._authentication_mechanisms.append(i)
    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, value):
        self._nonce = value
    @property
    def partial_transaction_details_signature(self):
        return self._partial_transaction_details_signature

    @partial_transaction_details_signature.setter
    def partial_transaction_details_signature(self, value):
        self._partial_transaction_details_signature = value
    @property
    def pin_format(self):
        return self._pin_format

    @pin_format.setter
    def pin_format(self, value):
        self._pin_format = value
    @property
    def signing_key_material(self):
        return self._signing_key_material

    @signing_key_material.setter
    def signing_key_material(self, value):
        self._signing_key_material = value


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_mechanisms:
            if isinstance(self.authentication_mechanisms, list):
                for i in range(0, len(self.authentication_mechanisms)):
                    element = self.authentication_mechanisms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authentication_mechanisms[i] = element.to_alipay_dict()
            if hasattr(self.authentication_mechanisms, 'to_alipay_dict'):
                params['authentication_mechanisms'] = self.authentication_mechanisms.to_alipay_dict()
            else:
                params['authentication_mechanisms'] = self.authentication_mechanisms
        if self.nonce:
            if hasattr(self.nonce, 'to_alipay_dict'):
                params['nonce'] = self.nonce.to_alipay_dict()
            else:
                params['nonce'] = self.nonce
        if self.partial_transaction_details_signature:
            if hasattr(self.partial_transaction_details_signature, 'to_alipay_dict'):
                params['partial_transaction_details_signature'] = self.partial_transaction_details_signature.to_alipay_dict()
            else:
                params['partial_transaction_details_signature'] = self.partial_transaction_details_signature
        if self.pin_format:
            if hasattr(self.pin_format, 'to_alipay_dict'):
                params['pin_format'] = self.pin_format.to_alipay_dict()
            else:
                params['pin_format'] = self.pin_format
        if self.signing_key_material:
            if hasattr(self.signing_key_material, 'to_alipay_dict'):
                params['signing_key_material'] = self.signing_key_material.to_alipay_dict()
            else:
                params['signing_key_material'] = self.signing_key_material
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UpdatedAuthenticationDetails()
        if 'authentication_mechanisms' in d:
            o.authentication_mechanisms = d['authentication_mechanisms']
        if 'nonce' in d:
            o.nonce = d['nonce']
        if 'partial_transaction_details_signature' in d:
            o.partial_transaction_details_signature = d['partial_transaction_details_signature']
        if 'pin_format' in d:
            o.pin_format = d['pin_format']
        if 'signing_key_material' in d:
            o.signing_key_material = d['signing_key_material']
        return o


