#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEprintPrinterAddModel(object):

    def __init__(self):
        self._client_id = None
        self._client_secret = None
        self._eprint_token = None
        self._machine_code = None
        self._msign = None
        self._phone = None
        self._print_name = None

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
    @property
    def msign(self):
        return self._msign

    @msign.setter
    def msign(self, value):
        self._msign = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def print_name(self):
        return self._print_name

    @print_name.setter
    def print_name(self, value):
        self._print_name = value


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
        if self.msign:
            if hasattr(self.msign, 'to_alipay_dict'):
                params['msign'] = self.msign.to_alipay_dict()
            else:
                params['msign'] = self.msign
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.print_name:
            if hasattr(self.print_name, 'to_alipay_dict'):
                params['print_name'] = self.print_name.to_alipay_dict()
            else:
                params['print_name'] = self.print_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEprintPrinterAddModel()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_secret' in d:
            o.client_secret = d['client_secret']
        if 'eprint_token' in d:
            o.eprint_token = d['eprint_token']
        if 'machine_code' in d:
            o.machine_code = d['machine_code']
        if 'msign' in d:
            o.msign = d['msign']
        if 'phone' in d:
            o.phone = d['phone']
        if 'print_name' in d:
            o.print_name = d['print_name']
        return o


