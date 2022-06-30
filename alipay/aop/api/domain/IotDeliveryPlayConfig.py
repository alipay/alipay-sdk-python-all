#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotDeliveryContentInfo import IotDeliveryContentInfo


class IotDeliveryPlayConfig(object):

    def __init__(self):
        self._delivery_content_info = None

    @property
    def delivery_content_info(self):
        return self._delivery_content_info

    @delivery_content_info.setter
    def delivery_content_info(self, value):
        if isinstance(value, IotDeliveryContentInfo):
            self._delivery_content_info = value
        else:
            self._delivery_content_info = IotDeliveryContentInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        o = IotDeliveryPlayConfig()
        if 'delivery_content_info' in d:
            o.delivery_content_info = d['delivery_content_info']
        return o


