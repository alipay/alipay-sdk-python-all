#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentRiskDetail import ContentRiskDetail
from alipay.aop.api.domain.SubContentRisks import SubContentRisks


class ContentRisks(object):

    def __init__(self):
        self._can_mark = None
        self._file_id = None
        self._file_type = None
        self._origin_file = None
        self._origin_file_id = None
        self._origin_name = None
        self._parent_file_id = None
        self._risks = None
        self._sub_contents = None

    @property
    def can_mark(self):
        return self._can_mark

    @can_mark.setter
    def can_mark(self, value):
        self._can_mark = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def origin_file(self):
        return self._origin_file

    @origin_file.setter
    def origin_file(self, value):
        self._origin_file = value
    @property
    def origin_file_id(self):
        return self._origin_file_id

    @origin_file_id.setter
    def origin_file_id(self, value):
        self._origin_file_id = value
    @property
    def origin_name(self):
        return self._origin_name

    @origin_name.setter
    def origin_name(self, value):
        self._origin_name = value
    @property
    def parent_file_id(self):
        return self._parent_file_id

    @parent_file_id.setter
    def parent_file_id(self, value):
        self._parent_file_id = value
    @property
    def risks(self):
        return self._risks

    @risks.setter
    def risks(self, value):
        if isinstance(value, list):
            self._risks = list()
            for i in value:
                if isinstance(i, ContentRiskDetail):
                    self._risks.append(i)
                else:
                    self._risks.append(ContentRiskDetail.from_alipay_dict(i))
    @property
    def sub_contents(self):
        return self._sub_contents

    @sub_contents.setter
    def sub_contents(self, value):
        if isinstance(value, list):
            self._sub_contents = list()
            for i in value:
                if isinstance(i, SubContentRisks):
                    self._sub_contents.append(i)
                else:
                    self._sub_contents.append(SubContentRisks.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.can_mark:
            if hasattr(self.can_mark, 'to_alipay_dict'):
                params['can_mark'] = self.can_mark.to_alipay_dict()
            else:
                params['can_mark'] = self.can_mark
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.origin_file:
            if hasattr(self.origin_file, 'to_alipay_dict'):
                params['origin_file'] = self.origin_file.to_alipay_dict()
            else:
                params['origin_file'] = self.origin_file
        if self.origin_file_id:
            if hasattr(self.origin_file_id, 'to_alipay_dict'):
                params['origin_file_id'] = self.origin_file_id.to_alipay_dict()
            else:
                params['origin_file_id'] = self.origin_file_id
        if self.origin_name:
            if hasattr(self.origin_name, 'to_alipay_dict'):
                params['origin_name'] = self.origin_name.to_alipay_dict()
            else:
                params['origin_name'] = self.origin_name
        if self.parent_file_id:
            if hasattr(self.parent_file_id, 'to_alipay_dict'):
                params['parent_file_id'] = self.parent_file_id.to_alipay_dict()
            else:
                params['parent_file_id'] = self.parent_file_id
        if self.risks:
            if isinstance(self.risks, list):
                for i in range(0, len(self.risks)):
                    element = self.risks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risks[i] = element.to_alipay_dict()
            if hasattr(self.risks, 'to_alipay_dict'):
                params['risks'] = self.risks.to_alipay_dict()
            else:
                params['risks'] = self.risks
        if self.sub_contents:
            if isinstance(self.sub_contents, list):
                for i in range(0, len(self.sub_contents)):
                    element = self.sub_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_contents[i] = element.to_alipay_dict()
            if hasattr(self.sub_contents, 'to_alipay_dict'):
                params['sub_contents'] = self.sub_contents.to_alipay_dict()
            else:
                params['sub_contents'] = self.sub_contents
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContentRisks()
        if 'can_mark' in d:
            o.can_mark = d['can_mark']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'origin_file' in d:
            o.origin_file = d['origin_file']
        if 'origin_file_id' in d:
            o.origin_file_id = d['origin_file_id']
        if 'origin_name' in d:
            o.origin_name = d['origin_name']
        if 'parent_file_id' in d:
            o.parent_file_id = d['parent_file_id']
        if 'risks' in d:
            o.risks = d['risks']
        if 'sub_contents' in d:
            o.sub_contents = d['sub_contents']
        return o


