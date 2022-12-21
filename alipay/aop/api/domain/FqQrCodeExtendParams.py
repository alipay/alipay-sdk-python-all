#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FqQrCodeExtendParams(object):

    def __init__(self):
        self._fq_num = None

    @property
    def fq_num(self):
        return self._fq_num

    @fq_num.setter
    def fq_num(self, value):
        self._fq_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.fq_num:
            if hasattr(self.fq_num, 'to_alipay_dict'):
                params['fq_num'] = self.fq_num.to_alipay_dict()
            else:
                params['fq_num'] = self.fq_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FqQrCodeExtendParams()
        if 'fq_num' in d:
            o.fq_num = d['fq_num']
        return o


