#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockQualifiedInvestorApplyModel(object):

    def __init__(self):
        self._id_number_encrypt = None

    @property
    def id_number_encrypt(self):
        return self._id_number_encrypt

    @id_number_encrypt.setter
    def id_number_encrypt(self, value):
        self._id_number_encrypt = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_number_encrypt:
            if hasattr(self.id_number_encrypt, 'to_alipay_dict'):
                params['id_number_encrypt'] = self.id_number_encrypt.to_alipay_dict()
            else:
                params['id_number_encrypt'] = self.id_number_encrypt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockQualifiedInvestorApplyModel()
        if 'id_number_encrypt' in d:
            o.id_number_encrypt = d['id_number_encrypt']
        return o


