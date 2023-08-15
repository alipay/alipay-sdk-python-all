#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundBusinessExtend(object):

    def __init__(self):
        self._refund_inst_consult = None

    @property
    def refund_inst_consult(self):
        return self._refund_inst_consult

    @refund_inst_consult.setter
    def refund_inst_consult(self, value):
        self._refund_inst_consult = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_inst_consult:
            if hasattr(self.refund_inst_consult, 'to_alipay_dict'):
                params['refund_inst_consult'] = self.refund_inst_consult.to_alipay_dict()
            else:
                params['refund_inst_consult'] = self.refund_inst_consult
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundBusinessExtend()
        if 'refund_inst_consult' in d:
            o.refund_inst_consult = d['refund_inst_consult']
        return o


