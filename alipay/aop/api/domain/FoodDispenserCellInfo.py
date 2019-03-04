#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FoodDispenserCellInfo(object):

    def __init__(self):
        self._biz_status = None
        self._cell_code = None
        self._cell_name = None
        self._column_no = None
        self._row_no = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def cell_code(self):
        return self._cell_code

    @cell_code.setter
    def cell_code(self, value):
        self._cell_code = value
    @property
    def cell_name(self):
        return self._cell_name

    @cell_name.setter
    def cell_name(self, value):
        self._cell_name = value
    @property
    def column_no(self):
        return self._column_no

    @column_no.setter
    def column_no(self, value):
        self._column_no = value
    @property
    def row_no(self):
        return self._row_no

    @row_no.setter
    def row_no(self, value):
        self._row_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.cell_code:
            if hasattr(self.cell_code, 'to_alipay_dict'):
                params['cell_code'] = self.cell_code.to_alipay_dict()
            else:
                params['cell_code'] = self.cell_code
        if self.cell_name:
            if hasattr(self.cell_name, 'to_alipay_dict'):
                params['cell_name'] = self.cell_name.to_alipay_dict()
            else:
                params['cell_name'] = self.cell_name
        if self.column_no:
            if hasattr(self.column_no, 'to_alipay_dict'):
                params['column_no'] = self.column_no.to_alipay_dict()
            else:
                params['column_no'] = self.column_no
        if self.row_no:
            if hasattr(self.row_no, 'to_alipay_dict'):
                params['row_no'] = self.row_no.to_alipay_dict()
            else:
                params['row_no'] = self.row_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FoodDispenserCellInfo()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'cell_code' in d:
            o.cell_code = d['cell_code']
        if 'cell_name' in d:
            o.cell_name = d['cell_name']
        if 'column_no' in d:
            o.column_no = d['column_no']
        if 'row_no' in d:
            o.row_no = d['row_no']
        return o


