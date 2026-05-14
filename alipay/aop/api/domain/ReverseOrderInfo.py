#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemThirdPartyInfo import ItemThirdPartyInfo


class ReverseOrderInfo(object):

    def __init__(self):
        self._channel_reverse_order_no = None
        self._order_status = None
        self._refund_amount = None
        self._return_item_list = None

    @property
    def channel_reverse_order_no(self):
        return self._channel_reverse_order_no

    @channel_reverse_order_no.setter
    def channel_reverse_order_no(self, value):
        self._channel_reverse_order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def return_item_list(self):
        return self._return_item_list

    @return_item_list.setter
    def return_item_list(self, value):
        if isinstance(value, list):
            self._return_item_list = list()
            for i in value:
                if isinstance(i, ItemThirdPartyInfo):
                    self._return_item_list.append(i)
                else:
                    self._return_item_list.append(ItemThirdPartyInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.channel_reverse_order_no:
            if hasattr(self.channel_reverse_order_no, 'to_alipay_dict'):
                params['channel_reverse_order_no'] = self.channel_reverse_order_no.to_alipay_dict()
            else:
                params['channel_reverse_order_no'] = self.channel_reverse_order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.return_item_list:
            if isinstance(self.return_item_list, list):
                for i in range(0, len(self.return_item_list)):
                    element = self.return_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.return_item_list[i] = element.to_alipay_dict()
            if hasattr(self.return_item_list, 'to_alipay_dict'):
                params['return_item_list'] = self.return_item_list.to_alipay_dict()
            else:
                params['return_item_list'] = self.return_item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReverseOrderInfo()
        if 'channel_reverse_order_no' in d:
            o.channel_reverse_order_no = d['channel_reverse_order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'return_item_list' in d:
            o.return_item_list = d['return_item_list']
        return o


