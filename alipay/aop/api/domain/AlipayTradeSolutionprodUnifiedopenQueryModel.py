#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSolutionprodUnifiedopenQueryModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._uniopen_order_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def uniopen_order_id(self):
        return self._uniopen_order_id

    @uniopen_order_id.setter
    def uniopen_order_id(self, value):
        self._uniopen_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.uniopen_order_id:
            if hasattr(self.uniopen_order_id, 'to_alipay_dict'):
                params['uniopen_order_id'] = self.uniopen_order_id.to_alipay_dict()
            else:
                params['uniopen_order_id'] = self.uniopen_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSolutionprodUnifiedopenQueryModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'uniopen_order_id' in d:
            o.uniopen_order_id = d['uniopen_order_id']
        return o


