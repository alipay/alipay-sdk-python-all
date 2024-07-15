#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoItemConsultDetailInfo import PromoItemConsultDetailInfo


class ItemDiscountDetailInfo(object):

    def __init__(self):
        self._buy_restrict = None
        self._consult_detail_info_list = None

    @property
    def buy_restrict(self):
        return self._buy_restrict

    @buy_restrict.setter
    def buy_restrict(self, value):
        self._buy_restrict = value
    @property
    def consult_detail_info_list(self):
        return self._consult_detail_info_list

    @consult_detail_info_list.setter
    def consult_detail_info_list(self, value):
        if isinstance(value, list):
            self._consult_detail_info_list = list()
            for i in value:
                if isinstance(i, PromoItemConsultDetailInfo):
                    self._consult_detail_info_list.append(i)
                else:
                    self._consult_detail_info_list.append(PromoItemConsultDetailInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.buy_restrict:
            if hasattr(self.buy_restrict, 'to_alipay_dict'):
                params['buy_restrict'] = self.buy_restrict.to_alipay_dict()
            else:
                params['buy_restrict'] = self.buy_restrict
        if self.consult_detail_info_list:
            if isinstance(self.consult_detail_info_list, list):
                for i in range(0, len(self.consult_detail_info_list)):
                    element = self.consult_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consult_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.consult_detail_info_list, 'to_alipay_dict'):
                params['consult_detail_info_list'] = self.consult_detail_info_list.to_alipay_dict()
            else:
                params['consult_detail_info_list'] = self.consult_detail_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDiscountDetailInfo()
        if 'buy_restrict' in d:
            o.buy_restrict = d['buy_restrict']
        if 'consult_detail_info_list' in d:
            o.consult_detail_info_list = d['consult_detail_info_list']
        return o


