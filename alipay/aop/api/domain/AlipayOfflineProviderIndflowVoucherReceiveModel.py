#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderIndflowVoucherReceiveModel(object):

    def __init__(self):
        self._mobile_phone = None
        self._record_id = None
        self._send_order_ids = None

    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def send_order_ids(self):
        return self._send_order_ids

    @send_order_ids.setter
    def send_order_ids(self, value):
        if isinstance(value, list):
            self._send_order_ids = list()
            for i in value:
                self._send_order_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.send_order_ids:
            if isinstance(self.send_order_ids, list):
                for i in range(0, len(self.send_order_ids)):
                    element = self.send_order_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.send_order_ids[i] = element.to_alipay_dict()
            if hasattr(self.send_order_ids, 'to_alipay_dict'):
                params['send_order_ids'] = self.send_order_ids.to_alipay_dict()
            else:
                params['send_order_ids'] = self.send_order_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndflowVoucherReceiveModel()
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'send_order_ids' in d:
            o.send_order_ids = d['send_order_ids']
        return o


