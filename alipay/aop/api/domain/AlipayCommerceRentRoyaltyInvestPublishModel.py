#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentRoyaltyPublishDetailRequest import RentRoyaltyPublishDetailRequest


class AlipayCommerceRentRoyaltyInvestPublishModel(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._invest_app_id = None
        self._invest_id = None
        self._loan_amount = None
        self._operate_type = None
        self._order_id = None
        self._royalty_publish_detail = None
        self._total_royalty_price = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def invest_app_id(self):
        return self._invest_app_id

    @invest_app_id.setter
    def invest_app_id(self, value):
        self._invest_app_id = value
    @property
    def invest_id(self):
        return self._invest_id

    @invest_id.setter
    def invest_id(self, value):
        self._invest_id = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def royalty_publish_detail(self):
        return self._royalty_publish_detail

    @royalty_publish_detail.setter
    def royalty_publish_detail(self, value):
        if isinstance(value, list):
            self._royalty_publish_detail = list()
            for i in value:
                if isinstance(i, RentRoyaltyPublishDetailRequest):
                    self._royalty_publish_detail.append(i)
                else:
                    self._royalty_publish_detail.append(RentRoyaltyPublishDetailRequest.from_alipay_dict(i))
    @property
    def total_royalty_price(self):
        return self._total_royalty_price

    @total_royalty_price.setter
    def total_royalty_price(self, value):
        self._total_royalty_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.invest_app_id:
            if hasattr(self.invest_app_id, 'to_alipay_dict'):
                params['invest_app_id'] = self.invest_app_id.to_alipay_dict()
            else:
                params['invest_app_id'] = self.invest_app_id
        if self.invest_id:
            if hasattr(self.invest_id, 'to_alipay_dict'):
                params['invest_id'] = self.invest_id.to_alipay_dict()
            else:
                params['invest_id'] = self.invest_id
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.royalty_publish_detail:
            if isinstance(self.royalty_publish_detail, list):
                for i in range(0, len(self.royalty_publish_detail)):
                    element = self.royalty_publish_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_publish_detail[i] = element.to_alipay_dict()
            if hasattr(self.royalty_publish_detail, 'to_alipay_dict'):
                params['royalty_publish_detail'] = self.royalty_publish_detail.to_alipay_dict()
            else:
                params['royalty_publish_detail'] = self.royalty_publish_detail
        if self.total_royalty_price:
            if hasattr(self.total_royalty_price, 'to_alipay_dict'):
                params['total_royalty_price'] = self.total_royalty_price.to_alipay_dict()
            else:
                params['total_royalty_price'] = self.total_royalty_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentRoyaltyInvestPublishModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'invest_app_id' in d:
            o.invest_app_id = d['invest_app_id']
        if 'invest_id' in d:
            o.invest_id = d['invest_id']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'royalty_publish_detail' in d:
            o.royalty_publish_detail = d['royalty_publish_detail']
        if 'total_royalty_price' in d:
            o.total_royalty_price = d['total_royalty_price']
        return o


