#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryContentInfo import DeliveryContentInfo


class DeliveryFullSendConfig(object):

    def __init__(self):
        self._delivery_content_info = None
        self._delivery_floor_amount = None

    @property
    def delivery_content_info(self):
        return self._delivery_content_info

    @delivery_content_info.setter
    def delivery_content_info(self, value):
        if isinstance(value, DeliveryContentInfo):
            self._delivery_content_info = value
        else:
            self._delivery_content_info = DeliveryContentInfo.from_alipay_dict(value)
    @property
    def delivery_floor_amount(self):
        return self._delivery_floor_amount

    @delivery_floor_amount.setter
    def delivery_floor_amount(self, value):
        self._delivery_floor_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_content_info:
            if hasattr(self.delivery_content_info, 'to_alipay_dict'):
                params['delivery_content_info'] = self.delivery_content_info.to_alipay_dict()
            else:
                params['delivery_content_info'] = self.delivery_content_info
        if self.delivery_floor_amount:
            if hasattr(self.delivery_floor_amount, 'to_alipay_dict'):
                params['delivery_floor_amount'] = self.delivery_floor_amount.to_alipay_dict()
            else:
                params['delivery_floor_amount'] = self.delivery_floor_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryFullSendConfig()
        if 'delivery_content_info' in d:
            o.delivery_content_info = d['delivery_content_info']
        if 'delivery_floor_amount' in d:
            o.delivery_floor_amount = d['delivery_floor_amount']
        return o


