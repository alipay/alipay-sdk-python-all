#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitEnrollMerchant(object):

    def __init__(self):
        self._merchant_uid = None

    @property
    def merchant_uid(self):
        return self._merchant_uid

    @merchant_uid.setter
    def merchant_uid(self, value):
        self._merchant_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_uid:
            if hasattr(self.merchant_uid, 'to_alipay_dict'):
                params['merchant_uid'] = self.merchant_uid.to_alipay_dict()
            else:
                params['merchant_uid'] = self.merchant_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitEnrollMerchant()
        if 'merchant_uid' in d:
            o.merchant_uid = d['merchant_uid']
        return o


