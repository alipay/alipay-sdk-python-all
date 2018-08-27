#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceKeyInfo import InvoiceKeyInfo


class InvoiceInfo(object):

    def __init__(self):
        self._details = None
        self._key_info = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value
    @property
    def key_info(self):
        return self._key_info

    @key_info.setter
    def key_info(self, value):
        if isinstance(value, InvoiceKeyInfo):
            self._key_info = value
        else:
            self._key_info = InvoiceKeyInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.details:
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.key_info:
            if hasattr(self.key_info, 'to_alipay_dict'):
                params['key_info'] = self.key_info.to_alipay_dict()
            else:
                params['key_info'] = self.key_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceInfo()
        if 'details' in d:
            o.details = d['details']
        if 'key_info' in d:
            o.key_info = d['key_info']
        return o


