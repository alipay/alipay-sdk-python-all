#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransactionAuthenticationDetailDTO(object):

    def __init__(self):
        self._authentication_mechanisms = None
        self._pin_format = None

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
    def pin_format(self):
        return self._pin_format

    @pin_format.setter
    def pin_format(self, value):
        self._pin_format = value


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
        if self.pin_format:
            if hasattr(self.pin_format, 'to_alipay_dict'):
                params['pin_format'] = self.pin_format.to_alipay_dict()
            else:
                params['pin_format'] = self.pin_format
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransactionAuthenticationDetailDTO()
        if 'authentication_mechanisms' in d:
            o.authentication_mechanisms = d['authentication_mechanisms']
        if 'pin_format' in d:
            o.pin_format = d['pin_format']
        return o


