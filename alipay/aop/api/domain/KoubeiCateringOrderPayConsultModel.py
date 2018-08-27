#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbPosOrderDishDetail import KbPosOrderDishDetail


class KoubeiCateringOrderPayConsultModel(object):

    def __init__(self):
        self._apdid_token = None
        self._dish_details = None
        self._member_flag = None
        self._other_amount = None
        self._packing_amount = None
        self._request_id = None
        self._service_amount = None
        self._shop_id = None
        self._total_amount = None
        self._user_id = None

    @property
    def apdid_token(self):
        return self._apdid_token

    @apdid_token.setter
    def apdid_token(self, value):
        self._apdid_token = value
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, KbPosOrderDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(KbPosOrderDishDetail.from_alipay_dict(i))
    @property
    def member_flag(self):
        return self._member_flag

    @member_flag.setter
    def member_flag(self, value):
        self._member_flag = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def packing_amount(self):
        return self._packing_amount

    @packing_amount.setter
    def packing_amount(self, value):
        self._packing_amount = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apdid_token:
            if hasattr(self.apdid_token, 'to_alipay_dict'):
                params['apdid_token'] = self.apdid_token.to_alipay_dict()
            else:
                params['apdid_token'] = self.apdid_token
        if self.dish_details:
            if isinstance(self.dish_details, list):
                for i in range(0, len(self.dish_details)):
                    element = self.dish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_details[i] = element.to_alipay_dict()
            if hasattr(self.dish_details, 'to_alipay_dict'):
                params['dish_details'] = self.dish_details.to_alipay_dict()
            else:
                params['dish_details'] = self.dish_details
        if self.member_flag:
            if hasattr(self.member_flag, 'to_alipay_dict'):
                params['member_flag'] = self.member_flag.to_alipay_dict()
            else:
                params['member_flag'] = self.member_flag
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.packing_amount:
            if hasattr(self.packing_amount, 'to_alipay_dict'):
                params['packing_amount'] = self.packing_amount.to_alipay_dict()
            else:
                params['packing_amount'] = self.packing_amount
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderPayConsultModel()
        if 'apdid_token' in d:
            o.apdid_token = d['apdid_token']
        if 'dish_details' in d:
            o.dish_details = d['dish_details']
        if 'member_flag' in d:
            o.member_flag = d['member_flag']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'packing_amount' in d:
            o.packing_amount = d['packing_amount']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


