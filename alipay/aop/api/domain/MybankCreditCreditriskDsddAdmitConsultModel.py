#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditCreditriskDsddAdmitConsultModel(object):

    def __init__(self):
        self._smid = None

    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditCreditriskDsddAdmitConsultModel()
        if 'smid' in d:
            o.smid = d['smid']
        return o


