#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalSyncRequest(object):

    def __init__(self):
        self._alipay_bill_id = None
        self._out_biz_no = None

    @property
    def alipay_bill_id(self):
        return self._alipay_bill_id

    @alipay_bill_id.setter
    def alipay_bill_id(self, value):
        self._alipay_bill_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_bill_id:
            if hasattr(self.alipay_bill_id, 'to_alipay_dict'):
                params['alipay_bill_id'] = self.alipay_bill_id.to_alipay_dict()
            else:
                params['alipay_bill_id'] = self.alipay_bill_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalSyncRequest()
        if 'alipay_bill_id' in d:
            o.alipay_bill_id = d['alipay_bill_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


