#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateRosterInfoDeleteModel(object):

    def __init__(self):
        self._inst_id = None
        self._roster_id_list = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def roster_id_list(self):
        return self._roster_id_list

    @roster_id_list.setter
    def roster_id_list(self, value):
        if isinstance(value, list):
            self._roster_id_list = list()
            for i in value:
                self._roster_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.roster_id_list:
            if isinstance(self.roster_id_list, list):
                for i in range(0, len(self.roster_id_list)):
                    element = self.roster_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.roster_id_list[i] = element.to_alipay_dict()
            if hasattr(self.roster_id_list, 'to_alipay_dict'):
                params['roster_id_list'] = self.roster_id_list.to_alipay_dict()
            else:
                params['roster_id_list'] = self.roster_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateRosterInfoDeleteModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'roster_id_list' in d:
            o.roster_id_list = d['roster_id_list']
        return o


