#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransInvoiceResubmitModifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._is_block = None
        self._uid_range = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def is_block(self):
        return self._is_block

    @is_block.setter
    def is_block(self, value):
        self._is_block = value
    @property
    def uid_range(self):
        return self._uid_range

    @uid_range.setter
    def uid_range(self, value):
        self._uid_range = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.is_block:
            if hasattr(self.is_block, 'to_alipay_dict'):
                params['is_block'] = self.is_block.to_alipay_dict()
            else:
                params['is_block'] = self.is_block
        if self.uid_range:
            if hasattr(self.uid_range, 'to_alipay_dict'):
                params['uid_range'] = self.uid_range.to_alipay_dict()
            else:
                params['uid_range'] = self.uid_range
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransInvoiceResubmitModifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'is_block' in d:
            o.is_block = d['is_block']
        if 'uid_range' in d:
            o.uid_range = d['uid_range']
        return o


