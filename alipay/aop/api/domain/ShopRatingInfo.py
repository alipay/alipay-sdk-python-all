#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopRatingInfo(object):

    def __init__(self):
        self._delivery_score = None
        self._itemdesc_score = None
        self._service_score = None

    @property
    def delivery_score(self):
        return self._delivery_score

    @delivery_score.setter
    def delivery_score(self, value):
        self._delivery_score = value
    @property
    def itemdesc_score(self):
        return self._itemdesc_score

    @itemdesc_score.setter
    def itemdesc_score(self, value):
        self._itemdesc_score = value
    @property
    def service_score(self):
        return self._service_score

    @service_score.setter
    def service_score(self, value):
        self._service_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_score:
            if hasattr(self.delivery_score, 'to_alipay_dict'):
                params['delivery_score'] = self.delivery_score.to_alipay_dict()
            else:
                params['delivery_score'] = self.delivery_score
        if self.itemdesc_score:
            if hasattr(self.itemdesc_score, 'to_alipay_dict'):
                params['itemdesc_score'] = self.itemdesc_score.to_alipay_dict()
            else:
                params['itemdesc_score'] = self.itemdesc_score
        if self.service_score:
            if hasattr(self.service_score, 'to_alipay_dict'):
                params['service_score'] = self.service_score.to_alipay_dict()
            else:
                params['service_score'] = self.service_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopRatingInfo()
        if 'delivery_score' in d:
            o.delivery_score = d['delivery_score']
        if 'itemdesc_score' in d:
            o.itemdesc_score = d['itemdesc_score']
        if 'service_score' in d:
            o.service_score = d['service_score']
        return o


