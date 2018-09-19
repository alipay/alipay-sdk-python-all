#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertIdentifyResponse(object):

    def __init__(self):
        self._benefit_ids = None
        self._benefit_type = None
        self._code = None
        self._ext_info = None
        self._identify = None
        self._identify_type = None

    @property
    def benefit_ids(self):
        return self._benefit_ids

    @benefit_ids.setter
    def benefit_ids(self, value):
        if isinstance(value, list):
            self._benefit_ids = list()
            for i in value:
                self._benefit_ids.append(i)
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, value):
        self._identify = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_ids:
            if isinstance(self.benefit_ids, list):
                for i in range(0, len(self.benefit_ids)):
                    element = self.benefit_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_ids[i] = element.to_alipay_dict()
            if hasattr(self.benefit_ids, 'to_alipay_dict'):
                params['benefit_ids'] = self.benefit_ids.to_alipay_dict()
            else:
                params['benefit_ids'] = self.benefit_ids
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.identify:
            if hasattr(self.identify, 'to_alipay_dict'):
                params['identify'] = self.identify.to_alipay_dict()
            else:
                params['identify'] = self.identify
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertIdentifyResponse()
        if 'benefit_ids' in d:
            o.benefit_ids = d['benefit_ids']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'code' in d:
            o.code = d['code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'identify' in d:
            o.identify = d['identify']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        return o


