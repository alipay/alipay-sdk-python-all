#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIOuterTaxInfoDetail import GFAOpenAPIOuterTaxInfoDetail


class GFAOpenAPIOuterTaxInfo(object):

    def __init__(self):
        self._tax_info_detail_list = None

    @property
    def tax_info_detail_list(self):
        return self._tax_info_detail_list

    @tax_info_detail_list.setter
    def tax_info_detail_list(self, value):
        if isinstance(value, list):
            self._tax_info_detail_list = list()
            for i in value:
                if isinstance(i, GFAOpenAPIOuterTaxInfoDetail):
                    self._tax_info_detail_list.append(i)
                else:
                    self._tax_info_detail_list.append(GFAOpenAPIOuterTaxInfoDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tax_info_detail_list:
            if isinstance(self.tax_info_detail_list, list):
                for i in range(0, len(self.tax_info_detail_list)):
                    element = self.tax_info_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tax_info_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.tax_info_detail_list, 'to_alipay_dict'):
                params['tax_info_detail_list'] = self.tax_info_detail_list.to_alipay_dict()
            else:
                params['tax_info_detail_list'] = self.tax_info_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIOuterTaxInfo()
        if 'tax_info_detail_list' in d:
            o.tax_info_detail_list = d['tax_info_detail_list']
        return o


