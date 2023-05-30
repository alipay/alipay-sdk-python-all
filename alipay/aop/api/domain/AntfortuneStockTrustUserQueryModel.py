#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockTrustUserQueryModel(object):

    def __init__(self):
        self._trust_user_id = None

    @property
    def trust_user_id(self):
        return self._trust_user_id

    @trust_user_id.setter
    def trust_user_id(self, value):
        self._trust_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.trust_user_id:
            if hasattr(self.trust_user_id, 'to_alipay_dict'):
                params['trust_user_id'] = self.trust_user_id.to_alipay_dict()
            else:
                params['trust_user_id'] = self.trust_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockTrustUserQueryModel()
        if 'trust_user_id' in d:
            o.trust_user_id = d['trust_user_id']
        return o


