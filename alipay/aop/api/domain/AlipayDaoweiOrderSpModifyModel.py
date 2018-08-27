#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDaoweiOrderSpModifyModel(object):

    def __init__(self):
        self._order_no = None
        self._out_sp_id = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_sp_id(self):
        return self._out_sp_id

    @out_sp_id.setter
    def out_sp_id(self, value):
        self._out_sp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_sp_id:
            if hasattr(self.out_sp_id, 'to_alipay_dict'):
                params['out_sp_id'] = self.out_sp_id.to_alipay_dict()
            else:
                params['out_sp_id'] = self.out_sp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDaoweiOrderSpModifyModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_sp_id' in d:
            o.out_sp_id = d['out_sp_id']
        return o


