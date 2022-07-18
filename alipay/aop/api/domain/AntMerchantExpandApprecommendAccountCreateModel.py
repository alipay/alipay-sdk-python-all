#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandApprecommendAccountCreateModel(object):

    def __init__(self):
        self._acc_no = None
        self._app_no = None

    @property
    def acc_no(self):
        return self._acc_no

    @acc_no.setter
    def acc_no(self, value):
        self._acc_no = value
    @property
    def app_no(self):
        return self._app_no

    @app_no.setter
    def app_no(self, value):
        self._app_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_no:
            if hasattr(self.acc_no, 'to_alipay_dict'):
                params['acc_no'] = self.acc_no.to_alipay_dict()
            else:
                params['acc_no'] = self.acc_no
        if self.app_no:
            if hasattr(self.app_no, 'to_alipay_dict'):
                params['app_no'] = self.app_no.to_alipay_dict()
            else:
                params['app_no'] = self.app_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandApprecommendAccountCreateModel()
        if 'acc_no' in d:
            o.acc_no = d['acc_no']
        if 'app_no' in d:
            o.app_no = d['app_no']
        return o


