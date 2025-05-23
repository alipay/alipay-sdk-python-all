#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingNewhouseLayoutQueryModel(object):

    def __init__(self):
        self._estate_project_id = None
        self._external_id = None
        self._page_num = None
        self._page_size = None

    @property
    def estate_project_id(self):
        return self._estate_project_id

    @estate_project_id.setter
    def estate_project_id(self, value):
        self._estate_project_id = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
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
        if self.estate_project_id:
            if hasattr(self.estate_project_id, 'to_alipay_dict'):
                params['estate_project_id'] = self.estate_project_id.to_alipay_dict()
            else:
                params['estate_project_id'] = self.estate_project_id
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
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
        o = AlipayCommerceHousingNewhouseLayoutQueryModel()
        if 'estate_project_id' in d:
            o.estate_project_id = d['estate_project_id']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


