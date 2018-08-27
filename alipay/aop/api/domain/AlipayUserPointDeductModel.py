#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserPointDeductModel(object):

    def __init__(self):
        self._benefit_id = None
        self._biz_date = None
        self._biz_type = None
        self._out_biz_no = None
        self._prod_title = None
        self._sub_biz_type = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_title(self):
        return self._prod_title

    @prod_title.setter
    def prod_title(self, value):
        self._prod_title = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_title:
            if hasattr(self.prod_title, 'to_alipay_dict'):
                params['prod_title'] = self.prod_title.to_alipay_dict()
            else:
                params['prod_title'] = self.prod_title
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserPointDeductModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_title' in d:
            o.prod_title = d['prod_title']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


