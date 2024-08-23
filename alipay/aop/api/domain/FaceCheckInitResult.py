#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceCheckInitResult(object):

    def __init__(self):
        self._verify_biz_no = None
        self._verify_id = None
        self._verify_url = None

    @property
    def verify_biz_no(self):
        return self._verify_biz_no

    @verify_biz_no.setter
    def verify_biz_no(self, value):
        self._verify_biz_no = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value
    @property
    def verify_url(self):
        return self._verify_url

    @verify_url.setter
    def verify_url(self, value):
        self._verify_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.verify_biz_no:
            if hasattr(self.verify_biz_no, 'to_alipay_dict'):
                params['verify_biz_no'] = self.verify_biz_no.to_alipay_dict()
            else:
                params['verify_biz_no'] = self.verify_biz_no
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        if self.verify_url:
            if hasattr(self.verify_url, 'to_alipay_dict'):
                params['verify_url'] = self.verify_url.to_alipay_dict()
            else:
                params['verify_url'] = self.verify_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceCheckInitResult()
        if 'verify_biz_no' in d:
            o.verify_biz_no = d['verify_biz_no']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        if 'verify_url' in d:
            o.verify_url = d['verify_url']
        return o


