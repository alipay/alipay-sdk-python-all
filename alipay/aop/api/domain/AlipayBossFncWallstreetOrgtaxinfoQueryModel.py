#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncWallstreetOrgtaxinfoQueryModel(object):

    def __init__(self):
        self._org_code = None
        self._org_id = None
        self._purchaser_tax_no = None

    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def purchaser_tax_no(self):
        return self._purchaser_tax_no

    @purchaser_tax_no.setter
    def purchaser_tax_no(self, value):
        self._purchaser_tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.purchaser_tax_no:
            if hasattr(self.purchaser_tax_no, 'to_alipay_dict'):
                params['purchaser_tax_no'] = self.purchaser_tax_no.to_alipay_dict()
            else:
                params['purchaser_tax_no'] = self.purchaser_tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncWallstreetOrgtaxinfoQueryModel()
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'purchaser_tax_no' in d:
            o.purchaser_tax_no = d['purchaser_tax_no']
        return o


