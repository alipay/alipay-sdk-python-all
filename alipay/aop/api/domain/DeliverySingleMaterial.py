#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliverySingleMaterial(object):

    def __init__(self):
        self._delivery_image = None

    @property
    def delivery_image(self):
        return self._delivery_image

    @delivery_image.setter
    def delivery_image(self, value):
        self._delivery_image = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_image:
            if hasattr(self.delivery_image, 'to_alipay_dict'):
                params['delivery_image'] = self.delivery_image.to_alipay_dict()
            else:
                params['delivery_image'] = self.delivery_image
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliverySingleMaterial()
        if 'delivery_image' in d:
            o.delivery_image = d['delivery_image']
        return o


