#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivitySubsidyModel import ActivitySubsidyModel
from alipay.aop.api.domain.InstallmentIntDiscountModel import InstallmentIntDiscountModel
from alipay.aop.api.domain.ResultMessage import ResultMessage
from alipay.aop.api.domain.VoucherSubsidyModel import VoucherSubsidyModel


class SubsidySimpleResponse(object):

    def __init__(self):
        self._activity_subsidy_list = None
        self._good_item_id = None
        self._installment_biz_info = None
        self._installment_int_discount_info = None
        self._out_order_no = None
        self._result_message = None
        self._trade_no = None
        self._user_id = None
        self._voucher_subsidy_list = None

    @property
    def activity_subsidy_list(self):
        return self._activity_subsidy_list

    @activity_subsidy_list.setter
    def activity_subsidy_list(self, value):
        if isinstance(value, list):
            self._activity_subsidy_list = list()
            for i in value:
                if isinstance(i, ActivitySubsidyModel):
                    self._activity_subsidy_list.append(i)
                else:
                    self._activity_subsidy_list.append(ActivitySubsidyModel.from_alipay_dict(i))
    @property
    def good_item_id(self):
        return self._good_item_id

    @good_item_id.setter
    def good_item_id(self, value):
        self._good_item_id = value
    @property
    def installment_biz_info(self):
        return self._installment_biz_info

    @installment_biz_info.setter
    def installment_biz_info(self, value):
        self._installment_biz_info = value
    @property
    def installment_int_discount_info(self):
        return self._installment_int_discount_info

    @installment_int_discount_info.setter
    def installment_int_discount_info(self, value):
        if isinstance(value, list):
            self._installment_int_discount_info = list()
            for i in value:
                if isinstance(i, InstallmentIntDiscountModel):
                    self._installment_int_discount_info.append(i)
                else:
                    self._installment_int_discount_info.append(InstallmentIntDiscountModel.from_alipay_dict(i))
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        if isinstance(value, ResultMessage):
            self._result_message = value
        else:
            self._result_message = ResultMessage.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def voucher_subsidy_list(self):
        return self._voucher_subsidy_list

    @voucher_subsidy_list.setter
    def voucher_subsidy_list(self, value):
        if isinstance(value, list):
            self._voucher_subsidy_list = list()
            for i in value:
                if isinstance(i, VoucherSubsidyModel):
                    self._voucher_subsidy_list.append(i)
                else:
                    self._voucher_subsidy_list.append(VoucherSubsidyModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_subsidy_list:
            if isinstance(self.activity_subsidy_list, list):
                for i in range(0, len(self.activity_subsidy_list)):
                    element = self.activity_subsidy_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_subsidy_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_subsidy_list, 'to_alipay_dict'):
                params['activity_subsidy_list'] = self.activity_subsidy_list.to_alipay_dict()
            else:
                params['activity_subsidy_list'] = self.activity_subsidy_list
        if self.good_item_id:
            if hasattr(self.good_item_id, 'to_alipay_dict'):
                params['good_item_id'] = self.good_item_id.to_alipay_dict()
            else:
                params['good_item_id'] = self.good_item_id
        if self.installment_biz_info:
            if hasattr(self.installment_biz_info, 'to_alipay_dict'):
                params['installment_biz_info'] = self.installment_biz_info.to_alipay_dict()
            else:
                params['installment_biz_info'] = self.installment_biz_info
        if self.installment_int_discount_info:
            if isinstance(self.installment_int_discount_info, list):
                for i in range(0, len(self.installment_int_discount_info)):
                    element = self.installment_int_discount_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_int_discount_info[i] = element.to_alipay_dict()
            if hasattr(self.installment_int_discount_info, 'to_alipay_dict'):
                params['installment_int_discount_info'] = self.installment_int_discount_info.to_alipay_dict()
            else:
                params['installment_int_discount_info'] = self.installment_int_discount_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.result_message:
            if hasattr(self.result_message, 'to_alipay_dict'):
                params['result_message'] = self.result_message.to_alipay_dict()
            else:
                params['result_message'] = self.result_message
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.voucher_subsidy_list:
            if isinstance(self.voucher_subsidy_list, list):
                for i in range(0, len(self.voucher_subsidy_list)):
                    element = self.voucher_subsidy_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_subsidy_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_subsidy_list, 'to_alipay_dict'):
                params['voucher_subsidy_list'] = self.voucher_subsidy_list.to_alipay_dict()
            else:
                params['voucher_subsidy_list'] = self.voucher_subsidy_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubsidySimpleResponse()
        if 'activity_subsidy_list' in d:
            o.activity_subsidy_list = d['activity_subsidy_list']
        if 'good_item_id' in d:
            o.good_item_id = d['good_item_id']
        if 'installment_biz_info' in d:
            o.installment_biz_info = d['installment_biz_info']
        if 'installment_int_discount_info' in d:
            o.installment_int_discount_info = d['installment_int_discount_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'result_message' in d:
            o.result_message = d['result_message']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'voucher_subsidy_list' in d:
            o.voucher_subsidy_list = d['voucher_subsidy_list']
        return o


