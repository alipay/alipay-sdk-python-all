#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliverySendGuide(object):

    def __init__(self):
        self._delivery_guide_url = None

    @property
    def delivery_guide_url(self):
        return self._delivery_guide_url

    @delivery_guide_url.setter
    def delivery_guide_url(self, value):
        self._delivery_guide_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_guide_url:
            if hasattr(self.delivery_guide_url, 'to_alipay_dict'):
                params['delivery_guide_url'] = self.delivery_guide_url.to_alipay_dict()
            else:
                params['delivery_guide_url'] = self.delivery_guide_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliverySendGuide()
        if 'delivery_guide_url' in d:
            o.delivery_guide_url = d['delivery_guide_url']
        return o


