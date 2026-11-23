#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPeUsercertMatchModel(object):

    def __init__(self):
        self._cert_no_list = None
        self._mobile_no = None

    @property
    def cert_no_list(self):
        return self._cert_no_list

    @cert_no_list.setter
    def cert_no_list(self, value):
        if isinstance(value, list):
            self._cert_no_list = list()
            for i in value:
                self._cert_no_list.append(i)
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no_list:
            if isinstance(self.cert_no_list, list):
                for i in range(0, len(self.cert_no_list)):
                    element = self.cert_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cert_no_list[i] = element.to_alipay_dict()
            if hasattr(self.cert_no_list, 'to_alipay_dict'):
                params['cert_no_list'] = self.cert_no_list.to_alipay_dict()
            else:
                params['cert_no_list'] = self.cert_no_list
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPeUsercertMatchModel()
        if 'cert_no_list' in d:
            o.cert_no_list = d['cert_no_list']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        return o


