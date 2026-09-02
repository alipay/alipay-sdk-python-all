#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSportsWhiteCreateModel(object):

    def __init__(self):
        self._organization_code = None
        self._roster_code = None
        self._white_type_list = None

    @property
    def organization_code(self):
        return self._organization_code

    @organization_code.setter
    def organization_code(self, value):
        self._organization_code = value
    @property
    def roster_code(self):
        return self._roster_code

    @roster_code.setter
    def roster_code(self, value):
        self._roster_code = value
    @property
    def white_type_list(self):
        return self._white_type_list

    @white_type_list.setter
    def white_type_list(self, value):
        if isinstance(value, list):
            self._white_type_list = list()
            for i in value:
                self._white_type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.organization_code:
            if hasattr(self.organization_code, 'to_alipay_dict'):
                params['organization_code'] = self.organization_code.to_alipay_dict()
            else:
                params['organization_code'] = self.organization_code
        if self.roster_code:
            if hasattr(self.roster_code, 'to_alipay_dict'):
                params['roster_code'] = self.roster_code.to_alipay_dict()
            else:
                params['roster_code'] = self.roster_code
        if self.white_type_list:
            if isinstance(self.white_type_list, list):
                for i in range(0, len(self.white_type_list)):
                    element = self.white_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_type_list[i] = element.to_alipay_dict()
            if hasattr(self.white_type_list, 'to_alipay_dict'):
                params['white_type_list'] = self.white_type_list.to_alipay_dict()
            else:
                params['white_type_list'] = self.white_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSportsWhiteCreateModel()
        if 'organization_code' in d:
            o.organization_code = d['organization_code']
        if 'roster_code' in d:
            o.roster_code = d['roster_code']
        if 'white_type_list' in d:
            o.white_type_list = d['white_type_list']
        return o


