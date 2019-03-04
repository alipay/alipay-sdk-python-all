#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentPrizeInfoModel import ContentPrizeInfoModel


class ContentExtInfoModel(object):

    def __init__(self):
        self._prize_info_list = None

    @property
    def prize_info_list(self):
        return self._prize_info_list

    @prize_info_list.setter
    def prize_info_list(self, value):
        if isinstance(value, list):
            self._prize_info_list = list()
            for i in value:
                if isinstance(i, ContentPrizeInfoModel):
                    self._prize_info_list.append(i)
                else:
                    self._prize_info_list.append(ContentPrizeInfoModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.prize_info_list:
            if isinstance(self.prize_info_list, list):
                for i in range(0, len(self.prize_info_list)):
                    element = self.prize_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_info_list[i] = element.to_alipay_dict()
            if hasattr(self.prize_info_list, 'to_alipay_dict'):
                params['prize_info_list'] = self.prize_info_list.to_alipay_dict()
            else:
                params['prize_info_list'] = self.prize_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentExtInfoModel()
        if 'prize_info_list' in d:
            o.prize_info_list = d['prize_info_list']
        return o


