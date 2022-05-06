#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryActivityContentInfo import DeliveryActivityContentInfo


class DeliveryContentInfo(object):

    def __init__(self):
        self._delivery_activity_content = None
        self._delivery_content_type = None

    @property
    def delivery_activity_content(self):
        return self._delivery_activity_content

    @delivery_activity_content.setter
    def delivery_activity_content(self, value):
        if isinstance(value, DeliveryActivityContentInfo):
            self._delivery_activity_content = value
        else:
            self._delivery_activity_content = DeliveryActivityContentInfo.from_alipay_dict(value)
    @property
    def delivery_content_type(self):
        return self._delivery_content_type

    @delivery_content_type.setter
    def delivery_content_type(self, value):
        self._delivery_content_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_activity_content:
            if hasattr(self.delivery_activity_content, 'to_alipay_dict'):
                params['delivery_activity_content'] = self.delivery_activity_content.to_alipay_dict()
            else:
                params['delivery_activity_content'] = self.delivery_activity_content
        if self.delivery_content_type:
            if hasattr(self.delivery_content_type, 'to_alipay_dict'):
                params['delivery_content_type'] = self.delivery_content_type.to_alipay_dict()
            else:
                params['delivery_content_type'] = self.delivery_content_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryContentInfo()
        if 'delivery_activity_content' in d:
            o.delivery_activity_content = d['delivery_activity_content']
        if 'delivery_content_type' in d:
            o.delivery_content_type = d['delivery_content_type']
        return o


