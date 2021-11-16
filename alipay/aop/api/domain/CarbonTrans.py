#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarbonTranDetail import CarbonTranDetail


class CarbonTrans(object):

    def __init__(self):
        self._carbon_value = None
        self._detail_list = None
        self._trans_date = None

    @property
    def carbon_value(self):
        return self._carbon_value

    @carbon_value.setter
    def carbon_value(self, value):
        self._carbon_value = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, CarbonTranDetail):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(CarbonTranDetail.from_alipay_dict(i))
    @property
    def trans_date(self):
        return self._trans_date

    @trans_date.setter
    def trans_date(self, value):
        self._trans_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.carbon_value:
            if hasattr(self.carbon_value, 'to_alipay_dict'):
                params['carbon_value'] = self.carbon_value.to_alipay_dict()
            else:
                params['carbon_value'] = self.carbon_value
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.trans_date:
            if hasattr(self.trans_date, 'to_alipay_dict'):
                params['trans_date'] = self.trans_date.to_alipay_dict()
            else:
                params['trans_date'] = self.trans_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarbonTrans()
        if 'carbon_value' in d:
            o.carbon_value = d['carbon_value']
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'trans_date' in d:
            o.trans_date = d['trans_date']
        return o


