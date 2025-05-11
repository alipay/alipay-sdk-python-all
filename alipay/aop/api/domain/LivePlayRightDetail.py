#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LivePlayRightDetail(object):

    def __init__(self):
        self._jump_url = None
        self._right_amount = None
        self._right_desc_text = None
        self._right_name_text = None
        self._right_title_text = None
        self._right_unit = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def right_amount(self):
        return self._right_amount

    @right_amount.setter
    def right_amount(self, value):
        self._right_amount = value
    @property
    def right_desc_text(self):
        return self._right_desc_text

    @right_desc_text.setter
    def right_desc_text(self, value):
        self._right_desc_text = value
    @property
    def right_name_text(self):
        return self._right_name_text

    @right_name_text.setter
    def right_name_text(self, value):
        self._right_name_text = value
    @property
    def right_title_text(self):
        return self._right_title_text

    @right_title_text.setter
    def right_title_text(self, value):
        self._right_title_text = value
    @property
    def right_unit(self):
        return self._right_unit

    @right_unit.setter
    def right_unit(self, value):
        self._right_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.right_amount:
            if hasattr(self.right_amount, 'to_alipay_dict'):
                params['right_amount'] = self.right_amount.to_alipay_dict()
            else:
                params['right_amount'] = self.right_amount
        if self.right_desc_text:
            if hasattr(self.right_desc_text, 'to_alipay_dict'):
                params['right_desc_text'] = self.right_desc_text.to_alipay_dict()
            else:
                params['right_desc_text'] = self.right_desc_text
        if self.right_name_text:
            if hasattr(self.right_name_text, 'to_alipay_dict'):
                params['right_name_text'] = self.right_name_text.to_alipay_dict()
            else:
                params['right_name_text'] = self.right_name_text
        if self.right_title_text:
            if hasattr(self.right_title_text, 'to_alipay_dict'):
                params['right_title_text'] = self.right_title_text.to_alipay_dict()
            else:
                params['right_title_text'] = self.right_title_text
        if self.right_unit:
            if hasattr(self.right_unit, 'to_alipay_dict'):
                params['right_unit'] = self.right_unit.to_alipay_dict()
            else:
                params['right_unit'] = self.right_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LivePlayRightDetail()
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'right_amount' in d:
            o.right_amount = d['right_amount']
        if 'right_desc_text' in d:
            o.right_desc_text = d['right_desc_text']
        if 'right_name_text' in d:
            o.right_name_text = d['right_name_text']
        if 'right_title_text' in d:
            o.right_title_text = d['right_title_text']
        if 'right_unit' in d:
            o.right_unit = d['right_unit']
        return o


