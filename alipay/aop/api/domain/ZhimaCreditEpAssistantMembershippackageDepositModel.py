#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantMembershippackageDepositModel(object):

    def __init__(self):
        self._benefit_sku_code = None
        self._benefit_sku_quantity = None
        self._order_no = None
        self._out_biz_no = None
        self._package_id = None

    @property
    def benefit_sku_code(self):
        return self._benefit_sku_code

    @benefit_sku_code.setter
    def benefit_sku_code(self, value):
        self._benefit_sku_code = value
    @property
    def benefit_sku_quantity(self):
        return self._benefit_sku_quantity

    @benefit_sku_quantity.setter
    def benefit_sku_quantity(self, value):
        self._benefit_sku_quantity = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def package_id(self):
        return self._package_id

    @package_id.setter
    def package_id(self, value):
        self._package_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_sku_code:
            if hasattr(self.benefit_sku_code, 'to_alipay_dict'):
                params['benefit_sku_code'] = self.benefit_sku_code.to_alipay_dict()
            else:
                params['benefit_sku_code'] = self.benefit_sku_code
        if self.benefit_sku_quantity:
            if hasattr(self.benefit_sku_quantity, 'to_alipay_dict'):
                params['benefit_sku_quantity'] = self.benefit_sku_quantity.to_alipay_dict()
            else:
                params['benefit_sku_quantity'] = self.benefit_sku_quantity
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.package_id:
            if hasattr(self.package_id, 'to_alipay_dict'):
                params['package_id'] = self.package_id.to_alipay_dict()
            else:
                params['package_id'] = self.package_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantMembershippackageDepositModel()
        if 'benefit_sku_code' in d:
            o.benefit_sku_code = d['benefit_sku_code']
        if 'benefit_sku_quantity' in d:
            o.benefit_sku_quantity = d['benefit_sku_quantity']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'package_id' in d:
            o.package_id = d['package_id']
        return o


