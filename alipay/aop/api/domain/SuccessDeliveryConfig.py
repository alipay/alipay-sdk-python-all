#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryConfig import DeliveryConfig


class SuccessDeliveryConfig(object):

    def __init__(self):
        self._delivery_config = None

    @property
    def delivery_config(self):
        return self._delivery_config

    @delivery_config.setter
    def delivery_config(self, value):
        if isinstance(value, DeliveryConfig):
            self._delivery_config = value
        else:
            self._delivery_config = DeliveryConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_config:
            if hasattr(self.delivery_config, 'to_alipay_dict'):
                params['delivery_config'] = self.delivery_config.to_alipay_dict()
            else:
                params['delivery_config'] = self.delivery_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SuccessDeliveryConfig()
        if 'delivery_config' in d:
            o.delivery_config = d['delivery_config']
        return o


