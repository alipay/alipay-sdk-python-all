#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryLogistics(object):

    def __init__(self):
        self._delivery_status = None
        self._express_company_code = None
        self._express_company_name = None
        self._express_no = None

    @property
    def delivery_status(self):
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, value):
        self._delivery_status = value
    @property
    def express_company_code(self):
        return self._express_company_code

    @express_company_code.setter
    def express_company_code(self, value):
        self._express_company_code = value
    @property
    def express_company_name(self):
        return self._express_company_name

    @express_company_name.setter
    def express_company_name(self, value):
        self._express_company_name = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_status:
            if hasattr(self.delivery_status, 'to_alipay_dict'):
                params['delivery_status'] = self.delivery_status.to_alipay_dict()
            else:
                params['delivery_status'] = self.delivery_status
        if self.express_company_code:
            if hasattr(self.express_company_code, 'to_alipay_dict'):
                params['express_company_code'] = self.express_company_code.to_alipay_dict()
            else:
                params['express_company_code'] = self.express_company_code
        if self.express_company_name:
            if hasattr(self.express_company_name, 'to_alipay_dict'):
                params['express_company_name'] = self.express_company_name.to_alipay_dict()
            else:
                params['express_company_name'] = self.express_company_name
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryLogistics()
        if 'delivery_status' in d:
            o.delivery_status = d['delivery_status']
        if 'express_company_code' in d:
            o.express_company_code = d['express_company_code']
        if 'express_company_name' in d:
            o.express_company_name = d['express_company_name']
        if 'express_no' in d:
            o.express_no = d['express_no']
        return o


