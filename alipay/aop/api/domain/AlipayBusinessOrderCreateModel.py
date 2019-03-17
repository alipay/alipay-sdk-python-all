#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity
from alipay.aop.api.domain.ControlInfo import ControlInfo
from alipay.aop.api.domain.EnvInfo import EnvInfo
from alipay.aop.api.domain.ItemDetail import ItemDetail
from alipay.aop.api.domain.MarketingSelectionInfo import MarketingSelectionInfo
from alipay.aop.api.domain.UserIdentity import UserIdentity


class AlipayBusinessOrderCreateModel(object):

    def __init__(self):
        self._buyer_identity = None
        self._control_info = None
        self._env_info = None
        self._item_list = None
        self._merchant_order_no = None
        self._order_amount = None
        self._selected_marketing = None
        self._seller_identity = None
        self._title = None

    @property
    def buyer_identity(self):
        return self._buyer_identity

    @buyer_identity.setter
    def buyer_identity(self, value):
        if isinstance(value, UserIdentity):
            self._buyer_identity = value
        else:
            self._buyer_identity = UserIdentity.from_alipay_dict(value)
    @property
    def control_info(self):
        return self._control_info

    @control_info.setter
    def control_info(self, value):
        if isinstance(value, ControlInfo):
            self._control_info = value
        else:
            self._control_info = ControlInfo.from_alipay_dict(value)
    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, EnvInfo):
            self._env_info = value
        else:
            self._env_info = EnvInfo.from_alipay_dict(value)
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemDetail):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemDetail.from_alipay_dict(i))
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def selected_marketing(self):
        return self._selected_marketing

    @selected_marketing.setter
    def selected_marketing(self, value):
        if isinstance(value, MarketingSelectionInfo):
            self._selected_marketing = value
        else:
            self._selected_marketing = MarketingSelectionInfo.from_alipay_dict(value)
    @property
    def seller_identity(self):
        return self._seller_identity

    @seller_identity.setter
    def seller_identity(self, value):
        if isinstance(value, UserIdentity):
            self._seller_identity = value
        else:
            self._seller_identity = UserIdentity.from_alipay_dict(value)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_identity:
            if hasattr(self.buyer_identity, 'to_alipay_dict'):
                params['buyer_identity'] = self.buyer_identity.to_alipay_dict()
            else:
                params['buyer_identity'] = self.buyer_identity
        if self.control_info:
            if hasattr(self.control_info, 'to_alipay_dict'):
                params['control_info'] = self.control_info.to_alipay_dict()
            else:
                params['control_info'] = self.control_info
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.selected_marketing:
            if hasattr(self.selected_marketing, 'to_alipay_dict'):
                params['selected_marketing'] = self.selected_marketing.to_alipay_dict()
            else:
                params['selected_marketing'] = self.selected_marketing
        if self.seller_identity:
            if hasattr(self.seller_identity, 'to_alipay_dict'):
                params['seller_identity'] = self.seller_identity.to_alipay_dict()
            else:
                params['seller_identity'] = self.seller_identity
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderCreateModel()
        if 'buyer_identity' in d:
            o.buyer_identity = d['buyer_identity']
        if 'control_info' in d:
            o.control_info = d['control_info']
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'selected_marketing' in d:
            o.selected_marketing = d['selected_marketing']
        if 'seller_identity' in d:
            o.seller_identity = d['seller_identity']
        if 'title' in d:
            o.title = d['title']
        return o


