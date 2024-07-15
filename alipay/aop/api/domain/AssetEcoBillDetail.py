#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetEcoOrderBillDetail import AssetEcoOrderBillDetail


class AssetEcoBillDetail(object):

    def __init__(self):
        self._bill_entity = None
        self._bill_no = None
        self._eco_code = None
        self._eco_order_bill_details = None
        self._fee_price = None
        self._shop_code = None

    @property
    def bill_entity(self):
        return self._bill_entity

    @bill_entity.setter
    def bill_entity(self, value):
        self._bill_entity = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def eco_order_bill_details(self):
        return self._eco_order_bill_details

    @eco_order_bill_details.setter
    def eco_order_bill_details(self, value):
        if isinstance(value, list):
            self._eco_order_bill_details = list()
            for i in value:
                if isinstance(i, AssetEcoOrderBillDetail):
                    self._eco_order_bill_details.append(i)
                else:
                    self._eco_order_bill_details.append(AssetEcoOrderBillDetail.from_alipay_dict(i))
    @property
    def fee_price(self):
        return self._fee_price

    @fee_price.setter
    def fee_price(self, value):
        self._fee_price = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entity:
            if hasattr(self.bill_entity, 'to_alipay_dict'):
                params['bill_entity'] = self.bill_entity.to_alipay_dict()
            else:
                params['bill_entity'] = self.bill_entity
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.eco_order_bill_details:
            if isinstance(self.eco_order_bill_details, list):
                for i in range(0, len(self.eco_order_bill_details)):
                    element = self.eco_order_bill_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.eco_order_bill_details[i] = element.to_alipay_dict()
            if hasattr(self.eco_order_bill_details, 'to_alipay_dict'):
                params['eco_order_bill_details'] = self.eco_order_bill_details.to_alipay_dict()
            else:
                params['eco_order_bill_details'] = self.eco_order_bill_details
        if self.fee_price:
            if hasattr(self.fee_price, 'to_alipay_dict'):
                params['fee_price'] = self.fee_price.to_alipay_dict()
            else:
                params['fee_price'] = self.fee_price
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoBillDetail()
        if 'bill_entity' in d:
            o.bill_entity = d['bill_entity']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'eco_order_bill_details' in d:
            o.eco_order_bill_details = d['eco_order_bill_details']
        if 'fee_price' in d:
            o.fee_price = d['fee_price']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        return o


