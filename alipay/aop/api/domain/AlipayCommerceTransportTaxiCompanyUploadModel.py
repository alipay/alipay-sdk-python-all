#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompanyImportItem import CompanyImportItem


class AlipayCommerceTransportTaxiCompanyUploadModel(object):

    def __init__(self):
        self._company_list = None

    @property
    def company_list(self):
        return self._company_list

    @company_list.setter
    def company_list(self, value):
        if isinstance(value, list):
            self._company_list = list()
            for i in value:
                if isinstance(i, CompanyImportItem):
                    self._company_list.append(i)
                else:
                    self._company_list.append(CompanyImportItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.company_list:
            if isinstance(self.company_list, list):
                for i in range(0, len(self.company_list)):
                    element = self.company_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.company_list[i] = element.to_alipay_dict()
            if hasattr(self.company_list, 'to_alipay_dict'):
                params['company_list'] = self.company_list.to_alipay_dict()
            else:
                params['company_list'] = self.company_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiCompanyUploadModel()
        if 'company_list' in d:
            o.company_list = d['company_list']
        return o


