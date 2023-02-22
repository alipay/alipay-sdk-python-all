#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemConsultRequest import ItemConsultRequest


class AlipayMarketingAssetPreconsultModel(object):

    def __init__(self):
        self._business_param = None
        self._item_consult_list = None
        self._open_id = None
        self._order_amount = None
        self._promo_rule = None
        self._scene_code = None
        self._specified_app_id = None
        self._user_id = None

    @property
    def business_param(self):
        return self._business_param

    @business_param.setter
    def business_param(self, value):
        self._business_param = value
    @property
    def item_consult_list(self):
        return self._item_consult_list

    @item_consult_list.setter
    def item_consult_list(self, value):
        if isinstance(value, list):
            self._item_consult_list = list()
            for i in value:
                if isinstance(i, ItemConsultRequest):
                    self._item_consult_list.append(i)
                else:
                    self._item_consult_list.append(ItemConsultRequest.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def promo_rule(self):
        return self._promo_rule

    @promo_rule.setter
    def promo_rule(self, value):
        self._promo_rule = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def specified_app_id(self):
        return self._specified_app_id

    @specified_app_id.setter
    def specified_app_id(self, value):
        self._specified_app_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_param:
            if hasattr(self.business_param, 'to_alipay_dict'):
                params['business_param'] = self.business_param.to_alipay_dict()
            else:
                params['business_param'] = self.business_param
        if self.item_consult_list:
            if isinstance(self.item_consult_list, list):
                for i in range(0, len(self.item_consult_list)):
                    element = self.item_consult_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_consult_list[i] = element.to_alipay_dict()
            if hasattr(self.item_consult_list, 'to_alipay_dict'):
                params['item_consult_list'] = self.item_consult_list.to_alipay_dict()
            else:
                params['item_consult_list'] = self.item_consult_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.promo_rule:
            if hasattr(self.promo_rule, 'to_alipay_dict'):
                params['promo_rule'] = self.promo_rule.to_alipay_dict()
            else:
                params['promo_rule'] = self.promo_rule
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.specified_app_id:
            if hasattr(self.specified_app_id, 'to_alipay_dict'):
                params['specified_app_id'] = self.specified_app_id.to_alipay_dict()
            else:
                params['specified_app_id'] = self.specified_app_id
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
        o = AlipayMarketingAssetPreconsultModel()
        if 'business_param' in d:
            o.business_param = d['business_param']
        if 'item_consult_list' in d:
            o.item_consult_list = d['item_consult_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'promo_rule' in d:
            o.promo_rule = d['promo_rule']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'specified_app_id' in d:
            o.specified_app_id = d['specified_app_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


