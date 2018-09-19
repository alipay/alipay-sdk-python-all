#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupSetting import GroupSetting


class AlipaySocialBaseGroupCreateModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_type = None
        self._group_settings = None
        self._master_id = None

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
    def group_settings(self):
        return self._group_settings

    @group_settings.setter
    def group_settings(self, value):
        if isinstance(value, GroupSetting):
            self._group_settings = value
        else:
            self._group_settings = GroupSetting.from_alipay_dict(value)
    @property
    def master_id(self):
        return self._master_id

    @master_id.setter
    def master_id(self, value):
        self._master_id = value


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
        if self.group_settings:
            if hasattr(self.group_settings, 'to_alipay_dict'):
                params['group_settings'] = self.group_settings.to_alipay_dict()
            else:
                params['group_settings'] = self.group_settings
        if self.master_id:
            if hasattr(self.master_id, 'to_alipay_dict'):
                params['master_id'] = self.master_id.to_alipay_dict()
            else:
                params['master_id'] = self.master_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseGroupCreateModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'group_settings' in d:
            o.group_settings = d['group_settings']
        if 'master_id' in d:
            o.master_id = d['master_id']
        return o


