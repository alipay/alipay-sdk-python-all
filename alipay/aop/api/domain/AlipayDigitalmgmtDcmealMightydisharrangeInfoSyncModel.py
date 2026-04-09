#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DcmealDishArrangeDetail import DcmealDishArrangeDetail


class AlipayDigitalmgmtDcmealMightydisharrangeInfoSyncModel(object):

    def __init__(self):
        self._dish_arrange_list = None

    @property
    def dish_arrange_list(self):
        return self._dish_arrange_list

    @dish_arrange_list.setter
    def dish_arrange_list(self, value):
        if isinstance(value, list):
            self._dish_arrange_list = list()
            for i in value:
                if isinstance(i, DcmealDishArrangeDetail):
                    self._dish_arrange_list.append(i)
                else:
                    self._dish_arrange_list.append(DcmealDishArrangeDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.dish_arrange_list:
            if isinstance(self.dish_arrange_list, list):
                for i in range(0, len(self.dish_arrange_list)):
                    element = self.dish_arrange_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_arrange_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_arrange_list, 'to_alipay_dict'):
                params['dish_arrange_list'] = self.dish_arrange_list.to_alipay_dict()
            else:
                params['dish_arrange_list'] = self.dish_arrange_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtDcmealMightydisharrangeInfoSyncModel()
        if 'dish_arrange_list' in d:
            o.dish_arrange_list = d['dish_arrange_list']
        return o


