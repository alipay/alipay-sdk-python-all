#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobResumeauthloginurlGetModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._return_complete_url = None
        self._template_id = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def return_complete_url(self):
        return self._return_complete_url

    @return_complete_url.setter
    def return_complete_url(self, value):
        self._return_complete_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.return_complete_url:
            if hasattr(self.return_complete_url, 'to_alipay_dict'):
                params['return_complete_url'] = self.return_complete_url.to_alipay_dict()
            else:
                params['return_complete_url'] = self.return_complete_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryJobResumeauthloginurlGetModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'return_complete_url' in d:
            o.return_complete_url = d['return_complete_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


