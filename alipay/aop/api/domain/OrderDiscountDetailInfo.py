#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoItemConsultDetailInfo import PromoItemConsultDetailInfo
from alipay.aop.api.domain.PromoSumInfo import PromoSumInfo


class OrderDiscountDetailInfo(object):

    def __init__(self):
        self._activity_consult_id = None
        self._item_consult_detail_info_list = None
        self._promo_amount_info_list = None

    @property
    def activity_consult_id(self):
        return self._activity_consult_id

    @activity_consult_id.setter
    def activity_consult_id(self, value):
        self._activity_consult_id = value
    @property
    def item_consult_detail_info_list(self):
        return self._item_consult_detail_info_list

    @item_consult_detail_info_list.setter
    def item_consult_detail_info_list(self, value):
        if isinstance(value, list):
            self._item_consult_detail_info_list = list()
            for i in value:
                if isinstance(i, PromoItemConsultDetailInfo):
                    self._item_consult_detail_info_list.append(i)
                else:
                    self._item_consult_detail_info_list.append(PromoItemConsultDetailInfo.from_alipay_dict(i))
    @property
    def promo_amount_info_list(self):
        return self._promo_amount_info_list

    @promo_amount_info_list.setter
    def promo_amount_info_list(self, value):
        if isinstance(value, list):
            self._promo_amount_info_list = list()
            for i in value:
                if isinstance(i, PromoSumInfo):
                    self._promo_amount_info_list.append(i)
                else:
                    self._promo_amount_info_list.append(PromoSumInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activity_consult_id:
            if hasattr(self.activity_consult_id, 'to_alipay_dict'):
                params['activity_consult_id'] = self.activity_consult_id.to_alipay_dict()
            else:
                params['activity_consult_id'] = self.activity_consult_id
        if self.item_consult_detail_info_list:
            if isinstance(self.item_consult_detail_info_list, list):
                for i in range(0, len(self.item_consult_detail_info_list)):
                    element = self.item_consult_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_consult_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.item_consult_detail_info_list, 'to_alipay_dict'):
                params['item_consult_detail_info_list'] = self.item_consult_detail_info_list.to_alipay_dict()
            else:
                params['item_consult_detail_info_list'] = self.item_consult_detail_info_list
        if self.promo_amount_info_list:
            if isinstance(self.promo_amount_info_list, list):
                for i in range(0, len(self.promo_amount_info_list)):
                    element = self.promo_amount_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_amount_info_list[i] = element.to_alipay_dict()
            if hasattr(self.promo_amount_info_list, 'to_alipay_dict'):
                params['promo_amount_info_list'] = self.promo_amount_info_list.to_alipay_dict()
            else:
                params['promo_amount_info_list'] = self.promo_amount_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDiscountDetailInfo()
        if 'activity_consult_id' in d:
            o.activity_consult_id = d['activity_consult_id']
        if 'item_consult_detail_info_list' in d:
            o.item_consult_detail_info_list = d['item_consult_detail_info_list']
        if 'promo_amount_info_list' in d:
            o.promo_amount_info_list = d['promo_amount_info_list']
        return o


