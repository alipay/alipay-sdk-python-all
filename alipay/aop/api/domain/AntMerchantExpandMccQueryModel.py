#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandMccQueryModel(object):

    def __init__(self):
        self._mcc_code_list = None

    @property
    def mcc_code_list(self):
        return self._mcc_code_list

    @mcc_code_list.setter
    def mcc_code_list(self, value):
        self._mcc_code_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.mcc_code_list:
            if hasattr(self.mcc_code_list, 'to_alipay_dict'):
                params['mcc_code_list'] = self.mcc_code_list.to_alipay_dict()
            else:
                params['mcc_code_list'] = self.mcc_code_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandMccQueryModel()
        if 'mcc_code_list' in d:
            o.mcc_code_list = d['mcc_code_list']
        return o


