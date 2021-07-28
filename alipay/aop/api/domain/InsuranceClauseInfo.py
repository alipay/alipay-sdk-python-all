#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuranceClauseInfo(object):

    def __init__(self):
        self._additional_item = None
        self._main_item_code = None
        self._main_item_content = None
        self._special = None

    @property
    def additional_item(self):
        return self._additional_item

    @additional_item.setter
    def additional_item(self, value):
        self._additional_item = value
    @property
    def main_item_code(self):
        return self._main_item_code

    @main_item_code.setter
    def main_item_code(self, value):
        self._main_item_code = value
    @property
    def main_item_content(self):
        return self._main_item_content

    @main_item_content.setter
    def main_item_content(self, value):
        self._main_item_content = value
    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, value):
        self._special = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_item:
            if hasattr(self.additional_item, 'to_alipay_dict'):
                params['additional_item'] = self.additional_item.to_alipay_dict()
            else:
                params['additional_item'] = self.additional_item
        if self.main_item_code:
            if hasattr(self.main_item_code, 'to_alipay_dict'):
                params['main_item_code'] = self.main_item_code.to_alipay_dict()
            else:
                params['main_item_code'] = self.main_item_code
        if self.main_item_content:
            if hasattr(self.main_item_content, 'to_alipay_dict'):
                params['main_item_content'] = self.main_item_content.to_alipay_dict()
            else:
                params['main_item_content'] = self.main_item_content
        if self.special:
            if hasattr(self.special, 'to_alipay_dict'):
                params['special'] = self.special.to_alipay_dict()
            else:
                params['special'] = self.special
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuranceClauseInfo()
        if 'additional_item' in d:
            o.additional_item = d['additional_item']
        if 'main_item_code' in d:
            o.main_item_code = d['main_item_code']
        if 'main_item_content' in d:
            o.main_item_content = d['main_item_content']
        if 'special' in d:
            o.special = d['special']
        return o


