#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishCookCateTopInfo import KbdishCookCateTopInfo


class KoubeiCateringDishCookcatetopSyncModel(object):

    def __init__(self):
        self._kbdish_cook_cate_top_info_list = None

    @property
    def kbdish_cook_cate_top_info_list(self):
        return self._kbdish_cook_cate_top_info_list

    @kbdish_cook_cate_top_info_list.setter
    def kbdish_cook_cate_top_info_list(self, value):
        if isinstance(value, list):
            self._kbdish_cook_cate_top_info_list = list()
            for i in value:
                if isinstance(i, KbdishCookCateTopInfo):
                    self._kbdish_cook_cate_top_info_list.append(i)
                else:
                    self._kbdish_cook_cate_top_info_list.append(KbdishCookCateTopInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.kbdish_cook_cate_top_info_list:
            if isinstance(self.kbdish_cook_cate_top_info_list, list):
                for i in range(0, len(self.kbdish_cook_cate_top_info_list)):
                    element = self.kbdish_cook_cate_top_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kbdish_cook_cate_top_info_list[i] = element.to_alipay_dict()
            if hasattr(self.kbdish_cook_cate_top_info_list, 'to_alipay_dict'):
                params['kbdish_cook_cate_top_info_list'] = self.kbdish_cook_cate_top_info_list.to_alipay_dict()
            else:
                params['kbdish_cook_cate_top_info_list'] = self.kbdish_cook_cate_top_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCookcatetopSyncModel()
        if 'kbdish_cook_cate_top_info_list' in d:
            o.kbdish_cook_cate_top_info_list = d['kbdish_cook_cate_top_info_list']
        return o


