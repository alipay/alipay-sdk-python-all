#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiPartnerSaDTO(object):

    def __init__(self):
        self._keyword_index = None
        self._ou_code = None
        self._ou_id = None
        self._partner_name = None

    @property
    def keyword_index(self):
        return self._keyword_index

    @keyword_index.setter
    def keyword_index(self, value):
        self._keyword_index = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def ou_id(self):
        return self._ou_id

    @ou_id.setter
    def ou_id(self, value):
        self._ou_id = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword_index:
            if hasattr(self.keyword_index, 'to_alipay_dict'):
                params['keyword_index'] = self.keyword_index.to_alipay_dict()
            else:
                params['keyword_index'] = self.keyword_index
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.ou_id:
            if hasattr(self.ou_id, 'to_alipay_dict'):
                params['ou_id'] = self.ou_id.to_alipay_dict()
            else:
                params['ou_id'] = self.ou_id
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiPartnerSaDTO()
        if 'keyword_index' in d:
            o.keyword_index = d['keyword_index']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'ou_id' in d:
            o.ou_id = d['ou_id']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        return o


