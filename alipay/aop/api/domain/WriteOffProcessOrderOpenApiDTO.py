#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WriteOffLeftRightDetailOpenApiDTO import WriteOffLeftRightDetailOpenApiDTO


class WriteOffProcessOrderOpenApiDTO(object):

    def __init__(self):
        self._out_biz_no = None
        self._write_off_detail_open_api_list = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def write_off_detail_open_api_list(self):
        return self._write_off_detail_open_api_list

    @write_off_detail_open_api_list.setter
    def write_off_detail_open_api_list(self, value):
        if isinstance(value, list):
            self._write_off_detail_open_api_list = list()
            for i in value:
                if isinstance(i, WriteOffLeftRightDetailOpenApiDTO):
                    self._write_off_detail_open_api_list.append(i)
                else:
                    self._write_off_detail_open_api_list.append(WriteOffLeftRightDetailOpenApiDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.write_off_detail_open_api_list:
            if isinstance(self.write_off_detail_open_api_list, list):
                for i in range(0, len(self.write_off_detail_open_api_list)):
                    element = self.write_off_detail_open_api_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.write_off_detail_open_api_list[i] = element.to_alipay_dict()
            if hasattr(self.write_off_detail_open_api_list, 'to_alipay_dict'):
                params['write_off_detail_open_api_list'] = self.write_off_detail_open_api_list.to_alipay_dict()
            else:
                params['write_off_detail_open_api_list'] = self.write_off_detail_open_api_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WriteOffProcessOrderOpenApiDTO()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'write_off_detail_open_api_list' in d:
            o.write_off_detail_open_api_list = d['write_off_detail_open_api_list']
        return o


