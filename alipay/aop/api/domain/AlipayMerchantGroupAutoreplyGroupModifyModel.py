#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupAutoreplyGroupModifyModel(object):

    def __init__(self):
        self._autoreply_id = None
        self._global_valid = None
        self._group_id_list = None

    @property
    def autoreply_id(self):
        return self._autoreply_id

    @autoreply_id.setter
    def autoreply_id(self, value):
        self._autoreply_id = value
    @property
    def global_valid(self):
        return self._global_valid

    @global_valid.setter
    def global_valid(self, value):
        self._global_valid = value
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.autoreply_id:
            if hasattr(self.autoreply_id, 'to_alipay_dict'):
                params['autoreply_id'] = self.autoreply_id.to_alipay_dict()
            else:
                params['autoreply_id'] = self.autoreply_id
        if self.global_valid:
            if hasattr(self.global_valid, 'to_alipay_dict'):
                params['global_valid'] = self.global_valid.to_alipay_dict()
            else:
                params['global_valid'] = self.global_valid
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupAutoreplyGroupModifyModel()
        if 'autoreply_id' in d:
            o.autoreply_id = d['autoreply_id']
        if 'global_valid' in d:
            o.global_valid = d['global_valid']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        return o


