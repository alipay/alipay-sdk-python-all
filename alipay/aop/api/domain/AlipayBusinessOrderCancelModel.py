#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaytoolCancelRequestDetail import PaytoolCancelRequestDetail


class AlipayBusinessOrderCancelModel(object):

    def __init__(self):
        self._cancel_paytool_list = None
        self._merchant_order_no = None
        self._order_no = None

    @property
    def cancel_paytool_list(self):
        return self._cancel_paytool_list

    @cancel_paytool_list.setter
    def cancel_paytool_list(self, value):
        if isinstance(value, list):
            self._cancel_paytool_list = list()
            for i in value:
                if isinstance(i, PaytoolCancelRequestDetail):
                    self._cancel_paytool_list.append(i)
                else:
                    self._cancel_paytool_list.append(PaytoolCancelRequestDetail.from_alipay_dict(i))
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_paytool_list:
            if isinstance(self.cancel_paytool_list, list):
                for i in range(0, len(self.cancel_paytool_list)):
                    element = self.cancel_paytool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cancel_paytool_list[i] = element.to_alipay_dict()
            if hasattr(self.cancel_paytool_list, 'to_alipay_dict'):
                params['cancel_paytool_list'] = self.cancel_paytool_list.to_alipay_dict()
            else:
                params['cancel_paytool_list'] = self.cancel_paytool_list
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderCancelModel()
        if 'cancel_paytool_list' in d:
            o.cancel_paytool_list = d['cancel_paytool_list']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


