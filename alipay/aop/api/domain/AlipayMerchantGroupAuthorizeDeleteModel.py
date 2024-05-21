#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupAuthorizeDeleteModel(object):

    def __init__(self):
        self._authorize_id = None

    @property
    def authorize_id(self):
        return self._authorize_id

    @authorize_id.setter
    def authorize_id(self, value):
        self._authorize_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorize_id:
            if hasattr(self.authorize_id, 'to_alipay_dict'):
                params['authorize_id'] = self.authorize_id.to_alipay_dict()
            else:
                params['authorize_id'] = self.authorize_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupAuthorizeDeleteModel()
        if 'authorize_id' in d:
            o.authorize_id = d['authorize_id']
        return o


