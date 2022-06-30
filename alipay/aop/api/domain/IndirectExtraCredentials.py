#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectExtraCredentials(object):

    def __init__(self):
        self._smid_list = None

    @property
    def smid_list(self):
        return self._smid_list

    @smid_list.setter
    def smid_list(self, value):
        if isinstance(value, list):
            self._smid_list = list()
            for i in value:
                self._smid_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.smid_list:
            if isinstance(self.smid_list, list):
                for i in range(0, len(self.smid_list)):
                    element = self.smid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.smid_list[i] = element.to_alipay_dict()
            if hasattr(self.smid_list, 'to_alipay_dict'):
                params['smid_list'] = self.smid_list.to_alipay_dict()
            else:
                params['smid_list'] = self.smid_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectExtraCredentials()
        if 'smid_list' in d:
            o.smid_list = d['smid_list']
        return o


