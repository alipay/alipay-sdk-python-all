#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChinaMobileBody import ChinaMobileBody
from alipay.aop.api.domain.ChinaMobileHead import ChinaMobileHead
from alipay.aop.api.domain.ChinaMobileVoucher import ChinaMobileVoucher


class ChinaMobileContractRoot(object):

    def __init__(self):
        self._body = None
        self._head = None
        self._voucher = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if isinstance(value, ChinaMobileBody):
            self._body = value
        else:
            self._body = ChinaMobileBody.from_alipay_dict(value)
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        if isinstance(value, ChinaMobileHead):
            self._head = value
        else:
            self._head = ChinaMobileHead.from_alipay_dict(value)
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, ChinaMobileVoucher):
            self._voucher = value
        else:
            self._voucher = ChinaMobileVoucher.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.head:
            if hasattr(self.head, 'to_alipay_dict'):
                params['head'] = self.head.to_alipay_dict()
            else:
                params['head'] = self.head
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChinaMobileContractRoot()
        if 'body' in d:
            o.body = d['body']
        if 'head' in d:
            o.head = d['head']
        if 'voucher' in d:
            o.voucher = d['voucher']
        return o


