#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultItem import ConsultItem


class RcMedConsultResult(object):

    def __init__(self):
        self._item_list = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ConsultItem):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ConsultItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RcMedConsultResult()
        if 'item_list' in d:
            o.item_list = d['item_list']
        return o


