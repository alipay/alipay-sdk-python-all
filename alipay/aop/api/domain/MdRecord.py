#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FvPairList import FvPairList


class MdRecord(object):

    def __init__(self):
        self._data_struct = None
        self._dicode = None
        self._diname = None
        self._dynamic_fields = None
        self._gmt_modified = None
        self._id = None
        self._memo = None
        self._multi_parents = None

    @property
    def data_struct(self):
        return self._data_struct

    @data_struct.setter
    def data_struct(self, value):
        self._data_struct = value
    @property
    def dicode(self):
        return self._dicode

    @dicode.setter
    def dicode(self, value):
        self._dicode = value
    @property
    def diname(self):
        return self._diname

    @diname.setter
    def diname(self, value):
        self._diname = value
    @property
    def dynamic_fields(self):
        return self._dynamic_fields

    @dynamic_fields.setter
    def dynamic_fields(self, value):
        if isinstance(value, list):
            self._dynamic_fields = list()
            for i in value:
                if isinstance(i, FvPairList):
                    self._dynamic_fields.append(i)
                else:
                    self._dynamic_fields.append(FvPairList.from_alipay_dict(i))
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def multi_parents(self):
        return self._multi_parents

    @multi_parents.setter
    def multi_parents(self, value):
        if isinstance(value, list):
            self._multi_parents = list()
            for i in value:
                self._multi_parents.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.data_struct:
            if hasattr(self.data_struct, 'to_alipay_dict'):
                params['data_struct'] = self.data_struct.to_alipay_dict()
            else:
                params['data_struct'] = self.data_struct
        if self.dicode:
            if hasattr(self.dicode, 'to_alipay_dict'):
                params['dicode'] = self.dicode.to_alipay_dict()
            else:
                params['dicode'] = self.dicode
        if self.diname:
            if hasattr(self.diname, 'to_alipay_dict'):
                params['diname'] = self.diname.to_alipay_dict()
            else:
                params['diname'] = self.diname
        if self.dynamic_fields:
            if isinstance(self.dynamic_fields, list):
                for i in range(0, len(self.dynamic_fields)):
                    element = self.dynamic_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dynamic_fields[i] = element.to_alipay_dict()
            if hasattr(self.dynamic_fields, 'to_alipay_dict'):
                params['dynamic_fields'] = self.dynamic_fields.to_alipay_dict()
            else:
                params['dynamic_fields'] = self.dynamic_fields
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.multi_parents:
            if isinstance(self.multi_parents, list):
                for i in range(0, len(self.multi_parents)):
                    element = self.multi_parents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.multi_parents[i] = element.to_alipay_dict()
            if hasattr(self.multi_parents, 'to_alipay_dict'):
                params['multi_parents'] = self.multi_parents.to_alipay_dict()
            else:
                params['multi_parents'] = self.multi_parents
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MdRecord()
        if 'data_struct' in d:
            o.data_struct = d['data_struct']
        if 'dicode' in d:
            o.dicode = d['dicode']
        if 'diname' in d:
            o.diname = d['diname']
        if 'dynamic_fields' in d:
            o.dynamic_fields = d['dynamic_fields']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'multi_parents' in d:
            o.multi_parents = d['multi_parents']
        return o


