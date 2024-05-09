#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTaxbillSignQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._contractor_code = None
        self._employer_code = None
        self._identification_in_belonging_employer = None
        self._product_code = None
        self._solution_code = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def contractor_code(self):
        return self._contractor_code

    @contractor_code.setter
    def contractor_code(self, value):
        self._contractor_code = value
    @property
    def employer_code(self):
        return self._employer_code

    @employer_code.setter
    def employer_code(self, value):
        self._employer_code = value
    @property
    def identification_in_belonging_employer(self):
        return self._identification_in_belonging_employer

    @identification_in_belonging_employer.setter
    def identification_in_belonging_employer(self, value):
        self._identification_in_belonging_employer = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.contractor_code:
            if hasattr(self.contractor_code, 'to_alipay_dict'):
                params['contractor_code'] = self.contractor_code.to_alipay_dict()
            else:
                params['contractor_code'] = self.contractor_code
        if self.employer_code:
            if hasattr(self.employer_code, 'to_alipay_dict'):
                params['employer_code'] = self.employer_code.to_alipay_dict()
            else:
                params['employer_code'] = self.employer_code
        if self.identification_in_belonging_employer:
            if hasattr(self.identification_in_belonging_employer, 'to_alipay_dict'):
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer.to_alipay_dict()
            else:
                params['identification_in_belonging_employer'] = self.identification_in_belonging_employer
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTaxbillSignQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'contractor_code' in d:
            o.contractor_code = d['contractor_code']
        if 'employer_code' in d:
            o.employer_code = d['employer_code']
        if 'identification_in_belonging_employer' in d:
            o.identification_in_belonging_employer = d['identification_in_belonging_employer']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


