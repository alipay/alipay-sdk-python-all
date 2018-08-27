#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneApplicationBatchqueryModel(object):

    def __init__(self):
        self._applicant = None
        self._out_biz_no = None
        self._source = None

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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationBatchqueryModel()
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'source' in d:
            o.source = d['source']
        return o


