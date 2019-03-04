#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ColumnMoreInfoModel import ColumnMoreInfoModel


class ViewColumnInfoModel(object):

    def __init__(self):
        self._code = None
        self._column_more_info = None
        self._operate_type = None
        self._title = None
        self._value = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def column_more_info(self):
        return self._column_more_info

    @column_more_info.setter
    def column_more_info(self, value):
        if isinstance(value, ColumnMoreInfoModel):
            self._column_more_info = value
        else:
            self._column_more_info = ColumnMoreInfoModel.from_alipay_dict(value)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.column_more_info:
            if hasattr(self.column_more_info, 'to_alipay_dict'):
                params['column_more_info'] = self.column_more_info.to_alipay_dict()
            else:
                params['column_more_info'] = self.column_more_info
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ViewColumnInfoModel()
        if 'code' in d:
            o.code = d['code']
        if 'column_more_info' in d:
            o.column_more_info = d['column_more_info']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'title' in d:
            o.title = d['title']
        if 'value' in d:
            o.value = d['value']
        return o


