#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SourceOffer(object):

    def __init__(self):
        self._offer_id = None
        self._offer_type = None

    @property
    def offer_id(self):
        return self._offer_id

    @offer_id.setter
    def offer_id(self, value):
        self._offer_id = value
    @property
    def offer_type(self):
        return self._offer_type

    @offer_type.setter
    def offer_type(self, value):
        self._offer_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.offer_id:
            if hasattr(self.offer_id, 'to_alipay_dict'):
                params['offer_id'] = self.offer_id.to_alipay_dict()
            else:
                params['offer_id'] = self.offer_id
        if self.offer_type:
            if hasattr(self.offer_type, 'to_alipay_dict'):
                params['offer_type'] = self.offer_type.to_alipay_dict()
            else:
                params['offer_type'] = self.offer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SourceOffer()
        if 'offer_id' in d:
            o.offer_id = d['offer_id']
        if 'offer_type' in d:
            o.offer_type = d['offer_type']
        return o


