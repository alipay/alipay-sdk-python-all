#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaytoolRequestDetail import PaytoolRequestDetail


class AlipayBusinessOrderPayModel(object):

    def __init__(self):
        self._order_no = None
        self._paytool_list = None

    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def paytool_list(self):
        return self._paytool_list

    @paytool_list.setter
    def paytool_list(self, value):
        if isinstance(value, list):
            self._paytool_list = list()
            for i in value:
                if isinstance(i, PaytoolRequestDetail):
                    self._paytool_list.append(i)
                else:
                    self._paytool_list.append(PaytoolRequestDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.paytool_list:
            if isinstance(self.paytool_list, list):
                for i in range(0, len(self.paytool_list)):
                    element = self.paytool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.paytool_list[i] = element.to_alipay_dict()
            if hasattr(self.paytool_list, 'to_alipay_dict'):
                params['paytool_list'] = self.paytool_list.to_alipay_dict()
            else:
                params['paytool_list'] = self.paytool_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderPayModel()
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'paytool_list' in d:
            o.paytool_list = d['paytool_list']
        return o


