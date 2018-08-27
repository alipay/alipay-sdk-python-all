#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CodeNOList import CodeNOList


class AlipayEcoMycarPromoTicketSyncModel(object):

    def __init__(self):
        self._active_id = None
        self._code_no_list = None
        self._source_type = None

    @property
    def active_id(self):
        return self._active_id

    @active_id.setter
    def active_id(self, value):
        self._active_id = value
    @property
    def code_no_list(self):
        return self._code_no_list

    @code_no_list.setter
    def code_no_list(self, value):
        if isinstance(value, list):
            self._code_no_list = list()
            for i in value:
                if isinstance(i, CodeNOList):
                    self._code_no_list.append(i)
                else:
                    self._code_no_list.append(CodeNOList.from_alipay_dict(i))
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_id:
            if hasattr(self.active_id, 'to_alipay_dict'):
                params['active_id'] = self.active_id.to_alipay_dict()
            else:
                params['active_id'] = self.active_id
        if self.code_no_list:
            if isinstance(self.code_no_list, list):
                for i in range(0, len(self.code_no_list)):
                    element = self.code_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_no_list[i] = element.to_alipay_dict()
            if hasattr(self.code_no_list, 'to_alipay_dict'):
                params['code_no_list'] = self.code_no_list.to_alipay_dict()
            else:
                params['code_no_list'] = self.code_no_list
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarPromoTicketSyncModel()
        if 'active_id' in d:
            o.active_id = d['active_id']
        if 'code_no_list' in d:
            o.code_no_list = d['code_no_list']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


