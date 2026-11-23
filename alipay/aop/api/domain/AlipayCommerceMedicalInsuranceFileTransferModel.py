#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HkFileItem import HkFileItem


class AlipayCommerceMedicalInsuranceFileTransferModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_type = None
        self._company_type = None
        self._file_items = None
        self._has_more_files = None
        self._hk_scene = None
        self._open_id = None
        self._policy_no = None
        self._request_no = None
        self._source = None
        self._tpa_id = None
        self._user_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def file_items(self):
        return self._file_items

    @file_items.setter
    def file_items(self, value):
        if isinstance(value, list):
            self._file_items = list()
            for i in value:
                if isinstance(i, HkFileItem):
                    self._file_items.append(i)
                else:
                    self._file_items.append(HkFileItem.from_alipay_dict(i))
    @property
    def has_more_files(self):
        return self._has_more_files

    @has_more_files.setter
    def has_more_files(self, value):
        self._has_more_files = value
    @property
    def hk_scene(self):
        return self._hk_scene

    @hk_scene.setter
    def hk_scene(self, value):
        self._hk_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.file_items:
            if isinstance(self.file_items, list):
                for i in range(0, len(self.file_items)):
                    element = self.file_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_items[i] = element.to_alipay_dict()
            if hasattr(self.file_items, 'to_alipay_dict'):
                params['file_items'] = self.file_items.to_alipay_dict()
            else:
                params['file_items'] = self.file_items
        if self.has_more_files:
            if hasattr(self.has_more_files, 'to_alipay_dict'):
                params['has_more_files'] = self.has_more_files.to_alipay_dict()
            else:
                params['has_more_files'] = self.has_more_files
        if self.hk_scene:
            if hasattr(self.hk_scene, 'to_alipay_dict'):
                params['hk_scene'] = self.hk_scene.to_alipay_dict()
            else:
                params['hk_scene'] = self.hk_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceFileTransferModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'file_items' in d:
            o.file_items = d['file_items']
        if 'has_more_files' in d:
            o.has_more_files = d['has_more_files']
        if 'hk_scene' in d:
            o.hk_scene = d['hk_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'source' in d:
            o.source = d['source']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


