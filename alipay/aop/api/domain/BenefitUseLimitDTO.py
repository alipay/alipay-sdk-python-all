#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CashBackInfoDTO import CashBackInfoDTO
from alipay.aop.api.domain.DiscountInfoDTO import DiscountInfoDTO
from alipay.aop.api.domain.GiftInfoDTO import GiftInfoDTO
from alipay.aop.api.domain.ReduceByInfoDTO import ReduceByInfoDTO
from alipay.aop.api.domain.ReduceToInfoDTO import ReduceToInfoDTO


class BenefitUseLimitDTO(object):

    def __init__(self):
        self._benefit_content_type = None
        self._cash_back_info = None
        self._description = None
        self._discount_info = None
        self._gift_info = None
        self._reduce_by_info = None
        self._reducy_to_info = None

    @property
    def benefit_content_type(self):
        return self._benefit_content_type

    @benefit_content_type.setter
    def benefit_content_type(self, value):
        self._benefit_content_type = value
    @property
    def cash_back_info(self):
        return self._cash_back_info

    @cash_back_info.setter
    def cash_back_info(self, value):
        if isinstance(value, CashBackInfoDTO):
            self._cash_back_info = value
        else:
            self._cash_back_info = CashBackInfoDTO.from_alipay_dict(value)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_info(self):
        return self._discount_info

    @discount_info.setter
    def discount_info(self, value):
        if isinstance(value, DiscountInfoDTO):
            self._discount_info = value
        else:
            self._discount_info = DiscountInfoDTO.from_alipay_dict(value)
    @property
    def gift_info(self):
        return self._gift_info

    @gift_info.setter
    def gift_info(self, value):
        if isinstance(value, GiftInfoDTO):
            self._gift_info = value
        else:
            self._gift_info = GiftInfoDTO.from_alipay_dict(value)
    @property
    def reduce_by_info(self):
        return self._reduce_by_info

    @reduce_by_info.setter
    def reduce_by_info(self, value):
        if isinstance(value, ReduceByInfoDTO):
            self._reduce_by_info = value
        else:
            self._reduce_by_info = ReduceByInfoDTO.from_alipay_dict(value)
    @property
    def reducy_to_info(self):
        return self._reducy_to_info

    @reducy_to_info.setter
    def reducy_to_info(self, value):
        if isinstance(value, ReduceToInfoDTO):
            self._reducy_to_info = value
        else:
            self._reducy_to_info = ReduceToInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_content_type:
            if hasattr(self.benefit_content_type, 'to_alipay_dict'):
                params['benefit_content_type'] = self.benefit_content_type.to_alipay_dict()
            else:
                params['benefit_content_type'] = self.benefit_content_type
        if self.cash_back_info:
            if hasattr(self.cash_back_info, 'to_alipay_dict'):
                params['cash_back_info'] = self.cash_back_info.to_alipay_dict()
            else:
                params['cash_back_info'] = self.cash_back_info
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_info:
            if hasattr(self.discount_info, 'to_alipay_dict'):
                params['discount_info'] = self.discount_info.to_alipay_dict()
            else:
                params['discount_info'] = self.discount_info
        if self.gift_info:
            if hasattr(self.gift_info, 'to_alipay_dict'):
                params['gift_info'] = self.gift_info.to_alipay_dict()
            else:
                params['gift_info'] = self.gift_info
        if self.reduce_by_info:
            if hasattr(self.reduce_by_info, 'to_alipay_dict'):
                params['reduce_by_info'] = self.reduce_by_info.to_alipay_dict()
            else:
                params['reduce_by_info'] = self.reduce_by_info
        if self.reducy_to_info:
            if hasattr(self.reducy_to_info, 'to_alipay_dict'):
                params['reducy_to_info'] = self.reducy_to_info.to_alipay_dict()
            else:
                params['reducy_to_info'] = self.reducy_to_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitUseLimitDTO()
        if 'benefit_content_type' in d:
            o.benefit_content_type = d['benefit_content_type']
        if 'cash_back_info' in d:
            o.cash_back_info = d['cash_back_info']
        if 'description' in d:
            o.description = d['description']
        if 'discount_info' in d:
            o.discount_info = d['discount_info']
        if 'gift_info' in d:
            o.gift_info = d['gift_info']
        if 'reduce_by_info' in d:
            o.reduce_by_info = d['reduce_by_info']
        if 'reducy_to_info' in d:
            o.reducy_to_info = d['reducy_to_info']
        return o


