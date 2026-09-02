#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UniqueBizInfo(object):

    def __init__(self):
        self._sub_phone_no = None
        self._sub_unique_biz_no = None

    @property
    def sub_phone_no(self):
        return self._sub_phone_no

    @sub_phone_no.setter
    def sub_phone_no(self, value):
        self._sub_phone_no = value
    @property
    def sub_unique_biz_no(self):
        return self._sub_unique_biz_no

    @sub_unique_biz_no.setter
    def sub_unique_biz_no(self, value):
        self._sub_unique_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_phone_no:
            if hasattr(self.sub_phone_no, 'to_alipay_dict'):
                params['sub_phone_no'] = self.sub_phone_no.to_alipay_dict()
            else:
                params['sub_phone_no'] = self.sub_phone_no
        if self.sub_unique_biz_no:
            if hasattr(self.sub_unique_biz_no, 'to_alipay_dict'):
                params['sub_unique_biz_no'] = self.sub_unique_biz_no.to_alipay_dict()
            else:
                params['sub_unique_biz_no'] = self.sub_unique_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UniqueBizInfo()
        if 'sub_phone_no' in d:
            o.sub_phone_no = d['sub_phone_no']
        if 'sub_unique_biz_no' in d:
            o.sub_unique_biz_no = d['sub_unique_biz_no']
        return o


