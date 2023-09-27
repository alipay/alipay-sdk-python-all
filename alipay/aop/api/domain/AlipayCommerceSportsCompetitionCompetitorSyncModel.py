#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsCompetitionCompetitorSyncModel(object):

    def __init__(self):
        self._cn_name = None
        self._code = None
        self._competition_code = None
        self._data_version = None
        self._en_name = None
        self._icon = None
        self._status = None

    @property
    def cn_name(self):
        return self._cn_name

    @cn_name.setter
    def cn_name(self, value):
        self._cn_name = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def competition_code(self):
        return self._competition_code

    @competition_code.setter
    def competition_code(self, value):
        self._competition_code = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cn_name:
            if hasattr(self.cn_name, 'to_alipay_dict'):
                params['cn_name'] = self.cn_name.to_alipay_dict()
            else:
                params['cn_name'] = self.cn_name
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.competition_code:
            if hasattr(self.competition_code, 'to_alipay_dict'):
                params['competition_code'] = self.competition_code.to_alipay_dict()
            else:
                params['competition_code'] = self.competition_code
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSportsCompetitionCompetitorSyncModel()
        if 'cn_name' in d:
            o.cn_name = d['cn_name']
        if 'code' in d:
            o.code = d['code']
        if 'competition_code' in d:
            o.competition_code = d['competition_code']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'icon' in d:
            o.icon = d['icon']
        if 'status' in d:
            o.status = d['status']
        return o


