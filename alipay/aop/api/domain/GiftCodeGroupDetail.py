#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GiftCodeDetail import GiftCodeDetail


class GiftCodeGroupDetail(object):

    def __init__(self):
        self._gift_code_detail_list = None
        self._id = None

    @property
    def gift_code_detail_list(self):
        return self._gift_code_detail_list

    @gift_code_detail_list.setter
    def gift_code_detail_list(self, value):
        if isinstance(value, list):
            self._gift_code_detail_list = list()
            for i in value:
                if isinstance(i, GiftCodeDetail):
                    self._gift_code_detail_list.append(i)
                else:
                    self._gift_code_detail_list.append(GiftCodeDetail.from_alipay_dict(i))
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gift_code_detail_list:
            if isinstance(self.gift_code_detail_list, list):
                for i in range(0, len(self.gift_code_detail_list)):
                    element = self.gift_code_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gift_code_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.gift_code_detail_list, 'to_alipay_dict'):
                params['gift_code_detail_list'] = self.gift_code_detail_list.to_alipay_dict()
            else:
                params['gift_code_detail_list'] = self.gift_code_detail_list
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftCodeGroupDetail()
        if 'gift_code_detail_list' in d:
            o.gift_code_detail_list = d['gift_code_detail_list']
        if 'id' in d:
            o.id = d['id']
        return o


