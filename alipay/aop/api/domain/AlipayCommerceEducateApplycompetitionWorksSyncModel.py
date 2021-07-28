#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateApplycompetitionWorksSyncModel(object):

    def __init__(self):
        self._apply_status = None
        self._extend_info = None
        self._file_type = None
        self._files_url = None
        self._participant_id = None
        self._source_id = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def files_url(self):
        return self._files_url

    @files_url.setter
    def files_url(self, value):
        self._files_url = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.files_url:
            if hasattr(self.files_url, 'to_alipay_dict'):
                params['files_url'] = self.files_url.to_alipay_dict()
            else:
                params['files_url'] = self.files_url
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateApplycompetitionWorksSyncModel()
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'files_url' in d:
            o.files_url = d['files_url']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


