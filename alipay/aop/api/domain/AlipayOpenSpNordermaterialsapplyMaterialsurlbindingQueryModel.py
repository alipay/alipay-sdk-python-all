#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsapplyMaterialsurlbindingQueryModel(object):

    def __init__(self):
        self._qr_code_url_list = None

    @property
    def qr_code_url_list(self):
        return self._qr_code_url_list

    @qr_code_url_list.setter
    def qr_code_url_list(self, value):
        if isinstance(value, list):
            self._qr_code_url_list = list()
            for i in value:
                self._qr_code_url_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.qr_code_url_list:
            if isinstance(self.qr_code_url_list, list):
                for i in range(0, len(self.qr_code_url_list)):
                    element = self.qr_code_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qr_code_url_list[i] = element.to_alipay_dict()
            if hasattr(self.qr_code_url_list, 'to_alipay_dict'):
                params['qr_code_url_list'] = self.qr_code_url_list.to_alipay_dict()
            else:
                params['qr_code_url_list'] = self.qr_code_url_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsapplyMaterialsurlbindingQueryModel()
        if 'qr_code_url_list' in d:
            o.qr_code_url_list = d['qr_code_url_list']
        return o


