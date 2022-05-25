#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryContentConfig import DeliveryContentConfig
from alipay.aop.api.domain.DeliveryContentInfo import DeliveryContentInfo


class DeliverySingleSendConfig(object):

    def __init__(self):
        self._delivery_content_config = None
        self._delivery_content_info = None

    @property
    def delivery_content_config(self):
        return self._delivery_content_config

    @delivery_content_config.setter
    def delivery_content_config(self, value):
        if isinstance(value, DeliveryContentConfig):
            self._delivery_content_config = value
        else:
            self._delivery_content_config = DeliveryContentConfig.from_alipay_dict(value)
    @property
    def delivery_content_info(self):
        return self._delivery_content_info

    @delivery_content_info.setter
    def delivery_content_info(self, value):
        if isinstance(value, DeliveryContentInfo):
            self._delivery_content_info = value
        else:
            self._delivery_content_info = DeliveryContentInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_content_config:
            if hasattr(self.delivery_content_config, 'to_alipay_dict'):
                params['delivery_content_config'] = self.delivery_content_config.to_alipay_dict()
            else:
                params['delivery_content_config'] = self.delivery_content_config
        if self.delivery_content_info:
            if hasattr(self.delivery_content_info, 'to_alipay_dict'):
                params['delivery_content_info'] = self.delivery_content_info.to_alipay_dict()
            else:
                params['delivery_content_info'] = self.delivery_content_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliverySingleSendConfig()
        if 'delivery_content_config' in d:
            o.delivery_content_config = d['delivery_content_config']
        if 'delivery_content_info' in d:
            o.delivery_content_info = d['delivery_content_info']
        return o


