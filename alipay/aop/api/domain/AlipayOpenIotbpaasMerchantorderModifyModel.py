#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceOrderStatus import DeviceOrderStatus


class AlipayOpenIotbpaasMerchantorderModifyModel(object):

    def __init__(self):
        self._device_order_status_list = None

    @property
    def device_order_status_list(self):
        return self._device_order_status_list

    @device_order_status_list.setter
    def device_order_status_list(self, value):
        if isinstance(value, list):
            self._device_order_status_list = list()
            for i in value:
                if isinstance(i, DeviceOrderStatus):
                    self._device_order_status_list.append(i)
                else:
                    self._device_order_status_list.append(DeviceOrderStatus.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.device_order_status_list:
            if isinstance(self.device_order_status_list, list):
                for i in range(0, len(self.device_order_status_list)):
                    element = self.device_order_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_order_status_list[i] = element.to_alipay_dict()
            if hasattr(self.device_order_status_list, 'to_alipay_dict'):
                params['device_order_status_list'] = self.device_order_status_list.to_alipay_dict()
            else:
                params['device_order_status_list'] = self.device_order_status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotbpaasMerchantorderModifyModel()
        if 'device_order_status_list' in d:
            o.device_order_status_list = d['device_order_status_list']
        return o


