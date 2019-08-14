#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderLogisticsInformation(object):

    def __init__(self):
        self._express_company = None
        self._tracking_no = None

    @property
    def express_company(self):
        return self._express_company

    @express_company.setter
    def express_company(self, value):
        self._express_company = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_company:
            if hasattr(self.express_company, 'to_alipay_dict'):
                params['express_company'] = self.express_company.to_alipay_dict()
            else:
                params['express_company'] = self.express_company
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderLogisticsInformation()
        if 'express_company' in d:
            o.express_company = d['express_company']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o


