#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentInfo import FulfillmentInfo


class ZhimaCreditEpSceneFulfillmentlistSyncModel(object):

    def __init__(self):
        self._credit_order_no = None
        self._fulfillment_info_list = None

    @property
    def credit_order_no(self):
        return self._credit_order_no

    @credit_order_no.setter
    def credit_order_no(self, value):
        self._credit_order_no = value
    @property
    def fulfillment_info_list(self):
        return self._fulfillment_info_list

    @fulfillment_info_list.setter
    def fulfillment_info_list(self, value):
        if isinstance(value, list):
            self._fulfillment_info_list = list()
            for i in value:
                if isinstance(i, FulfillmentInfo):
                    self._fulfillment_info_list.append(i)
                else:
                    self._fulfillment_info_list.append(FulfillmentInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.credit_order_no:
            if hasattr(self.credit_order_no, 'to_alipay_dict'):
                params['credit_order_no'] = self.credit_order_no.to_alipay_dict()
            else:
                params['credit_order_no'] = self.credit_order_no
        if self.fulfillment_info_list:
            if isinstance(self.fulfillment_info_list, list):
                for i in range(0, len(self.fulfillment_info_list)):
                    element = self.fulfillment_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fulfillment_info_list[i] = element.to_alipay_dict()
            if hasattr(self.fulfillment_info_list, 'to_alipay_dict'):
                params['fulfillment_info_list'] = self.fulfillment_info_list.to_alipay_dict()
            else:
                params['fulfillment_info_list'] = self.fulfillment_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpSceneFulfillmentlistSyncModel()
        if 'credit_order_no' in d:
            o.credit_order_no = d['credit_order_no']
        if 'fulfillment_info_list' in d:
            o.fulfillment_info_list = d['fulfillment_info_list']
        return o


