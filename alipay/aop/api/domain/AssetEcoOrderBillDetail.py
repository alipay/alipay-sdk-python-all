#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetEcoFeeDetail import AssetEcoFeeDetail


class AssetEcoOrderBillDetail(object):

    def __init__(self):
        self._actual_fee_price = None
        self._bill_entity = None
        self._bill_status = None
        self._busi_platform = None
        self._correct_fee_price = None
        self._eco_code = None
        self._eco_fee_details = None
        self._eco_order_id = None
        self._order_date = None
        self._out_order_id = None
        self._shop_code = None
        self._unbill_reason = None

    @property
    def actual_fee_price(self):
        return self._actual_fee_price

    @actual_fee_price.setter
    def actual_fee_price(self, value):
        self._actual_fee_price = value
    @property
    def bill_entity(self):
        return self._bill_entity

    @bill_entity.setter
    def bill_entity(self, value):
        self._bill_entity = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def busi_platform(self):
        return self._busi_platform

    @busi_platform.setter
    def busi_platform(self, value):
        self._busi_platform = value
    @property
    def correct_fee_price(self):
        return self._correct_fee_price

    @correct_fee_price.setter
    def correct_fee_price(self, value):
        self._correct_fee_price = value
    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def eco_fee_details(self):
        return self._eco_fee_details

    @eco_fee_details.setter
    def eco_fee_details(self, value):
        if isinstance(value, list):
            self._eco_fee_details = list()
            for i in value:
                if isinstance(i, AssetEcoFeeDetail):
                    self._eco_fee_details.append(i)
                else:
                    self._eco_fee_details.append(AssetEcoFeeDetail.from_alipay_dict(i))
    @property
    def eco_order_id(self):
        return self._eco_order_id

    @eco_order_id.setter
    def eco_order_id(self, value):
        self._eco_order_id = value
    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self._order_date = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def shop_code(self):
        return self._shop_code

    @shop_code.setter
    def shop_code(self, value):
        self._shop_code = value
    @property
    def unbill_reason(self):
        return self._unbill_reason

    @unbill_reason.setter
    def unbill_reason(self, value):
        self._unbill_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_fee_price:
            if hasattr(self.actual_fee_price, 'to_alipay_dict'):
                params['actual_fee_price'] = self.actual_fee_price.to_alipay_dict()
            else:
                params['actual_fee_price'] = self.actual_fee_price
        if self.bill_entity:
            if hasattr(self.bill_entity, 'to_alipay_dict'):
                params['bill_entity'] = self.bill_entity.to_alipay_dict()
            else:
                params['bill_entity'] = self.bill_entity
        if self.bill_status:
            if hasattr(self.bill_status, 'to_alipay_dict'):
                params['bill_status'] = self.bill_status.to_alipay_dict()
            else:
                params['bill_status'] = self.bill_status
        if self.busi_platform:
            if hasattr(self.busi_platform, 'to_alipay_dict'):
                params['busi_platform'] = self.busi_platform.to_alipay_dict()
            else:
                params['busi_platform'] = self.busi_platform
        if self.correct_fee_price:
            if hasattr(self.correct_fee_price, 'to_alipay_dict'):
                params['correct_fee_price'] = self.correct_fee_price.to_alipay_dict()
            else:
                params['correct_fee_price'] = self.correct_fee_price
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.eco_fee_details:
            if isinstance(self.eco_fee_details, list):
                for i in range(0, len(self.eco_fee_details)):
                    element = self.eco_fee_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.eco_fee_details[i] = element.to_alipay_dict()
            if hasattr(self.eco_fee_details, 'to_alipay_dict'):
                params['eco_fee_details'] = self.eco_fee_details.to_alipay_dict()
            else:
                params['eco_fee_details'] = self.eco_fee_details
        if self.eco_order_id:
            if hasattr(self.eco_order_id, 'to_alipay_dict'):
                params['eco_order_id'] = self.eco_order_id.to_alipay_dict()
            else:
                params['eco_order_id'] = self.eco_order_id
        if self.order_date:
            if hasattr(self.order_date, 'to_alipay_dict'):
                params['order_date'] = self.order_date.to_alipay_dict()
            else:
                params['order_date'] = self.order_date
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.shop_code:
            if hasattr(self.shop_code, 'to_alipay_dict'):
                params['shop_code'] = self.shop_code.to_alipay_dict()
            else:
                params['shop_code'] = self.shop_code
        if self.unbill_reason:
            if hasattr(self.unbill_reason, 'to_alipay_dict'):
                params['unbill_reason'] = self.unbill_reason.to_alipay_dict()
            else:
                params['unbill_reason'] = self.unbill_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoOrderBillDetail()
        if 'actual_fee_price' in d:
            o.actual_fee_price = d['actual_fee_price']
        if 'bill_entity' in d:
            o.bill_entity = d['bill_entity']
        if 'bill_status' in d:
            o.bill_status = d['bill_status']
        if 'busi_platform' in d:
            o.busi_platform = d['busi_platform']
        if 'correct_fee_price' in d:
            o.correct_fee_price = d['correct_fee_price']
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'eco_fee_details' in d:
            o.eco_fee_details = d['eco_fee_details']
        if 'eco_order_id' in d:
            o.eco_order_id = d['eco_order_id']
        if 'order_date' in d:
            o.order_date = d['order_date']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'shop_code' in d:
            o.shop_code = d['shop_code']
        if 'unbill_reason' in d:
            o.unbill_reason = d['unbill_reason']
        return o


