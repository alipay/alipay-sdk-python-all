#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BccSubjectDetail(object):

    def __init__(self):
        self._completions = None
        self._current_value = None
        self._item_no = None
        self._subject_id = None
        self._subject_type = None

    @property
    def completions(self):
        return self._completions

    @completions.setter
    def completions(self, value):
        self._completions = value
    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, value):
        self._current_value = value
    @property
    def item_no(self):
        return self._item_no

    @item_no.setter
    def item_no(self, value):
        self._item_no = value
    @property
    def subject_id(self):
        return self._subject_id

    @subject_id.setter
    def subject_id(self, value):
        self._subject_id = value
    @property
    def subject_type(self):
        return self._subject_type

    @subject_type.setter
    def subject_type(self, value):
        self._subject_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.completions:
            if hasattr(self.completions, 'to_alipay_dict'):
                params['completions'] = self.completions.to_alipay_dict()
            else:
                params['completions'] = self.completions
        if self.current_value:
            if hasattr(self.current_value, 'to_alipay_dict'):
                params['current_value'] = self.current_value.to_alipay_dict()
            else:
                params['current_value'] = self.current_value
        if self.item_no:
            if hasattr(self.item_no, 'to_alipay_dict'):
                params['item_no'] = self.item_no.to_alipay_dict()
            else:
                params['item_no'] = self.item_no
        if self.subject_id:
            if hasattr(self.subject_id, 'to_alipay_dict'):
                params['subject_id'] = self.subject_id.to_alipay_dict()
            else:
                params['subject_id'] = self.subject_id
        if self.subject_type:
            if hasattr(self.subject_type, 'to_alipay_dict'):
                params['subject_type'] = self.subject_type.to_alipay_dict()
            else:
                params['subject_type'] = self.subject_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BccSubjectDetail()
        if 'completions' in d:
            o.completions = d['completions']
        if 'current_value' in d:
            o.current_value = d['current_value']
        if 'item_no' in d:
            o.item_no = d['item_no']
        if 'subject_id' in d:
            o.subject_id = d['subject_id']
        if 'subject_type' in d:
            o.subject_type = d['subject_type']
        return o


