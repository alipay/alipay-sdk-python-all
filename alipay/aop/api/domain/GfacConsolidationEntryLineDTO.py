#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GfacConsolidationEntryLineDTO(object):

    def __init__(self):
        self._biz_bill_nos_map = None
        self._biz_elements = None
        self._direction = None
        self._is_fa_entry = None
        self._is_ma_entry = None
        self._line_desc = None
        self._line_no = None
        self._ma_coa_type = None
        self._ma_segments_str = None
        self._orig_amount = None
        self._segments_str = None
        self._sob_amount = None
        self._title_code = None

    @property
    def biz_bill_nos_map(self):
        return self._biz_bill_nos_map

    @biz_bill_nos_map.setter
    def biz_bill_nos_map(self, value):
        self._biz_bill_nos_map = value
    @property
    def biz_elements(self):
        return self._biz_elements

    @biz_elements.setter
    def biz_elements(self, value):
        self._biz_elements = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def is_fa_entry(self):
        return self._is_fa_entry

    @is_fa_entry.setter
    def is_fa_entry(self, value):
        self._is_fa_entry = value
    @property
    def is_ma_entry(self):
        return self._is_ma_entry

    @is_ma_entry.setter
    def is_ma_entry(self, value):
        self._is_ma_entry = value
    @property
    def line_desc(self):
        return self._line_desc

    @line_desc.setter
    def line_desc(self, value):
        self._line_desc = value
    @property
    def line_no(self):
        return self._line_no

    @line_no.setter
    def line_no(self, value):
        self._line_no = value
    @property
    def ma_coa_type(self):
        return self._ma_coa_type

    @ma_coa_type.setter
    def ma_coa_type(self, value):
        self._ma_coa_type = value
    @property
    def ma_segments_str(self):
        return self._ma_segments_str

    @ma_segments_str.setter
    def ma_segments_str(self, value):
        self._ma_segments_str = value
    @property
    def orig_amount(self):
        return self._orig_amount

    @orig_amount.setter
    def orig_amount(self, value):
        self._orig_amount = value
    @property
    def segments_str(self):
        return self._segments_str

    @segments_str.setter
    def segments_str(self, value):
        self._segments_str = value
    @property
    def sob_amount(self):
        return self._sob_amount

    @sob_amount.setter
    def sob_amount(self, value):
        self._sob_amount = value
    @property
    def title_code(self):
        return self._title_code

    @title_code.setter
    def title_code(self, value):
        self._title_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_bill_nos_map:
            if hasattr(self.biz_bill_nos_map, 'to_alipay_dict'):
                params['biz_bill_nos_map'] = self.biz_bill_nos_map.to_alipay_dict()
            else:
                params['biz_bill_nos_map'] = self.biz_bill_nos_map
        if self.biz_elements:
            if hasattr(self.biz_elements, 'to_alipay_dict'):
                params['biz_elements'] = self.biz_elements.to_alipay_dict()
            else:
                params['biz_elements'] = self.biz_elements
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.is_fa_entry:
            if hasattr(self.is_fa_entry, 'to_alipay_dict'):
                params['is_fa_entry'] = self.is_fa_entry.to_alipay_dict()
            else:
                params['is_fa_entry'] = self.is_fa_entry
        if self.is_ma_entry:
            if hasattr(self.is_ma_entry, 'to_alipay_dict'):
                params['is_ma_entry'] = self.is_ma_entry.to_alipay_dict()
            else:
                params['is_ma_entry'] = self.is_ma_entry
        if self.line_desc:
            if hasattr(self.line_desc, 'to_alipay_dict'):
                params['line_desc'] = self.line_desc.to_alipay_dict()
            else:
                params['line_desc'] = self.line_desc
        if self.line_no:
            if hasattr(self.line_no, 'to_alipay_dict'):
                params['line_no'] = self.line_no.to_alipay_dict()
            else:
                params['line_no'] = self.line_no
        if self.ma_coa_type:
            if hasattr(self.ma_coa_type, 'to_alipay_dict'):
                params['ma_coa_type'] = self.ma_coa_type.to_alipay_dict()
            else:
                params['ma_coa_type'] = self.ma_coa_type
        if self.ma_segments_str:
            if hasattr(self.ma_segments_str, 'to_alipay_dict'):
                params['ma_segments_str'] = self.ma_segments_str.to_alipay_dict()
            else:
                params['ma_segments_str'] = self.ma_segments_str
        if self.orig_amount:
            if hasattr(self.orig_amount, 'to_alipay_dict'):
                params['orig_amount'] = self.orig_amount.to_alipay_dict()
            else:
                params['orig_amount'] = self.orig_amount
        if self.segments_str:
            if hasattr(self.segments_str, 'to_alipay_dict'):
                params['segments_str'] = self.segments_str.to_alipay_dict()
            else:
                params['segments_str'] = self.segments_str
        if self.sob_amount:
            if hasattr(self.sob_amount, 'to_alipay_dict'):
                params['sob_amount'] = self.sob_amount.to_alipay_dict()
            else:
                params['sob_amount'] = self.sob_amount
        if self.title_code:
            if hasattr(self.title_code, 'to_alipay_dict'):
                params['title_code'] = self.title_code.to_alipay_dict()
            else:
                params['title_code'] = self.title_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GfacConsolidationEntryLineDTO()
        if 'biz_bill_nos_map' in d:
            o.biz_bill_nos_map = d['biz_bill_nos_map']
        if 'biz_elements' in d:
            o.biz_elements = d['biz_elements']
        if 'direction' in d:
            o.direction = d['direction']
        if 'is_fa_entry' in d:
            o.is_fa_entry = d['is_fa_entry']
        if 'is_ma_entry' in d:
            o.is_ma_entry = d['is_ma_entry']
        if 'line_desc' in d:
            o.line_desc = d['line_desc']
        if 'line_no' in d:
            o.line_no = d['line_no']
        if 'ma_coa_type' in d:
            o.ma_coa_type = d['ma_coa_type']
        if 'ma_segments_str' in d:
            o.ma_segments_str = d['ma_segments_str']
        if 'orig_amount' in d:
            o.orig_amount = d['orig_amount']
        if 'segments_str' in d:
            o.segments_str = d['segments_str']
        if 'sob_amount' in d:
            o.sob_amount = d['sob_amount']
        if 'title_code' in d:
            o.title_code = d['title_code']
        return o


