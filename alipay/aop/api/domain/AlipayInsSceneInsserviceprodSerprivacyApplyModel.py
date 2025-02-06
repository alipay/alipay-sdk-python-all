#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceConsultFactor import ServiceConsultFactor


class AlipayInsSceneInsserviceprodSerprivacyApplyModel(object):

    def __init__(self):
        self._apply_order_no = None
        self._biz_code = None
        self._consult_factor_list = None
        self._contract_no = None
        self._request_no = None

    @property
    def apply_order_no(self):
        return self._apply_order_no

    @apply_order_no.setter
    def apply_order_no(self, value):
        self._apply_order_no = value
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def consult_factor_list(self):
        return self._consult_factor_list

    @consult_factor_list.setter
    def consult_factor_list(self, value):
        if isinstance(value, list):
            self._consult_factor_list = list()
            for i in value:
                if isinstance(i, ServiceConsultFactor):
                    self._consult_factor_list.append(i)
                else:
                    self._consult_factor_list.append(ServiceConsultFactor.from_alipay_dict(i))
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_order_no:
            if hasattr(self.apply_order_no, 'to_alipay_dict'):
                params['apply_order_no'] = self.apply_order_no.to_alipay_dict()
            else:
                params['apply_order_no'] = self.apply_order_no
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.consult_factor_list:
            if isinstance(self.consult_factor_list, list):
                for i in range(0, len(self.consult_factor_list)):
                    element = self.consult_factor_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consult_factor_list[i] = element.to_alipay_dict()
            if hasattr(self.consult_factor_list, 'to_alipay_dict'):
                params['consult_factor_list'] = self.consult_factor_list.to_alipay_dict()
            else:
                params['consult_factor_list'] = self.consult_factor_list
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInsserviceprodSerprivacyApplyModel()
        if 'apply_order_no' in d:
            o.apply_order_no = d['apply_order_no']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'consult_factor_list' in d:
            o.consult_factor_list = d['consult_factor_list']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        return o


