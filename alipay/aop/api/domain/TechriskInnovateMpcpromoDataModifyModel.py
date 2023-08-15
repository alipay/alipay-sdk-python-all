#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ColumnData import ColumnData
from alipay.aop.api.domain.ColumnData import ColumnData


class TechriskInnovateMpcpromoDataModifyModel(object):

    def __init__(self):
        self._add_data_list = None
        self._del_data_list = None
        self._filename = None
        self._row_info_list = None

    @property
    def add_data_list(self):
        return self._add_data_list

    @add_data_list.setter
    def add_data_list(self, value):
        if isinstance(value, list):
            self._add_data_list = list()
            for i in value:
                if isinstance(i, ColumnData):
                    self._add_data_list.append(i)
                else:
                    self._add_data_list.append(ColumnData.from_alipay_dict(i))
    @property
    def del_data_list(self):
        return self._del_data_list

    @del_data_list.setter
    def del_data_list(self, value):
        if isinstance(value, list):
            self._del_data_list = list()
            for i in value:
                if isinstance(i, ColumnData):
                    self._del_data_list.append(i)
                else:
                    self._del_data_list.append(ColumnData.from_alipay_dict(i))
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value
    @property
    def row_info_list(self):
        return self._row_info_list

    @row_info_list.setter
    def row_info_list(self, value):
        if isinstance(value, list):
            self._row_info_list = list()
            for i in value:
                self._row_info_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.add_data_list:
            if isinstance(self.add_data_list, list):
                for i in range(0, len(self.add_data_list)):
                    element = self.add_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_data_list[i] = element.to_alipay_dict()
            if hasattr(self.add_data_list, 'to_alipay_dict'):
                params['add_data_list'] = self.add_data_list.to_alipay_dict()
            else:
                params['add_data_list'] = self.add_data_list
        if self.del_data_list:
            if isinstance(self.del_data_list, list):
                for i in range(0, len(self.del_data_list)):
                    element = self.del_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.del_data_list[i] = element.to_alipay_dict()
            if hasattr(self.del_data_list, 'to_alipay_dict'):
                params['del_data_list'] = self.del_data_list.to_alipay_dict()
            else:
                params['del_data_list'] = self.del_data_list
        if self.filename:
            if hasattr(self.filename, 'to_alipay_dict'):
                params['filename'] = self.filename.to_alipay_dict()
            else:
                params['filename'] = self.filename
        if self.row_info_list:
            if isinstance(self.row_info_list, list):
                for i in range(0, len(self.row_info_list)):
                    element = self.row_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.row_info_list[i] = element.to_alipay_dict()
            if hasattr(self.row_info_list, 'to_alipay_dict'):
                params['row_info_list'] = self.row_info_list.to_alipay_dict()
            else:
                params['row_info_list'] = self.row_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskInnovateMpcpromoDataModifyModel()
        if 'add_data_list' in d:
            o.add_data_list = d['add_data_list']
        if 'del_data_list' in d:
            o.del_data_list = d['del_data_list']
        if 'filename' in d:
            o.filename = d['filename']
        if 'row_info_list' in d:
            o.row_info_list = d['row_info_list']
        return o


