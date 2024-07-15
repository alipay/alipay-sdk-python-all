#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcDeliveryInfo(object):

    def __init__(self):
        self._display_name = None
        self._id = None
        self._post_fee = None

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def post_fee(self):
        return self._post_fee

    @post_fee.setter
    def post_fee(self, value):
        self._post_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.post_fee:
            if hasattr(self.post_fee, 'to_alipay_dict'):
                params['post_fee'] = self.post_fee.to_alipay_dict()
            else:
                params['post_fee'] = self.post_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcDeliveryInfo()
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'id' in d:
            o.id = d['id']
        if 'post_fee' in d:
            o.post_fee = d['post_fee']
        return o


