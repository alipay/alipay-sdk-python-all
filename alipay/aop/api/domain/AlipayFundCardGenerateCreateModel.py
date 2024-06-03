#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundCardGenerateOrder import FundCardGenerateOrder


class AlipayFundCardGenerateCreateModel(object):

    def __init__(self):
        self._agreement_no = None
        self._biz_scene = None
        self._fund_source = None
        self._fund_source_cert = None
        self._order_list = None
        self._out_request_no = None
        self._product_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def fund_source(self):
        return self._fund_source

    @fund_source.setter
    def fund_source(self, value):
        self._fund_source = value
    @property
    def fund_source_cert(self):
        return self._fund_source_cert

    @fund_source_cert.setter
    def fund_source_cert(self, value):
        self._fund_source_cert = value
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, FundCardGenerateOrder):
                    self._order_list.append(i)
                else:
                    self._order_list.append(FundCardGenerateOrder.from_alipay_dict(i))
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.fund_source:
            if hasattr(self.fund_source, 'to_alipay_dict'):
                params['fund_source'] = self.fund_source.to_alipay_dict()
            else:
                params['fund_source'] = self.fund_source
        if self.fund_source_cert:
            if hasattr(self.fund_source_cert, 'to_alipay_dict'):
                params['fund_source_cert'] = self.fund_source_cert.to_alipay_dict()
            else:
                params['fund_source_cert'] = self.fund_source_cert
        if self.order_list:
            if isinstance(self.order_list, list):
                for i in range(0, len(self.order_list)):
                    element = self.order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_list[i] = element.to_alipay_dict()
            if hasattr(self.order_list, 'to_alipay_dict'):
                params['order_list'] = self.order_list.to_alipay_dict()
            else:
                params['order_list'] = self.order_list
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundCardGenerateCreateModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'fund_source' in d:
            o.fund_source = d['fund_source']
        if 'fund_source_cert' in d:
            o.fund_source_cert = d['fund_source_cert']
        if 'order_list' in d:
            o.order_list = d['order_list']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


