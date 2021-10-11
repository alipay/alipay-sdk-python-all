#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstInfo(object):

    def __init__(self):
        self._inst_id = None
        self._isv_inst_no = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def isv_inst_no(self):
        return self._isv_inst_no

    @isv_inst_no.setter
    def isv_inst_no(self, value):
        self._isv_inst_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.isv_inst_no:
            if hasattr(self.isv_inst_no, 'to_alipay_dict'):
                params['isv_inst_no'] = self.isv_inst_no.to_alipay_dict()
            else:
                params['isv_inst_no'] = self.isv_inst_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstInfo()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'isv_inst_no' in d:
            o.isv_inst_no = d['isv_inst_no']
        return o


