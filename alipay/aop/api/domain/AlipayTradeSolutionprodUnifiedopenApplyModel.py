#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UniOpenReqItem import UniOpenReqItem


class AlipayTradeSolutionprodUnifiedopenApplyModel(object):

    def __init__(self):
        self._back_url = None
        self._back_url_type = None
        self._cert_no = None
        self._cert_type = None
        self._open_item_list = None
        self._out_biz_no = None
        self._real_name = None
        self._solution_code = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def back_url_type(self):
        return self._back_url_type

    @back_url_type.setter
    def back_url_type(self, value):
        self._back_url_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def open_item_list(self):
        return self._open_item_list

    @open_item_list.setter
    def open_item_list(self, value):
        if isinstance(value, list):
            self._open_item_list = list()
            for i in value:
                if isinstance(i, UniOpenReqItem):
                    self._open_item_list.append(i)
                else:
                    self._open_item_list.append(UniOpenReqItem.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.back_url_type:
            if hasattr(self.back_url_type, 'to_alipay_dict'):
                params['back_url_type'] = self.back_url_type.to_alipay_dict()
            else:
                params['back_url_type'] = self.back_url_type
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.open_item_list:
            if isinstance(self.open_item_list, list):
                for i in range(0, len(self.open_item_list)):
                    element = self.open_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_item_list[i] = element.to_alipay_dict()
            if hasattr(self.open_item_list, 'to_alipay_dict'):
                params['open_item_list'] = self.open_item_list.to_alipay_dict()
            else:
                params['open_item_list'] = self.open_item_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSolutionprodUnifiedopenApplyModel()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'back_url_type' in d:
            o.back_url_type = d['back_url_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'open_item_list' in d:
            o.open_item_list = d['open_item_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


