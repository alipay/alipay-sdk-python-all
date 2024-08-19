#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApprovalFlowInfo import ApprovalFlowInfo


class AntlescenterProcessDTO(object):

    def __init__(self):
        self._process_extra = None
        self._process_id = None
        self._process_info_list = None
        self._process_type = None

    @property
    def process_extra(self):
        return self._process_extra

    @process_extra.setter
    def process_extra(self, value):
        self._process_extra = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def process_info_list(self):
        return self._process_info_list

    @process_info_list.setter
    def process_info_list(self, value):
        if isinstance(value, list):
            self._process_info_list = list()
            for i in value:
                if isinstance(i, ApprovalFlowInfo):
                    self._process_info_list.append(i)
                else:
                    self._process_info_list.append(ApprovalFlowInfo.from_alipay_dict(i))
    @property
    def process_type(self):
        return self._process_type

    @process_type.setter
    def process_type(self, value):
        self._process_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.process_extra:
            if hasattr(self.process_extra, 'to_alipay_dict'):
                params['process_extra'] = self.process_extra.to_alipay_dict()
            else:
                params['process_extra'] = self.process_extra
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.process_info_list:
            if isinstance(self.process_info_list, list):
                for i in range(0, len(self.process_info_list)):
                    element = self.process_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.process_info_list[i] = element.to_alipay_dict()
            if hasattr(self.process_info_list, 'to_alipay_dict'):
                params['process_info_list'] = self.process_info_list.to_alipay_dict()
            else:
                params['process_info_list'] = self.process_info_list
        if self.process_type:
            if hasattr(self.process_type, 'to_alipay_dict'):
                params['process_type'] = self.process_type.to_alipay_dict()
            else:
                params['process_type'] = self.process_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntlescenterProcessDTO()
        if 'process_extra' in d:
            o.process_extra = d['process_extra']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'process_info_list' in d:
            o.process_info_list = d['process_info_list']
        if 'process_type' in d:
            o.process_type = d['process_type']
        return o


