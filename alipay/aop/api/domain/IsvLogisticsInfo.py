#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvLogisticsInfo(object):

    def __init__(self):
        self._express_company = None
        self._express_company_bill_no = None

    @property
    def express_company(self):
        return self._express_company

    @express_company.setter
    def express_company(self, value):
        self._express_company = value
    @property
    def express_company_bill_no(self):
        return self._express_company_bill_no

    @express_company_bill_no.setter
    def express_company_bill_no(self, value):
        self._express_company_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_company:
            if hasattr(self.express_company, 'to_alipay_dict'):
                params['express_company'] = self.express_company.to_alipay_dict()
            else:
                params['express_company'] = self.express_company
        if self.express_company_bill_no:
            if hasattr(self.express_company_bill_no, 'to_alipay_dict'):
                params['express_company_bill_no'] = self.express_company_bill_no.to_alipay_dict()
            else:
                params['express_company_bill_no'] = self.express_company_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvLogisticsInfo()
        if 'express_company' in d:
            o.express_company = d['express_company']
        if 'express_company_bill_no' in d:
            o.express_company_bill_no = d['express_company_bill_no']
        return o


