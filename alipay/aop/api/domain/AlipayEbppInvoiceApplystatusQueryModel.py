#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceApplystatusQueryModel(object):

    def __init__(self):
        self._m_short_name = None
        self._order_no_list = None
        self._sub_m_short_name = None

    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def order_no_list(self):
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, value):
        if isinstance(value, list):
            self._order_no_list = list()
            for i in value:
                self._order_no_list.append(i)
    @property
    def sub_m_short_name(self):
        return self._sub_m_short_name

    @sub_m_short_name.setter
    def sub_m_short_name(self, value):
        self._sub_m_short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
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
        if self.sub_m_short_name:
            if hasattr(self.sub_m_short_name, 'to_alipay_dict'):
                params['sub_m_short_name'] = self.sub_m_short_name.to_alipay_dict()
            else:
                params['sub_m_short_name'] = self.sub_m_short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceApplystatusQueryModel()
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'order_no_list' in d:
            o.order_no_list = d['order_no_list']
        if 'sub_m_short_name' in d:
            o.sub_m_short_name = d['sub_m_short_name']
        return o


