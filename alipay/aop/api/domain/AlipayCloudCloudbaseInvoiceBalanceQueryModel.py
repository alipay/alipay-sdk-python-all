#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseInvoiceBalanceQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._order_no_list = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def order_no_list(self):
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, value):
        if isinstance(value, list):
            self._order_no_list = list()
            for i in value:
                self._order_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.order_no_list:
            if isinstance(self.order_no_list, list):
                for i in range(0, len(self.order_no_list)):
                    element = self.order_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_no_list[i] = element.to_alipay_dict()
            if hasattr(self.order_no_list, 'to_alipay_dict'):
                params['order_no_list'] = self.order_no_list.to_alipay_dict()
            else:
                params['order_no_list'] = self.order_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseInvoiceBalanceQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'order_no_list' in d:
            o.order_no_list = d['order_no_list']
        return o


