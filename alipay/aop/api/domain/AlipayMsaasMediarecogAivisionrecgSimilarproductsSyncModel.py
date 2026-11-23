#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionrecgSimilarproductsSyncModel(object):

    def __init__(self):
        self._isv_id = None
        self._merchant_id = None
        self._similar_goods_group_file_url = None

    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def similar_goods_group_file_url(self):
        return self._similar_goods_group_file_url

    @similar_goods_group_file_url.setter
    def similar_goods_group_file_url(self, value):
        self._similar_goods_group_file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.similar_goods_group_file_url:
            if hasattr(self.similar_goods_group_file_url, 'to_alipay_dict'):
                params['similar_goods_group_file_url'] = self.similar_goods_group_file_url.to_alipay_dict()
            else:
                params['similar_goods_group_file_url'] = self.similar_goods_group_file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionrecgSimilarproductsSyncModel()
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'similar_goods_group_file_url' in d:
            o.similar_goods_group_file_url = d['similar_goods_group_file_url']
        return o


