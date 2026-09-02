#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalQuotationQueryModel(object):

    def __init__(self):
        self._quotation_no_list = None

    @property
    def quotation_no_list(self):
        return self._quotation_no_list

    @quotation_no_list.setter
    def quotation_no_list(self, value):
        if isinstance(value, list):
            self._quotation_no_list = list()
            for i in value:
                self._quotation_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.quotation_no_list:
            if isinstance(self.quotation_no_list, list):
                for i in range(0, len(self.quotation_no_list)):
                    element = self.quotation_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quotation_no_list[i] = element.to_alipay_dict()
            if hasattr(self.quotation_no_list, 'to_alipay_dict'):
                params['quotation_no_list'] = self.quotation_no_list.to_alipay_dict()
            else:
                params['quotation_no_list'] = self.quotation_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalQuotationQueryModel()
        if 'quotation_no_list' in d:
            o.quotation_no_list = d['quotation_no_list']
        return o


