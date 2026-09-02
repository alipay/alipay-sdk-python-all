#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNfcexpoprodOrderdetailQueryModel(object):

    def __init__(self):
        self._coil_no = None
        self._order_id = None
        self._out_biz_no = None

    @property
    def coil_no(self):
        return self._coil_no

    @coil_no.setter
    def coil_no(self, value):
        self._coil_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.coil_no:
            if hasattr(self.coil_no, 'to_alipay_dict'):
                params['coil_no'] = self.coil_no.to_alipay_dict()
            else:
                params['coil_no'] = self.coil_no
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = AlipayOpenSpNfcexpoprodOrderdetailQueryModel()
        if 'coil_no' in d:
            o.coil_no = d['coil_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


