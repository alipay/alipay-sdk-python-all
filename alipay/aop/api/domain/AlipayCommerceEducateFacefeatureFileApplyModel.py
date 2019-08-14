#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateFacefeatureFileApplyModel(object):

    def __init__(self):
        self._biz_code = None
        self._feature_version = None
        self._file_date = None
        self._file_type = None
        self._institution_id = None
        self._isv_name = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def feature_version(self):
        return self._feature_version

    @feature_version.setter
    def feature_version(self, value):
        self._feature_version = value
    @property
    def file_date(self):
        return self._file_date

    @file_date.setter
    def file_date(self, value):
        self._file_date = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.feature_version:
            if hasattr(self.feature_version, 'to_alipay_dict'):
                params['feature_version'] = self.feature_version.to_alipay_dict()
            else:
                params['feature_version'] = self.feature_version
        if self.file_date:
            if hasattr(self.file_date, 'to_alipay_dict'):
                params['file_date'] = self.file_date.to_alipay_dict()
            else:
                params['file_date'] = self.file_date
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateFacefeatureFileApplyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'feature_version' in d:
            o.feature_version = d['feature_version']
        if 'file_date' in d:
            o.file_date = d['file_date']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        return o


