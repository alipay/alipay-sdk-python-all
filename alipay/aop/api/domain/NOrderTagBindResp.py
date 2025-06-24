#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NOrderTagBindResp(object):

    def __init__(self):
        self._nfc_url = None

    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        if isinstance(value, list):
            self._nfc_url = list()
            for i in value:
                self._nfc_url.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.nfc_url:
            if isinstance(self.nfc_url, list):
                for i in range(0, len(self.nfc_url)):
                    element = self.nfc_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nfc_url[i] = element.to_alipay_dict()
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NOrderTagBindResp()
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        return o


