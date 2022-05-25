#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdvanceElementsDTO import AdvanceElementsDTO


class InstAccountElementsDTO(object):

    def __init__(self):
        self._advance_elements = None
        self._inst_id = None
        self._sub_account_name = None
        self._sub_account_type = None

    @property
    def advance_elements(self):
        return self._advance_elements

    @advance_elements.setter
    def advance_elements(self, value):
        if isinstance(value, AdvanceElementsDTO):
            self._advance_elements = value
        else:
            self._advance_elements = AdvanceElementsDTO.from_alipay_dict(value)
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def sub_account_name(self):
        return self._sub_account_name

    @sub_account_name.setter
    def sub_account_name(self, value):
        self._sub_account_name = value
    @property
    def sub_account_type(self):
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, value):
        self._sub_account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_elements:
            if hasattr(self.advance_elements, 'to_alipay_dict'):
                params['advance_elements'] = self.advance_elements.to_alipay_dict()
            else:
                params['advance_elements'] = self.advance_elements
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.sub_account_name:
            if hasattr(self.sub_account_name, 'to_alipay_dict'):
                params['sub_account_name'] = self.sub_account_name.to_alipay_dict()
            else:
                params['sub_account_name'] = self.sub_account_name
        if self.sub_account_type:
            if hasattr(self.sub_account_type, 'to_alipay_dict'):
                params['sub_account_type'] = self.sub_account_type.to_alipay_dict()
            else:
                params['sub_account_type'] = self.sub_account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstAccountElementsDTO()
        if 'advance_elements' in d:
            o.advance_elements = d['advance_elements']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'sub_account_name' in d:
            o.sub_account_name = d['sub_account_name']
        if 'sub_account_type' in d:
            o.sub_account_type = d['sub_account_type']
        return o


