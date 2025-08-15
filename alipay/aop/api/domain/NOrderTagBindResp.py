#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NOrderTagBindResp(object):

    def __init__(self):
        self._bind_pic = None
        self._nfc_url = None

    @property
    def bind_pic(self):
        return self._bind_pic

    @bind_pic.setter
    def bind_pic(self, value):
        if isinstance(value, list):
            self._bind_pic = list()
            for i in value:
                self._bind_pic.append(i)
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
        if self.bind_pic:
            if isinstance(self.bind_pic, list):
                for i in range(0, len(self.bind_pic)):
                    element = self.bind_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_pic[i] = element.to_alipay_dict()
            if hasattr(self.bind_pic, 'to_alipay_dict'):
                params['bind_pic'] = self.bind_pic.to_alipay_dict()
            else:
                params['bind_pic'] = self.bind_pic
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
        if 'bind_pic' in d:
            o.bind_pic = d['bind_pic']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        return o


