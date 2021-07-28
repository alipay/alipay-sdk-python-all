#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendGoods(object):

    def __init__(self):
        self._barcode = None
        self._goods_code = None
        self._rank = None
        self._recommend_channels_count = None
        self._recommend_goods_count = None
        self._recommend_reason = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
    @property
    def recommend_channels_count(self):
        return self._recommend_channels_count

    @recommend_channels_count.setter
    def recommend_channels_count(self, value):
        self._recommend_channels_count = value
    @property
    def recommend_goods_count(self):
        return self._recommend_goods_count

    @recommend_goods_count.setter
    def recommend_goods_count(self, value):
        self._recommend_goods_count = value
    @property
    def recommend_reason(self):
        return self._recommend_reason

    @recommend_reason.setter
    def recommend_reason(self, value):
        self._recommend_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.rank:
            if hasattr(self.rank, 'to_alipay_dict'):
                params['rank'] = self.rank.to_alipay_dict()
            else:
                params['rank'] = self.rank
        if self.recommend_channels_count:
            if hasattr(self.recommend_channels_count, 'to_alipay_dict'):
                params['recommend_channels_count'] = self.recommend_channels_count.to_alipay_dict()
            else:
                params['recommend_channels_count'] = self.recommend_channels_count
        if self.recommend_goods_count:
            if hasattr(self.recommend_goods_count, 'to_alipay_dict'):
                params['recommend_goods_count'] = self.recommend_goods_count.to_alipay_dict()
            else:
                params['recommend_goods_count'] = self.recommend_goods_count
        if self.recommend_reason:
            if hasattr(self.recommend_reason, 'to_alipay_dict'):
                params['recommend_reason'] = self.recommend_reason.to_alipay_dict()
            else:
                params['recommend_reason'] = self.recommend_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendGoods()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'rank' in d:
            o.rank = d['rank']
        if 'recommend_channels_count' in d:
            o.recommend_channels_count = d['recommend_channels_count']
        if 'recommend_goods_count' in d:
            o.recommend_goods_count = d['recommend_goods_count']
        if 'recommend_reason' in d:
            o.recommend_reason = d['recommend_reason']
        return o


