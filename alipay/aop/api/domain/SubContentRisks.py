#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContentRiskDetail import ContentRiskDetail


class SubContentRisks(object):

    def __init__(self):
        self._can_mark = None
        self._ext = None
        self._file_id = None
        self._file_type = None
        self._generated_url = None
        self._origin_file = None
        self._origin_name = None
        self._risks = None

    @property
    def can_mark(self):
        return self._can_mark

    @can_mark.setter
    def can_mark(self, value):
        self._can_mark = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
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
    def generated_url(self):
        return self._generated_url

    @generated_url.setter
    def generated_url(self, value):
        self._generated_url = value
    @property
    def origin_file(self):
        return self._origin_file

    @origin_file.setter
    def origin_file(self, value):
        self._origin_file = value
    @property
    def origin_name(self):
        return self._origin_name

    @origin_name.setter
    def origin_name(self, value):
        self._origin_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.can_mark:
            if hasattr(self.can_mark, 'to_alipay_dict'):
                params['can_mark'] = self.can_mark.to_alipay_dict()
            else:
                params['can_mark'] = self.can_mark
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
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
        if self.generated_url:
            if hasattr(self.generated_url, 'to_alipay_dict'):
                params['generated_url'] = self.generated_url.to_alipay_dict()
            else:
                params['generated_url'] = self.generated_url
        if self.origin_file:
            if hasattr(self.origin_file, 'to_alipay_dict'):
                params['origin_file'] = self.origin_file.to_alipay_dict()
            else:
                params['origin_file'] = self.origin_file
        if self.origin_name:
            if hasattr(self.origin_name, 'to_alipay_dict'):
                params['origin_name'] = self.origin_name.to_alipay_dict()
            else:
                params['origin_name'] = self.origin_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubContentRisks()
        if 'can_mark' in d:
            o.can_mark = d['can_mark']
        if 'ext' in d:
            o.ext = d['ext']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'generated_url' in d:
            o.generated_url = d['generated_url']
        if 'origin_file' in d:
            o.origin_file = d['origin_file']
        if 'origin_name' in d:
            o.origin_name = d['origin_name']
        if 'risks' in d:
            o.risks = d['risks']
        return o


