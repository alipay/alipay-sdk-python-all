#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandNfcInfoQueryModel(object):

    def __init__(self):
        self._nfc_url_list = None

    @property
    def nfc_url_list(self):
        return self._nfc_url_list

    @nfc_url_list.setter
    def nfc_url_list(self, value):
        if isinstance(value, list):
            self._nfc_url_list = list()
            for i in value:
                self._nfc_url_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.nfc_url_list:
            if isinstance(self.nfc_url_list, list):
                for i in range(0, len(self.nfc_url_list)):
                    element = self.nfc_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nfc_url_list[i] = element.to_alipay_dict()
            if hasattr(self.nfc_url_list, 'to_alipay_dict'):
                params['nfc_url_list'] = self.nfc_url_list.to_alipay_dict()
            else:
                params['nfc_url_list'] = self.nfc_url_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandNfcInfoQueryModel()
        if 'nfc_url_list' in d:
            o.nfc_url_list = d['nfc_url_list']
        return o


