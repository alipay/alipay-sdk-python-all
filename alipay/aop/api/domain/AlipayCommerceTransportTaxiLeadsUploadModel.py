#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LeadsImportItem import LeadsImportItem


class AlipayCommerceTransportTaxiLeadsUploadModel(object):

    def __init__(self):
        self._leads_list = None

    @property
    def leads_list(self):
        return self._leads_list

    @leads_list.setter
    def leads_list(self, value):
        if isinstance(value, list):
            self._leads_list = list()
            for i in value:
                if isinstance(i, LeadsImportItem):
                    self._leads_list.append(i)
                else:
                    self._leads_list.append(LeadsImportItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.leads_list:
            if isinstance(self.leads_list, list):
                for i in range(0, len(self.leads_list)):
                    element = self.leads_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leads_list[i] = element.to_alipay_dict()
            if hasattr(self.leads_list, 'to_alipay_dict'):
                params['leads_list'] = self.leads_list.to_alipay_dict()
            else:
                params['leads_list'] = self.leads_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiLeadsUploadModel()
        if 'leads_list' in d:
            o.leads_list = d['leads_list']
        return o


