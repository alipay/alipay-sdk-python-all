#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserTaxRefundQueryModel(object):

    def __init__(self):
        self._qr_code = None
        self._refund_biz_no = None

    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def refund_biz_no(self):
        return self._refund_biz_no

    @refund_biz_no.setter
    def refund_biz_no(self, value):
        self._refund_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
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
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'refund_biz_no' in d:
            o.refund_biz_no = d['refund_biz_no']
        return o


