#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbikeChargeQrcodeParam(object):

    def __init__(self):
        self._biz_no = None
        self._ch_info = None
        self._describe = None
        self._ext_param = None
        self._query_param = None
        self._size = None
        self._url_param = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, value):
        self._query_param = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def url_param(self):
        return self._url_param

    @url_param.setter
    def url_param(self, value):
        self._url_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.query_param:
            if hasattr(self.query_param, 'to_alipay_dict'):
                params['query_param'] = self.query_param.to_alipay_dict()
            else:
                params['query_param'] = self.query_param
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.url_param:
            if hasattr(self.url_param, 'to_alipay_dict'):
                params['url_param'] = self.url_param.to_alipay_dict()
            else:
                params['url_param'] = self.url_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EbikeChargeQrcodeParam()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'describe' in d:
            o.describe = d['describe']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'query_param' in d:
            o.query_param = d['query_param']
        if 'size' in d:
            o.size = d['size']
        if 'url_param' in d:
            o.url_param = d['url_param']
        return o


