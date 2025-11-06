#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GuidanceUseDrugItem(object):

    def __init__(self):
        self._drug_name = None
        self._drug_num = None
        self._drug_specifications = None
        self._notice_info = None
        self._over_instruction_str = None
        self._usage = None

    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value
    @property
    def drug_num(self):
        return self._drug_num

    @drug_num.setter
    def drug_num(self, value):
        self._drug_num = value
    @property
    def drug_specifications(self):
        return self._drug_specifications

    @drug_specifications.setter
    def drug_specifications(self, value):
        self._drug_specifications = value
    @property
    def notice_info(self):
        return self._notice_info

    @notice_info.setter
    def notice_info(self, value):
        self._notice_info = value
    @property
    def over_instruction_str(self):
        return self._over_instruction_str

    @over_instruction_str.setter
    def over_instruction_str(self, value):
        self._over_instruction_str = value
    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, value):
        self._usage = value


    def to_alipay_dict(self):
        params = dict()
        if self.drug_name:
            if hasattr(self.drug_name, 'to_alipay_dict'):
                params['drug_name'] = self.drug_name.to_alipay_dict()
            else:
                params['drug_name'] = self.drug_name
        if self.drug_num:
            if hasattr(self.drug_num, 'to_alipay_dict'):
                params['drug_num'] = self.drug_num.to_alipay_dict()
            else:
                params['drug_num'] = self.drug_num
        if self.drug_specifications:
            if hasattr(self.drug_specifications, 'to_alipay_dict'):
                params['drug_specifications'] = self.drug_specifications.to_alipay_dict()
            else:
                params['drug_specifications'] = self.drug_specifications
        if self.notice_info:
            if hasattr(self.notice_info, 'to_alipay_dict'):
                params['notice_info'] = self.notice_info.to_alipay_dict()
            else:
                params['notice_info'] = self.notice_info
        if self.over_instruction_str:
            if hasattr(self.over_instruction_str, 'to_alipay_dict'):
                params['over_instruction_str'] = self.over_instruction_str.to_alipay_dict()
            else:
                params['over_instruction_str'] = self.over_instruction_str
        if self.usage:
            if hasattr(self.usage, 'to_alipay_dict'):
                params['usage'] = self.usage.to_alipay_dict()
            else:
                params['usage'] = self.usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GuidanceUseDrugItem()
        if 'drug_name' in d:
            o.drug_name = d['drug_name']
        if 'drug_num' in d:
            o.drug_num = d['drug_num']
        if 'drug_specifications' in d:
            o.drug_specifications = d['drug_specifications']
        if 'notice_info' in d:
            o.notice_info = d['notice_info']
        if 'over_instruction_str' in d:
            o.over_instruction_str = d['over_instruction_str']
        if 'usage' in d:
            o.usage = d['usage']
        return o


