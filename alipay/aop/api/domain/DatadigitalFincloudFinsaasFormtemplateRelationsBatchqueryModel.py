#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasFormtemplateRelationsBatchqueryModel(object):

    def __init__(self):
        self._marketing_type = None
        self._page_num = None
        self._page_size = None

    @property
    def marketing_type(self):
        return self._marketing_type

    @marketing_type.setter
    def marketing_type(self, value):
        self._marketing_type = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.marketing_type:
            if hasattr(self.marketing_type, 'to_alipay_dict'):
                params['marketing_type'] = self.marketing_type.to_alipay_dict()
            else:
                params['marketing_type'] = self.marketing_type
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasFormtemplateRelationsBatchqueryModel()
        if 'marketing_type' in d:
            o.marketing_type = d['marketing_type']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


