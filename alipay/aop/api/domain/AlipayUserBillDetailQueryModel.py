#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserBillDetailQueryModel(object):

    def __init__(self):
        self._biz_in_no = None

    @property
    def biz_in_no(self):
        return self._biz_in_no

    @biz_in_no.setter
    def biz_in_no(self, value):
        self._biz_in_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_in_no:
            if hasattr(self.biz_in_no, 'to_alipay_dict'):
                params['biz_in_no'] = self.biz_in_no.to_alipay_dict()
            else:
                params['biz_in_no'] = self.biz_in_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserBillDetailQueryModel()
        if 'biz_in_no' in d:
            o.biz_in_no = d['biz_in_no']
        return o


