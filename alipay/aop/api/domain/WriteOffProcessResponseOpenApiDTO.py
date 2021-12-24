#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WriteOffProcessDetailResponseOpenApiDTO import WriteOffProcessDetailResponseOpenApiDTO


class WriteOffProcessResponseOpenApiDTO(object):

    def __init__(self):
        self._detail_list = None
        self._out_biz_no = None

    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, WriteOffProcessDetailResponseOpenApiDTO):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(WriteOffProcessDetailResponseOpenApiDTO.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WriteOffProcessResponseOpenApiDTO()
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


