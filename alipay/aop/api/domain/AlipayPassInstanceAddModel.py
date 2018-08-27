#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPassInstanceAddModel(object):

    def __init__(self):
        self._recognition_info = None
        self._recognition_type = None
        self._tpl_id = None
        self._tpl_params = None

    @property
    def recognition_info(self):
        return self._recognition_info

    @recognition_info.setter
    def recognition_info(self, value):
        self._recognition_info = value
    @property
    def recognition_type(self):
        return self._recognition_type

    @recognition_type.setter
    def recognition_type(self, value):
        self._recognition_type = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value
    @property
    def tpl_params(self):
        return self._tpl_params

    @tpl_params.setter
    def tpl_params(self, value):
        self._tpl_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.recognition_info:
            if hasattr(self.recognition_info, 'to_alipay_dict'):
                params['recognition_info'] = self.recognition_info.to_alipay_dict()
            else:
                params['recognition_info'] = self.recognition_info
        if self.recognition_type:
            if hasattr(self.recognition_type, 'to_alipay_dict'):
                params['recognition_type'] = self.recognition_type.to_alipay_dict()
            else:
                params['recognition_type'] = self.recognition_type
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        if self.tpl_params:
            if hasattr(self.tpl_params, 'to_alipay_dict'):
                params['tpl_params'] = self.tpl_params.to_alipay_dict()
            else:
                params['tpl_params'] = self.tpl_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPassInstanceAddModel()
        if 'recognition_info' in d:
            o.recognition_info = d['recognition_info']
        if 'recognition_type' in d:
            o.recognition_type = d['recognition_type']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        if 'tpl_params' in d:
            o.tpl_params = d['tpl_params']
        return o


