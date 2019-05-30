#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSceneprodDataUploadModel(object):

    def __init__(self):
        self._app_seqno = None
        self._data_config = None
        self._data_content = None
        self._org_code = None
        self._product_code = None

    @property
    def app_seqno(self):
        return self._app_seqno

    @app_seqno.setter
    def app_seqno(self, value):
        self._app_seqno = value
    @property
    def data_config(self):
        return self._data_config

    @data_config.setter
    def data_config(self, value):
        self._data_config = value
    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_seqno:
            if hasattr(self.app_seqno, 'to_alipay_dict'):
                params['app_seqno'] = self.app_seqno.to_alipay_dict()
            else:
                params['app_seqno'] = self.app_seqno
        if self.data_config:
            if hasattr(self.data_config, 'to_alipay_dict'):
                params['data_config'] = self.data_config.to_alipay_dict()
            else:
                params['data_config'] = self.data_config
        if self.data_content:
            if hasattr(self.data_content, 'to_alipay_dict'):
                params['data_content'] = self.data_content.to_alipay_dict()
            else:
                params['data_content'] = self.data_content
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSceneprodDataUploadModel()
        if 'app_seqno' in d:
            o.app_seqno = d['app_seqno']
        if 'data_config' in d:
            o.data_config = d['data_config']
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


