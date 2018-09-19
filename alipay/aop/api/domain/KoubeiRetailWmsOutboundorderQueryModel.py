#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsOutboundorderQueryModel(object):

    def __init__(self):
        self._need_detail = None
        self._out_biz_no = None
        self._outbound_order_id = None

    @property
    def need_detail(self):
        return self._need_detail

    @need_detail.setter
    def need_detail(self, value):
        self._need_detail = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def outbound_order_id(self):
        return self._outbound_order_id

    @outbound_order_id.setter
    def outbound_order_id(self, value):
        self._outbound_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_detail:
            if hasattr(self.need_detail, 'to_alipay_dict'):
                params['need_detail'] = self.need_detail.to_alipay_dict()
            else:
                params['need_detail'] = self.need_detail
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.outbound_order_id:
            if hasattr(self.outbound_order_id, 'to_alipay_dict'):
                params['outbound_order_id'] = self.outbound_order_id.to_alipay_dict()
            else:
                params['outbound_order_id'] = self.outbound_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsOutboundorderQueryModel()
        if 'need_detail' in d:
            o.need_detail = d['need_detail']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'outbound_order_id' in d:
            o.outbound_order_id = d['outbound_order_id']
        return o


