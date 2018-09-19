#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsInboundorderQueryModel(object):

    def __init__(self):
        self._inbound_order_id = None
        self._need_detail = None
        self._out_biz_no = None

    @property
    def inbound_order_id(self):
        return self._inbound_order_id

    @inbound_order_id.setter
    def inbound_order_id(self, value):
        self._inbound_order_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.inbound_order_id:
            if hasattr(self.inbound_order_id, 'to_alipay_dict'):
                params['inbound_order_id'] = self.inbound_order_id.to_alipay_dict()
            else:
                params['inbound_order_id'] = self.inbound_order_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsInboundorderQueryModel()
        if 'inbound_order_id' in d:
            o.inbound_order_id = d['inbound_order_id']
        if 'need_detail' in d:
            o.need_detail = d['need_detail']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


