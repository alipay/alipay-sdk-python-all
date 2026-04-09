#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubPrizeResult import SubPrizeResult


class CombinePrizeResult(object):

    def __init__(self):
        self._activity_id = None
        self._activity_order_id = None
        self._combine_prize_status = None
        self._discount_type = None
        self._out_biz_no = None
        self._sub_prize_result_list = None
        self._total_amount = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_order_id(self):
        return self._activity_order_id

    @activity_order_id.setter
    def activity_order_id(self, value):
        self._activity_order_id = value
    @property
    def combine_prize_status(self):
        return self._combine_prize_status

    @combine_prize_status.setter
    def combine_prize_status(self, value):
        self._combine_prize_status = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sub_prize_result_list(self):
        return self._sub_prize_result_list

    @sub_prize_result_list.setter
    def sub_prize_result_list(self, value):
        if isinstance(value, list):
            self._sub_prize_result_list = list()
            for i in value:
                if isinstance(i, SubPrizeResult):
                    self._sub_prize_result_list.append(i)
                else:
                    self._sub_prize_result_list.append(SubPrizeResult.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_order_id:
            if hasattr(self.activity_order_id, 'to_alipay_dict'):
                params['activity_order_id'] = self.activity_order_id.to_alipay_dict()
            else:
                params['activity_order_id'] = self.activity_order_id
        if self.combine_prize_status:
            if hasattr(self.combine_prize_status, 'to_alipay_dict'):
                params['combine_prize_status'] = self.combine_prize_status.to_alipay_dict()
            else:
                params['combine_prize_status'] = self.combine_prize_status
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sub_prize_result_list:
            if isinstance(self.sub_prize_result_list, list):
                for i in range(0, len(self.sub_prize_result_list)):
                    element = self.sub_prize_result_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_prize_result_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_prize_result_list, 'to_alipay_dict'):
                params['sub_prize_result_list'] = self.sub_prize_result_list.to_alipay_dict()
            else:
                params['sub_prize_result_list'] = self.sub_prize_result_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CombinePrizeResult()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_order_id' in d:
            o.activity_order_id = d['activity_order_id']
        if 'combine_prize_status' in d:
            o.combine_prize_status = d['combine_prize_status']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sub_prize_result_list' in d:
            o.sub_prize_result_list = d['sub_prize_result_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


