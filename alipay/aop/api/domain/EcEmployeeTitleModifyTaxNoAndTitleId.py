#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcEmployeeTitleModifyTaxNoAndTitleId(object):

    def __init__(self):
        self._tax_register_no = None
        self._title_id = None

    @property
    def tax_register_no(self):
        return self._tax_register_no

    @tax_register_no.setter
    def tax_register_no(self, value):
        self._tax_register_no = value
    @property
    def title_id(self):
        return self._title_id

    @title_id.setter
    def title_id(self, value):
        self._title_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tax_register_no:
            if hasattr(self.tax_register_no, 'to_alipay_dict'):
                params['tax_register_no'] = self.tax_register_no.to_alipay_dict()
            else:
                params['tax_register_no'] = self.tax_register_no
        if self.title_id:
            if hasattr(self.title_id, 'to_alipay_dict'):
                params['title_id'] = self.title_id.to_alipay_dict()
            else:
                params['title_id'] = self.title_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcEmployeeTitleModifyTaxNoAndTitleId()
        if 'tax_register_no' in d:
            o.tax_register_no = d['tax_register_no']
        if 'title_id' in d:
            o.title_id = d['title_id']
        return o


