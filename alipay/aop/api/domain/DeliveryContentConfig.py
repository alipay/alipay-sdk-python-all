#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliverySendGuide import DeliverySendGuide


class DeliveryContentConfig(object):

    def __init__(self):
        self._delivery_send_guide = None

    @property
    def delivery_send_guide(self):
        return self._delivery_send_guide

    @delivery_send_guide.setter
    def delivery_send_guide(self, value):
        if isinstance(value, DeliverySendGuide):
            self._delivery_send_guide = value
        else:
            self._delivery_send_guide = DeliverySendGuide.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_send_guide:
            if hasattr(self.delivery_send_guide, 'to_alipay_dict'):
                params['delivery_send_guide'] = self.delivery_send_guide.to_alipay_dict()
            else:
                params['delivery_send_guide'] = self.delivery_send_guide
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryContentConfig()
        if 'delivery_send_guide' in d:
            o.delivery_send_guide = d['delivery_send_guide']
        return o


