#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherStockUseModel(object):

    def __init__(self):
        self._entity_no = None
        self._out_biz_no = None

    @property
    def entity_no(self):
        return self._entity_no

    @entity_no.setter
    def entity_no(self, value):
        self._entity_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.entity_no:
            if hasattr(self.entity_no, 'to_alipay_dict'):
                params['entity_no'] = self.entity_no.to_alipay_dict()
            else:
                params['entity_no'] = self.entity_no
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
        o = AlipayMarketingVoucherStockUseModel()
        if 'entity_no' in d:
            o.entity_no = d['entity_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


