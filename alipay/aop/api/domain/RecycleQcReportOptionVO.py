#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleQcReportOptionVO(object):

    def __init__(self):
        self._defect_option = None
        self._option_code = None
        self._option_image_id_list = None
        self._option_image_url_list = None
        self._option_name = None

    @property
    def defect_option(self):
        return self._defect_option

    @defect_option.setter
    def defect_option(self, value):
        self._defect_option = value
    @property
    def option_code(self):
        return self._option_code

    @option_code.setter
    def option_code(self, value):
        self._option_code = value
    @property
    def option_image_id_list(self):
        return self._option_image_id_list

    @option_image_id_list.setter
    def option_image_id_list(self, value):
        if isinstance(value, list):
            self._option_image_id_list = list()
            for i in value:
                self._option_image_id_list.append(i)
    @property
    def option_image_url_list(self):
        return self._option_image_url_list

    @option_image_url_list.setter
    def option_image_url_list(self, value):
        if isinstance(value, list):
            self._option_image_url_list = list()
            for i in value:
                self._option_image_url_list.append(i)
    @property
    def option_name(self):
        return self._option_name

    @option_name.setter
    def option_name(self, value):
        self._option_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.defect_option:
            if hasattr(self.defect_option, 'to_alipay_dict'):
                params['defect_option'] = self.defect_option.to_alipay_dict()
            else:
                params['defect_option'] = self.defect_option
        if self.option_code:
            if hasattr(self.option_code, 'to_alipay_dict'):
                params['option_code'] = self.option_code.to_alipay_dict()
            else:
                params['option_code'] = self.option_code
        if self.option_image_id_list:
            if isinstance(self.option_image_id_list, list):
                for i in range(0, len(self.option_image_id_list)):
                    element = self.option_image_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.option_image_id_list[i] = element.to_alipay_dict()
            if hasattr(self.option_image_id_list, 'to_alipay_dict'):
                params['option_image_id_list'] = self.option_image_id_list.to_alipay_dict()
            else:
                params['option_image_id_list'] = self.option_image_id_list
        if self.option_image_url_list:
            if isinstance(self.option_image_url_list, list):
                for i in range(0, len(self.option_image_url_list)):
                    element = self.option_image_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.option_image_url_list[i] = element.to_alipay_dict()
            if hasattr(self.option_image_url_list, 'to_alipay_dict'):
                params['option_image_url_list'] = self.option_image_url_list.to_alipay_dict()
            else:
                params['option_image_url_list'] = self.option_image_url_list
        if self.option_name:
            if hasattr(self.option_name, 'to_alipay_dict'):
                params['option_name'] = self.option_name.to_alipay_dict()
            else:
                params['option_name'] = self.option_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQcReportOptionVO()
        if 'defect_option' in d:
            o.defect_option = d['defect_option']
        if 'option_code' in d:
            o.option_code = d['option_code']
        if 'option_image_id_list' in d:
            o.option_image_id_list = d['option_image_id_list']
        if 'option_image_url_list' in d:
            o.option_image_url_list = d['option_image_url_list']
        if 'option_name' in d:
            o.option_name = d['option_name']
        return o


