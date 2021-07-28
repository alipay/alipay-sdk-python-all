#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishSpecGroup import KbdishSpecGroup


class KoubeiCateringDishSpecgroupSyncModel(object):

    def __init__(self):
        self._create_user = None
        self._kbdish_spec_group = None
        self._syn_type = None
        self._update_user = None

    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def kbdish_spec_group(self):
        return self._kbdish_spec_group

    @kbdish_spec_group.setter
    def kbdish_spec_group(self, value):
        if isinstance(value, KbdishSpecGroup):
            self._kbdish_spec_group = value
        else:
            self._kbdish_spec_group = KbdishSpecGroup.from_alipay_dict(value)
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.kbdish_spec_group:
            if hasattr(self.kbdish_spec_group, 'to_alipay_dict'):
                params['kbdish_spec_group'] = self.kbdish_spec_group.to_alipay_dict()
            else:
                params['kbdish_spec_group'] = self.kbdish_spec_group
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishSpecgroupSyncModel()
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'kbdish_spec_group' in d:
            o.kbdish_spec_group = d['kbdish_spec_group']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


