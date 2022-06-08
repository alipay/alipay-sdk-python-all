#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundExtInfo import FundExtInfo


class AlipayFundEnterprisepayGroupModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._biz_scene = None
        self._fund_ext_info = None
        self._name = None
        self._operation_type_list = None
        self._out_biz_no = None
        self._product_code = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
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
    def fund_ext_info(self):
        return self._fund_ext_info

    @fund_ext_info.setter
    def fund_ext_info(self, value):
        if isinstance(value, FundExtInfo):
            self._fund_ext_info = value
        else:
            self._fund_ext_info = FundExtInfo.from_alipay_dict(value)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operation_type_list(self):
        return self._operation_type_list

    @operation_type_list.setter
    def operation_type_list(self, value):
        if isinstance(value, list):
            self._operation_type_list = list()
            for i in value:
                self._operation_type_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
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
        if self.fund_ext_info:
            if hasattr(self.fund_ext_info, 'to_alipay_dict'):
                params['fund_ext_info'] = self.fund_ext_info.to_alipay_dict()
            else:
                params['fund_ext_info'] = self.fund_ext_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operation_type_list:
            if isinstance(self.operation_type_list, list):
                for i in range(0, len(self.operation_type_list)):
                    element = self.operation_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_type_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_type_list, 'to_alipay_dict'):
                params['operation_type_list'] = self.operation_type_list.to_alipay_dict()
            else:
                params['operation_type_list'] = self.operation_type_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayFundEnterprisepayGroupModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'fund_ext_info' in d:
            o.fund_ext_info = d['fund_ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'operation_type_list' in d:
            o.operation_type_list = d['operation_type_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


