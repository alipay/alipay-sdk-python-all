#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallMergeCartRequestDto import MallMergeCartRequestDto


class AlipayDigitalmgmtPunchoutBasketCreateModel(object):

    def __init__(self):
        self._param_mall_merge_cart_request_dto = None

    @property
    def param_mall_merge_cart_request_dto(self):
        return self._param_mall_merge_cart_request_dto

    @param_mall_merge_cart_request_dto.setter
    def param_mall_merge_cart_request_dto(self, value):
        if isinstance(value, MallMergeCartRequestDto):
            self._param_mall_merge_cart_request_dto = value
        else:
            self._param_mall_merge_cart_request_dto = MallMergeCartRequestDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.param_mall_merge_cart_request_dto:
            if hasattr(self.param_mall_merge_cart_request_dto, 'to_alipay_dict'):
                params['param_mall_merge_cart_request_dto'] = self.param_mall_merge_cart_request_dto.to_alipay_dict()
            else:
                params['param_mall_merge_cart_request_dto'] = self.param_mall_merge_cart_request_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtPunchoutBasketCreateModel()
        if 'param_mall_merge_cart_request_dto' in d:
            o.param_mall_merge_cart_request_dto = d['param_mall_merge_cart_request_dto']
        return o


