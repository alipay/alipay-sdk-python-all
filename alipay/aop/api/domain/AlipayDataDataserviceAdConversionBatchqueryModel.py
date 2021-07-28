#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdConversionBatchqueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._conversion_id_list = None
        self._conversion_type = None
        self._page_no = None
        self._page_size = None
        self._principal_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def conversion_id_list(self):
        return self._conversion_id_list

    @conversion_id_list.setter
    def conversion_id_list(self, value):
        if isinstance(value, list):
            self._conversion_id_list = list()
            for i in value:
                self._conversion_id_list.append(i)
    @property
    def conversion_type(self):
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        self._conversion_type = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.conversion_id_list:
            if isinstance(self.conversion_id_list, list):
                for i in range(0, len(self.conversion_id_list)):
                    element = self.conversion_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_id_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_id_list, 'to_alipay_dict'):
                params['conversion_id_list'] = self.conversion_id_list.to_alipay_dict()
            else:
                params['conversion_id_list'] = self.conversion_id_list
        if self.conversion_type:
            if hasattr(self.conversion_type, 'to_alipay_dict'):
                params['conversion_type'] = self.conversion_type.to_alipay_dict()
            else:
                params['conversion_type'] = self.conversion_type
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdConversionBatchqueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'conversion_id_list' in d:
            o.conversion_id_list = d['conversion_id_list']
        if 'conversion_type' in d:
            o.conversion_type = d['conversion_type']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        return o


