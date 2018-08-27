#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsSupplierreportdetailQueryModel(object):

    def __init__(self):
        self._supplier_report_id = None

    @property
    def supplier_report_id(self):
        return self._supplier_report_id

    @supplier_report_id.setter
    def supplier_report_id(self, value):
        self._supplier_report_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.supplier_report_id:
            if hasattr(self.supplier_report_id, 'to_alipay_dict'):
                params['supplier_report_id'] = self.supplier_report_id.to_alipay_dict()
            else:
                params['supplier_report_id'] = self.supplier_report_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsSupplierreportdetailQueryModel()
        if 'supplier_report_id' in d:
            o.supplier_report_id = d['supplier_report_id']
        return o


