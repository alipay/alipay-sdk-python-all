#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAeprepayContractQueryModel(object):

    def __init__(self):
        self._seller_login_id = None

    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayContractQueryModel()
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        return o


