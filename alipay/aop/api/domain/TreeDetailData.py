#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TreeDetailData(object):

    def __init__(self):
        self._apply_time = None
        self._certificate_id = None
        self._cooperation = None
        self._tree_alias = None
        self._tree_type = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def cooperation(self):
        return self._cooperation

    @cooperation.setter
    def cooperation(self, value):
        self._cooperation = value
    @property
    def tree_alias(self):
        return self._tree_alias

    @tree_alias.setter
    def tree_alias(self, value):
        self._tree_alias = value
    @property
    def tree_type(self):
        return self._tree_type

    @tree_type.setter
    def tree_type(self, value):
        self._tree_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.cooperation:
            if hasattr(self.cooperation, 'to_alipay_dict'):
                params['cooperation'] = self.cooperation.to_alipay_dict()
            else:
                params['cooperation'] = self.cooperation
        if self.tree_alias:
            if hasattr(self.tree_alias, 'to_alipay_dict'):
                params['tree_alias'] = self.tree_alias.to_alipay_dict()
            else:
                params['tree_alias'] = self.tree_alias
        if self.tree_type:
            if hasattr(self.tree_type, 'to_alipay_dict'):
                params['tree_type'] = self.tree_type.to_alipay_dict()
            else:
                params['tree_type'] = self.tree_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreeDetailData()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'cooperation' in d:
            o.cooperation = d['cooperation']
        if 'tree_alias' in d:
            o.tree_alias = d['tree_alias']
        if 'tree_type' in d:
            o.tree_type = d['tree_type']
        return o


