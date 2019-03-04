#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneProductInquiryApplyModel(object):

    def __init__(self):
        self._applicant = None
        self._biz_data = None
        self._copies_count = None
        self._insureds = None
        self._out_biz_no = None
        self._period = None
        self._prod_code = None
        self._source = None
        self._sum_insured = None

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsPerson):
            self._applicant = value
        else:
            self._applicant = InsPerson.from_alipay_dict(value)
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def copies_count(self):
        return self._copies_count

    @copies_count.setter
    def copies_count(self, value):
        self._copies_count = value
    @property
    def insureds(self):
        return self._insureds

    @insureds.setter
    def insureds(self, value):
        if isinstance(value, list):
            self._insureds = list()
            for i in value:
                if isinstance(i, InsPerson):
                    self._insureds.append(i)
                else:
                    self._insureds.append(InsPerson.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.copies_count:
            if hasattr(self.copies_count, 'to_alipay_dict'):
                params['copies_count'] = self.copies_count.to_alipay_dict()
            else:
                params['copies_count'] = self.copies_count
        if self.insureds:
            if isinstance(self.insureds, list):
                for i in range(0, len(self.insureds)):
                    element = self.insureds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insureds[i] = element.to_alipay_dict()
            if hasattr(self.insureds, 'to_alipay_dict'):
                params['insureds'] = self.insureds.to_alipay_dict()
            else:
                params['insureds'] = self.insureds
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneProductInquiryApplyModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'copies_count' in d:
            o.copies_count = d['copies_count']
        if 'insureds' in d:
            o.insureds = d['insureds']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period' in d:
            o.period = d['period']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'source' in d:
            o.source = d['source']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


