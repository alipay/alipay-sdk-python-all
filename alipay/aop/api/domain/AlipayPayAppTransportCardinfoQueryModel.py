#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppTransportCardinfoQueryModel(object):

    def __init__(self):
        self._command = None
        self._encoded_cipher = None
        self._k_version = None
        self._tid_cipher = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
    @property
    def encoded_cipher(self):
        return self._encoded_cipher

    @encoded_cipher.setter
    def encoded_cipher(self, value):
        self._encoded_cipher = value
    @property
    def k_version(self):
        return self._k_version

    @k_version.setter
    def k_version(self, value):
        self._k_version = value
    @property
    def tid_cipher(self):
        return self._tid_cipher

    @tid_cipher.setter
    def tid_cipher(self, value):
        self._tid_cipher = value


    def to_alipay_dict(self):
        params = dict()
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        if self.encoded_cipher:
            if hasattr(self.encoded_cipher, 'to_alipay_dict'):
                params['encoded_cipher'] = self.encoded_cipher.to_alipay_dict()
            else:
                params['encoded_cipher'] = self.encoded_cipher
        if self.k_version:
            if hasattr(self.k_version, 'to_alipay_dict'):
                params['k_version'] = self.k_version.to_alipay_dict()
            else:
                params['k_version'] = self.k_version
        if self.tid_cipher:
            if hasattr(self.tid_cipher, 'to_alipay_dict'):
                params['tid_cipher'] = self.tid_cipher.to_alipay_dict()
            else:
                params['tid_cipher'] = self.tid_cipher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppTransportCardinfoQueryModel()
        if 'command' in d:
            o.command = d['command']
        if 'encoded_cipher' in d:
            o.encoded_cipher = d['encoded_cipher']
        if 'k_version' in d:
            o.k_version = d['k_version']
        if 'tid_cipher' in d:
            o.tid_cipher = d['tid_cipher']
        return o


