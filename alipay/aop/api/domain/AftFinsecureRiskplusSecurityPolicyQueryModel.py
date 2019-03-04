#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EventInfo import EventInfo


class AftFinsecureRiskplusSecurityPolicyQueryModel(object):

    def __init__(self):
        self._event_info = None
        self._product_instance_id = None

    @property
    def event_info(self):
        return self._event_info

    @event_info.setter
    def event_info(self, value):
        if isinstance(value, EventInfo):
            self._event_info = value
        else:
            self._event_info = EventInfo.from_alipay_dict(value)
    @property
    def product_instance_id(self):
        return self._product_instance_id

    @product_instance_id.setter
    def product_instance_id(self, value):
        self._product_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_info:
            if hasattr(self.event_info, 'to_alipay_dict'):
                params['event_info'] = self.event_info.to_alipay_dict()
            else:
                params['event_info'] = self.event_info
        if self.product_instance_id:
            if hasattr(self.product_instance_id, 'to_alipay_dict'):
                params['product_instance_id'] = self.product_instance_id.to_alipay_dict()
            else:
                params['product_instance_id'] = self.product_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftFinsecureRiskplusSecurityPolicyQueryModel()
        if 'event_info' in d:
            o.event_info = d['event_info']
        if 'product_instance_id' in d:
            o.product_instance_id = d['product_instance_id']
        return o


