#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleRoyaltyInfo import RecycleRoyaltyInfo


class AlipayCommerceRecycleRoyaltyRelationModifyModel(object):

    def __init__(self):
        self._merchant_order_no = None
        self._open_id = None
        self._royalty_info_list = None
        self._user_id = None

    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def royalty_info_list(self):
        return self._royalty_info_list

    @royalty_info_list.setter
    def royalty_info_list(self, value):
        if isinstance(value, list):
            self._royalty_info_list = list()
            for i in value:
                if isinstance(i, RecycleRoyaltyInfo):
                    self._royalty_info_list.append(i)
                else:
                    self._royalty_info_list.append(RecycleRoyaltyInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.royalty_info_list:
            if isinstance(self.royalty_info_list, list):
                for i in range(0, len(self.royalty_info_list)):
                    element = self.royalty_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_info_list[i] = element.to_alipay_dict()
            if hasattr(self.royalty_info_list, 'to_alipay_dict'):
                params['royalty_info_list'] = self.royalty_info_list.to_alipay_dict()
            else:
                params['royalty_info_list'] = self.royalty_info_list
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
        o = AlipayCommerceRecycleRoyaltyRelationModifyModel()
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'royalty_info_list' in d:
            o.royalty_info_list = d['royalty_info_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


