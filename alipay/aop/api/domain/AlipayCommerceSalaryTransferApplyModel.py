#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizSalaryOrder import BizSalaryOrder
from alipay.aop.api.domain.SalaryTransferInfo import SalaryTransferInfo


class AlipayCommerceSalaryTransferApplyModel(object):

    def __init__(self):
        self._biz_salary_order = None
        self._biz_scene = None
        self._out_biz_no = None
        self._product_code = None
        self._transfer_info = None

    @property
    def biz_salary_order(self):
        return self._biz_salary_order

    @biz_salary_order.setter
    def biz_salary_order(self, value):
        if isinstance(value, list):
            self._biz_salary_order = list()
            for i in value:
                if isinstance(i, BizSalaryOrder):
                    self._biz_salary_order.append(i)
                else:
                    self._biz_salary_order.append(BizSalaryOrder.from_alipay_dict(i))
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
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
    @property
    def transfer_info(self):
        return self._transfer_info

    @transfer_info.setter
    def transfer_info(self, value):
        if isinstance(value, SalaryTransferInfo):
            self._transfer_info = value
        else:
            self._transfer_info = SalaryTransferInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_salary_order:
            if isinstance(self.biz_salary_order, list):
                for i in range(0, len(self.biz_salary_order)):
                    element = self.biz_salary_order[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_salary_order[i] = element.to_alipay_dict()
            if hasattr(self.biz_salary_order, 'to_alipay_dict'):
                params['biz_salary_order'] = self.biz_salary_order.to_alipay_dict()
            else:
                params['biz_salary_order'] = self.biz_salary_order
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
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
        if self.transfer_info:
            if hasattr(self.transfer_info, 'to_alipay_dict'):
                params['transfer_info'] = self.transfer_info.to_alipay_dict()
            else:
                params['transfer_info'] = self.transfer_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSalaryTransferApplyModel()
        if 'biz_salary_order' in d:
            o.biz_salary_order = d['biz_salary_order']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'transfer_info' in d:
            o.transfer_info = d['transfer_info']
        return o


