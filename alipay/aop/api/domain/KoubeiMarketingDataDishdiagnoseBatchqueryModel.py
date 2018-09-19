#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataDishdiagnoseBatchqueryModel(object):

    def __init__(self):
        self._item_diagnose_type = None
        self._page_no = None
        self._page_size = None
        self._report_date = None

    @property
    def item_diagnose_type(self):
        return self._item_diagnose_type

    @item_diagnose_type.setter
    def item_diagnose_type(self, value):
        self._item_diagnose_type = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_diagnose_type:
            if hasattr(self.item_diagnose_type, 'to_alipay_dict'):
                params['item_diagnose_type'] = self.item_diagnose_type.to_alipay_dict()
            else:
                params['item_diagnose_type'] = self.item_diagnose_type
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataDishdiagnoseBatchqueryModel()
        if 'item_diagnose_type' in d:
            o.item_diagnose_type = d['item_diagnose_type']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


