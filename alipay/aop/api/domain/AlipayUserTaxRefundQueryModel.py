#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserTaxRefundQueryModel(object):

    def __init__(self):
        self._refund_biz_no = None

    @property
    def refund_biz_no(self):
        return self._refund_biz_no

    @refund_biz_no.setter
    def refund_biz_no(self, value):
        self._refund_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_biz_no:
            if hasattr(self.refund_biz_no, 'to_alipay_dict'):
                params['refund_biz_no'] = self.refund_biz_no.to_alipay_dict()
            else:
                params['refund_biz_no'] = self.refund_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserTaxRefundQueryModel()
        if 'refund_biz_no' in d:
            o.refund_biz_no = d['refund_biz_no']
        return o


