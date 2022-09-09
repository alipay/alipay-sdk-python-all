#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneQuoteDetailQueryModel(object):

    def __init__(self):
        self._out_order_id = None
        self._partner_org_id = None
        self._product_plan_id = None
        self._quote_id = None

    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def quote_id(self):
        return self._quote_id

    @quote_id.setter
    def quote_id(self, value):
        self._quote_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.quote_id:
            if hasattr(self.quote_id, 'to_alipay_dict'):
                params['quote_id'] = self.quote_id.to_alipay_dict()
            else:
                params['quote_id'] = self.quote_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneQuoteDetailQueryModel()
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'quote_id' in d:
            o.quote_id = d['quote_id']
        return o


