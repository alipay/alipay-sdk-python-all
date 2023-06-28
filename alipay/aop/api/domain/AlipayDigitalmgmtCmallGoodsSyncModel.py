#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessGoodsDto import AccessGoodsDto
from alipay.aop.api.domain.AccessProductDto import AccessProductDto


class AlipayDigitalmgmtCmallGoodsSyncModel(object):

    def __init__(self):
        self._access_goods_dto = None
        self._access_product_dto = None

    @property
    def access_goods_dto(self):
        return self._access_goods_dto

    @access_goods_dto.setter
    def access_goods_dto(self, value):
        if isinstance(value, AccessGoodsDto):
            self._access_goods_dto = value
        else:
            self._access_goods_dto = AccessGoodsDto.from_alipay_dict(value)
    @property
    def access_product_dto(self):
        return self._access_product_dto

    @access_product_dto.setter
    def access_product_dto(self, value):
        if isinstance(value, AccessProductDto):
            self._access_product_dto = value
        else:
            self._access_product_dto = AccessProductDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.access_goods_dto:
            if hasattr(self.access_goods_dto, 'to_alipay_dict'):
                params['access_goods_dto'] = self.access_goods_dto.to_alipay_dict()
            else:
                params['access_goods_dto'] = self.access_goods_dto
        if self.access_product_dto:
            if hasattr(self.access_product_dto, 'to_alipay_dict'):
                params['access_product_dto'] = self.access_product_dto.to_alipay_dict()
            else:
                params['access_product_dto'] = self.access_product_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtCmallGoodsSyncModel()
        if 'access_goods_dto' in d:
            o.access_goods_dto = d['access_goods_dto']
        if 'access_product_dto' in d:
            o.access_product_dto = d['access_product_dto']
        return o


