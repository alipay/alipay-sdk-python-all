#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityLimitationDTO import ActivityLimitationDTO
from alipay.aop.api.domain.FullDiscountDTO import FullDiscountDTO
from alipay.aop.api.domain.FullGiftDTO import FullGiftDTO
from alipay.aop.api.domain.FullReductionDTO import FullReductionDTO
from alipay.aop.api.domain.RechargeDTO import RechargeDTO
from alipay.aop.api.domain.SpecialPriceDTO import SpecialPriceDTO


class KmsBakingPromotionDTO(object):

    def __init__(self):
        self._activity_limitation = None
        self._available_date = None
        self._available_end_time = None
        self._available_start_time = None
        self._data_id = None
        self._description = None
        self._end_time = None
        self._exclusive = None
        self._full_discount = None
        self._full_gift = None
        self._full_reduction = None
        self._member_promotion = None
        self._operation_name = None
        self._operation_time = None
        self._promotion_channel = None
        self._promotion_id = None
        self._promotion_name = None
        self._promotion_scope = None
        self._promotion_type = None
        self._recharge = None
        self._special_price = None
        self._start_time = None

    @property
    def activity_limitation(self):
        return self._activity_limitation

    @activity_limitation.setter
    def activity_limitation(self, value):
        if isinstance(value, ActivityLimitationDTO):
            self._activity_limitation = value
        else:
            self._activity_limitation = ActivityLimitationDTO.from_alipay_dict(value)
    @property
    def available_date(self):
        return self._available_date

    @available_date.setter
    def available_date(self, value):
        self._available_date = value
    @property
    def available_end_time(self):
        return self._available_end_time

    @available_end_time.setter
    def available_end_time(self, value):
        self._available_end_time = value
    @property
    def available_start_time(self):
        return self._available_start_time

    @available_start_time.setter
    def available_start_time(self, value):
        self._available_start_time = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exclusive(self):
        return self._exclusive

    @exclusive.setter
    def exclusive(self, value):
        self._exclusive = value
    @property
    def full_discount(self):
        return self._full_discount

    @full_discount.setter
    def full_discount(self, value):
        if isinstance(value, FullDiscountDTO):
            self._full_discount = value
        else:
            self._full_discount = FullDiscountDTO.from_alipay_dict(value)
    @property
    def full_gift(self):
        return self._full_gift

    @full_gift.setter
    def full_gift(self, value):
        if isinstance(value, FullGiftDTO):
            self._full_gift = value
        else:
            self._full_gift = FullGiftDTO.from_alipay_dict(value)
    @property
    def full_reduction(self):
        return self._full_reduction

    @full_reduction.setter
    def full_reduction(self, value):
        if isinstance(value, FullReductionDTO):
            self._full_reduction = value
        else:
            self._full_reduction = FullReductionDTO.from_alipay_dict(value)
    @property
    def member_promotion(self):
        return self._member_promotion

    @member_promotion.setter
    def member_promotion(self, value):
        self._member_promotion = value
    @property
    def operation_name(self):
        return self._operation_name

    @operation_name.setter
    def operation_name(self, value):
        self._operation_name = value
    @property
    def operation_time(self):
        return self._operation_time

    @operation_time.setter
    def operation_time(self, value):
        self._operation_time = value
    @property
    def promotion_channel(self):
        return self._promotion_channel

    @promotion_channel.setter
    def promotion_channel(self, value):
        self._promotion_channel = value
    @property
    def promotion_id(self):
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, value):
        self._promotion_id = value
    @property
    def promotion_name(self):
        return self._promotion_name

    @promotion_name.setter
    def promotion_name(self, value):
        self._promotion_name = value
    @property
    def promotion_scope(self):
        return self._promotion_scope

    @promotion_scope.setter
    def promotion_scope(self, value):
        self._promotion_scope = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def recharge(self):
        return self._recharge

    @recharge.setter
    def recharge(self, value):
        if isinstance(value, RechargeDTO):
            self._recharge = value
        else:
            self._recharge = RechargeDTO.from_alipay_dict(value)
    @property
    def special_price(self):
        return self._special_price

    @special_price.setter
    def special_price(self, value):
        if isinstance(value, SpecialPriceDTO):
            self._special_price = value
        else:
            self._special_price = SpecialPriceDTO.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_limitation:
            if hasattr(self.activity_limitation, 'to_alipay_dict'):
                params['activity_limitation'] = self.activity_limitation.to_alipay_dict()
            else:
                params['activity_limitation'] = self.activity_limitation
        if self.available_date:
            if hasattr(self.available_date, 'to_alipay_dict'):
                params['available_date'] = self.available_date.to_alipay_dict()
            else:
                params['available_date'] = self.available_date
        if self.available_end_time:
            if hasattr(self.available_end_time, 'to_alipay_dict'):
                params['available_end_time'] = self.available_end_time.to_alipay_dict()
            else:
                params['available_end_time'] = self.available_end_time
        if self.available_start_time:
            if hasattr(self.available_start_time, 'to_alipay_dict'):
                params['available_start_time'] = self.available_start_time.to_alipay_dict()
            else:
                params['available_start_time'] = self.available_start_time
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.exclusive:
            if hasattr(self.exclusive, 'to_alipay_dict'):
                params['exclusive'] = self.exclusive.to_alipay_dict()
            else:
                params['exclusive'] = self.exclusive
        if self.full_discount:
            if hasattr(self.full_discount, 'to_alipay_dict'):
                params['full_discount'] = self.full_discount.to_alipay_dict()
            else:
                params['full_discount'] = self.full_discount
        if self.full_gift:
            if hasattr(self.full_gift, 'to_alipay_dict'):
                params['full_gift'] = self.full_gift.to_alipay_dict()
            else:
                params['full_gift'] = self.full_gift
        if self.full_reduction:
            if hasattr(self.full_reduction, 'to_alipay_dict'):
                params['full_reduction'] = self.full_reduction.to_alipay_dict()
            else:
                params['full_reduction'] = self.full_reduction
        if self.member_promotion:
            if hasattr(self.member_promotion, 'to_alipay_dict'):
                params['member_promotion'] = self.member_promotion.to_alipay_dict()
            else:
                params['member_promotion'] = self.member_promotion
        if self.operation_name:
            if hasattr(self.operation_name, 'to_alipay_dict'):
                params['operation_name'] = self.operation_name.to_alipay_dict()
            else:
                params['operation_name'] = self.operation_name
        if self.operation_time:
            if hasattr(self.operation_time, 'to_alipay_dict'):
                params['operation_time'] = self.operation_time.to_alipay_dict()
            else:
                params['operation_time'] = self.operation_time
        if self.promotion_channel:
            if hasattr(self.promotion_channel, 'to_alipay_dict'):
                params['promotion_channel'] = self.promotion_channel.to_alipay_dict()
            else:
                params['promotion_channel'] = self.promotion_channel
        if self.promotion_id:
            if hasattr(self.promotion_id, 'to_alipay_dict'):
                params['promotion_id'] = self.promotion_id.to_alipay_dict()
            else:
                params['promotion_id'] = self.promotion_id
        if self.promotion_name:
            if hasattr(self.promotion_name, 'to_alipay_dict'):
                params['promotion_name'] = self.promotion_name.to_alipay_dict()
            else:
                params['promotion_name'] = self.promotion_name
        if self.promotion_scope:
            if hasattr(self.promotion_scope, 'to_alipay_dict'):
                params['promotion_scope'] = self.promotion_scope.to_alipay_dict()
            else:
                params['promotion_scope'] = self.promotion_scope
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        if self.recharge:
            if hasattr(self.recharge, 'to_alipay_dict'):
                params['recharge'] = self.recharge.to_alipay_dict()
            else:
                params['recharge'] = self.recharge
        if self.special_price:
            if hasattr(self.special_price, 'to_alipay_dict'):
                params['special_price'] = self.special_price.to_alipay_dict()
            else:
                params['special_price'] = self.special_price
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KmsBakingPromotionDTO()
        if 'activity_limitation' in d:
            o.activity_limitation = d['activity_limitation']
        if 'available_date' in d:
            o.available_date = d['available_date']
        if 'available_end_time' in d:
            o.available_end_time = d['available_end_time']
        if 'available_start_time' in d:
            o.available_start_time = d['available_start_time']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'description' in d:
            o.description = d['description']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exclusive' in d:
            o.exclusive = d['exclusive']
        if 'full_discount' in d:
            o.full_discount = d['full_discount']
        if 'full_gift' in d:
            o.full_gift = d['full_gift']
        if 'full_reduction' in d:
            o.full_reduction = d['full_reduction']
        if 'member_promotion' in d:
            o.member_promotion = d['member_promotion']
        if 'operation_name' in d:
            o.operation_name = d['operation_name']
        if 'operation_time' in d:
            o.operation_time = d['operation_time']
        if 'promotion_channel' in d:
            o.promotion_channel = d['promotion_channel']
        if 'promotion_id' in d:
            o.promotion_id = d['promotion_id']
        if 'promotion_name' in d:
            o.promotion_name = d['promotion_name']
        if 'promotion_scope' in d:
            o.promotion_scope = d['promotion_scope']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        if 'recharge' in d:
            o.recharge = d['recharge']
        if 'special_price' in d:
            o.special_price = d['special_price']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


