#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupAutoreplyQueryModel(object):

    def __init__(self):
        self._autoreply_id = None

    @property
    def autoreply_id(self):
        return self._autoreply_id

    @autoreply_id.setter
    def autoreply_id(self, value):
        self._autoreply_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.autoreply_id:
            if hasattr(self.autoreply_id, 'to_alipay_dict'):
                params['autoreply_id'] = self.autoreply_id.to_alipay_dict()
            else:
                params['autoreply_id'] = self.autoreply_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupAutoreplyQueryModel()
        if 'autoreply_id' in d:
            o.autoreply_id = d['autoreply_id']
        return o


