#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEprintPrinterDeleteModel(object):

    def __init__(self):
        self._client_id = None
        self._client_secret = None
        self._eprint_token = None
        self._machine_code = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value
    @property
    def eprint_token(self):
        return self._eprint_token

    @eprint_token.setter
    def eprint_token(self, value):
        self._eprint_token = value
    @property
    def machine_code(self):
        return self._machine_code

    @machine_code.setter
    def machine_code(self, value):
        self._machine_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.client_secret:
            if hasattr(self.client_secret, 'to_alipay_dict'):
                params['client_secret'] = self.client_secret.to_alipay_dict()
            else:
                params['client_secret'] = self.client_secret
        if self.eprint_token:
            if hasattr(self.eprint_token, 'to_alipay_dict'):
                params['eprint_token'] = self.eprint_token.to_alipay_dict()
            else:
                params['eprint_token'] = self.eprint_token
        if self.machine_code:
            if hasattr(self.machine_code, 'to_alipay_dict'):
                params['machine_code'] = self.machine_code.to_alipay_dict()
            else:
                params['machine_code'] = self.machine_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEprintPrinterDeleteModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_secret' in d:
            o.client_secret = d['client_secret']
        if 'eprint_token' in d:
            o.eprint_token = d['eprint_token']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        return o


