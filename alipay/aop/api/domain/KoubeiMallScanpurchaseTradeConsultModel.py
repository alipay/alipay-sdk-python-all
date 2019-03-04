#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallGoodsDetail import MallGoodsDetail


class KoubeiMallScanpurchaseTradeConsultModel(object):

    def __init__(self):
        self._goods_detail = None
        self._partner_id = None
        self._request_id = None
        self._shop_id = None
        self._total_amount = None
        self._undiscountable_amount = None
        self._user_id = None

    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, MallGoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(MallGoodsDetail.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMallScanpurchaseTradeConsultModel()
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


