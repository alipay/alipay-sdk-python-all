#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemConsultRequest import ItemConsultRequest


class AlipayMarketingCampaignOrderVoucherConsultModel(object):

    def __init__(self):
        self._item_consult_list = None
        self._order_amount = None
        self._scene_code = None
        self._specified_app_id = None

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
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        if isinstance(value, list):
            self._scene_code = list()
            for i in value:
                self._scene_code.append(i)
    @property
    def specified_app_id(self):
        return self._specified_app_id

    @specified_app_id.setter
    def specified_app_id(self, value):
        self._specified_app_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.scene_code:
            if isinstance(self.scene_code, list):
                for i in range(0, len(self.scene_code)):
                    element = self.scene_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_code[i] = element.to_alipay_dict()
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.specified_app_id:
            if hasattr(self.specified_app_id, 'to_alipay_dict'):
                params['specified_app_id'] = self.specified_app_id.to_alipay_dict()
            else:
                params['specified_app_id'] = self.specified_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignOrderVoucherConsultModel()
        if 'item_consult_list' in d:
            o.item_consult_list = d['item_consult_list']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'specified_app_id' in d:
            o.specified_app_id = d['specified_app_id']
        return o


