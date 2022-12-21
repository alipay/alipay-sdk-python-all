#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGORightConfig(object):

    def __init__(self):
        self._cumulative_preferential_redirect_schema = None
        self._custom_benefit_desc = None
        self._custom_sub_benefit_desc = None

    @property
    def cumulative_preferential_redirect_schema(self):
        return self._cumulative_preferential_redirect_schema

    @cumulative_preferential_redirect_schema.setter
    def cumulative_preferential_redirect_schema(self, value):
        self._cumulative_preferential_redirect_schema = value
    @property
    def custom_benefit_desc(self):
        return self._custom_benefit_desc

    @custom_benefit_desc.setter
    def custom_benefit_desc(self, value):
        self._custom_benefit_desc = value
    @property
    def custom_sub_benefit_desc(self):
        return self._custom_sub_benefit_desc

    @custom_sub_benefit_desc.setter
    def custom_sub_benefit_desc(self, value):
        self._custom_sub_benefit_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.cumulative_preferential_redirect_schema:
            if hasattr(self.cumulative_preferential_redirect_schema, 'to_alipay_dict'):
                params['cumulative_preferential_redirect_schema'] = self.cumulative_preferential_redirect_schema.to_alipay_dict()
            else:
                params['cumulative_preferential_redirect_schema'] = self.cumulative_preferential_redirect_schema
        if self.custom_benefit_desc:
            if hasattr(self.custom_benefit_desc, 'to_alipay_dict'):
                params['custom_benefit_desc'] = self.custom_benefit_desc.to_alipay_dict()
            else:
                params['custom_benefit_desc'] = self.custom_benefit_desc
        if self.custom_sub_benefit_desc:
            if hasattr(self.custom_sub_benefit_desc, 'to_alipay_dict'):
                params['custom_sub_benefit_desc'] = self.custom_sub_benefit_desc.to_alipay_dict()
            else:
                params['custom_sub_benefit_desc'] = self.custom_sub_benefit_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGORightConfig()
        if 'cumulative_preferential_redirect_schema' in d:
            o.cumulative_preferential_redirect_schema = d['cumulative_preferential_redirect_schema']
        if 'custom_benefit_desc' in d:
            o.custom_benefit_desc = d['custom_benefit_desc']
        if 'custom_sub_benefit_desc' in d:
            o.custom_sub_benefit_desc = d['custom_sub_benefit_desc']
        return o


