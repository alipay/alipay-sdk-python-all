#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CaptureCreateOrder import CaptureCreateOrder


class AlipayBossFncSettleCaptureCreateModel(object):

    def __init__(self):
        self._capture_create_order_list = None

    @property
    def capture_create_order_list(self):
        return self._capture_create_order_list

    @capture_create_order_list.setter
    def capture_create_order_list(self, value):
        if isinstance(value, list):
            self._capture_create_order_list = list()
            for i in value:
                if isinstance(i, CaptureCreateOrder):
                    self._capture_create_order_list.append(i)
                else:
                    self._capture_create_order_list.append(CaptureCreateOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.capture_create_order_list:
            if isinstance(self.capture_create_order_list, list):
                for i in range(0, len(self.capture_create_order_list)):
                    element = self.capture_create_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.capture_create_order_list[i] = element.to_alipay_dict()
            if hasattr(self.capture_create_order_list, 'to_alipay_dict'):
                params['capture_create_order_list'] = self.capture_create_order_list.to_alipay_dict()
            else:
                params['capture_create_order_list'] = self.capture_create_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSettleCaptureCreateModel()
        if 'capture_create_order_list' in d:
            o.capture_create_order_list = d['capture_create_order_list']
        return o


