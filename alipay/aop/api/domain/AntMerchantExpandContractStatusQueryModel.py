#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandContractStatusQueryModel(object):

    def __init__(self):
        self._sign_biz_from = None

    @property
    def sign_biz_from(self):
        return self._sign_biz_from

    @sign_biz_from.setter
    def sign_biz_from(self, value):
        self._sign_biz_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_biz_from:
            if hasattr(self.sign_biz_from, 'to_alipay_dict'):
                params['sign_biz_from'] = self.sign_biz_from.to_alipay_dict()
            else:
                params['sign_biz_from'] = self.sign_biz_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandContractStatusQueryModel()
        if 'sign_biz_from' in d:
            o.sign_biz_from = d['sign_biz_from']
        return o


