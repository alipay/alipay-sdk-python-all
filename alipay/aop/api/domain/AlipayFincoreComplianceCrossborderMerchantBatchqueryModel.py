#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BaseCrossborderMerchantInfo import BaseCrossborderMerchantInfo


class AlipayFincoreComplianceCrossborderMerchantBatchqueryModel(object):

    def __init__(self):
        self._biz_source = None
        self._org_list = None
        self._out_biz_no = None
        self._total = None

    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def org_list(self):
        return self._org_list

    @org_list.setter
    def org_list(self, value):
        if isinstance(value, list):
            self._org_list = list()
            for i in value:
                if isinstance(i, BaseCrossborderMerchantInfo):
                    self._org_list.append(i)
                else:
                    self._org_list.append(BaseCrossborderMerchantInfo.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.org_list:
            if isinstance(self.org_list, list):
                for i in range(0, len(self.org_list)):
                    element = self.org_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.org_list[i] = element.to_alipay_dict()
            if hasattr(self.org_list, 'to_alipay_dict'):
                params['org_list'] = self.org_list.to_alipay_dict()
            else:
                params['org_list'] = self.org_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.total:
            if hasattr(self.total, 'to_alipay_dict'):
                params['total'] = self.total.to_alipay_dict()
            else:
                params['total'] = self.total
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceCrossborderMerchantBatchqueryModel()
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'org_list' in d:
            o.org_list = d['org_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'total' in d:
            o.total = d['total']
        return o


