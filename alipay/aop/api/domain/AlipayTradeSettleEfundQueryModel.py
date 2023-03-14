#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSettleEfundQueryModel(object):

    def __init__(self):
        self._seller_open_id = None
        self._seller_user_id = None
        self._settle_biz_type = None

    @property
    def seller_open_id(self):
        return self._seller_open_id

    @seller_open_id.setter
    def seller_open_id(self, value):
        self._seller_open_id = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def settle_biz_type(self):
        return self._settle_biz_type

    @settle_biz_type.setter
    def settle_biz_type(self, value):
        self._settle_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.seller_open_id:
            if hasattr(self.seller_open_id, 'to_alipay_dict'):
                params['seller_open_id'] = self.seller_open_id.to_alipay_dict()
            else:
                params['seller_open_id'] = self.seller_open_id
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.settle_biz_type:
            if hasattr(self.settle_biz_type, 'to_alipay_dict'):
                params['settle_biz_type'] = self.settle_biz_type.to_alipay_dict()
            else:
                params['settle_biz_type'] = self.settle_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSettleEfundQueryModel()
        if 'seller_open_id' in d:
            o.seller_open_id = d['seller_open_id']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'settle_biz_type' in d:
            o.settle_biz_type = d['settle_biz_type']
        return o


