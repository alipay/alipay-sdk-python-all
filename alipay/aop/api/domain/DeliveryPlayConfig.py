#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFullSendConfig import DeliveryFullSendConfig
from alipay.aop.api.domain.DeliverySingleSendConfig import DeliverySingleSendConfig


class DeliveryPlayConfig(object):

    def __init__(self):
        self._delivery_full_send_config = None
        self._delivery_single_send_config = None

    @property
    def delivery_full_send_config(self):
        return self._delivery_full_send_config

    @delivery_full_send_config.setter
    def delivery_full_send_config(self, value):
        if isinstance(value, DeliveryFullSendConfig):
            self._delivery_full_send_config = value
        else:
            self._delivery_full_send_config = DeliveryFullSendConfig.from_alipay_dict(value)
    @property
    def delivery_single_send_config(self):
        return self._delivery_single_send_config

    @delivery_single_send_config.setter
    def delivery_single_send_config(self, value):
        if isinstance(value, DeliverySingleSendConfig):
            self._delivery_single_send_config = value
        else:
            self._delivery_single_send_config = DeliverySingleSendConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_full_send_config:
            if hasattr(self.delivery_full_send_config, 'to_alipay_dict'):
                params['delivery_full_send_config'] = self.delivery_full_send_config.to_alipay_dict()
            else:
                params['delivery_full_send_config'] = self.delivery_full_send_config
        if self.delivery_single_send_config:
            if hasattr(self.delivery_single_send_config, 'to_alipay_dict'):
                params['delivery_single_send_config'] = self.delivery_single_send_config.to_alipay_dict()
            else:
                params['delivery_single_send_config'] = self.delivery_single_send_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryPlayConfig()
        if 'delivery_full_send_config' in d:
            o.delivery_full_send_config = d['delivery_full_send_config']
        if 'delivery_single_send_config' in d:
            o.delivery_single_send_config = d['delivery_single_send_config']
        return o


