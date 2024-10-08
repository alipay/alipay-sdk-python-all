#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApartmentPicInfo(object):

    def __init__(self):
        self._appearance_pic_list = None
        self._function_area_pic_list = None
        self._hall_pic_list = None
        self._leisure_area_pic_list = None

    @property
    def appearance_pic_list(self):
        return self._appearance_pic_list

    @appearance_pic_list.setter
    def appearance_pic_list(self, value):
        if isinstance(value, list):
            self._appearance_pic_list = list()
            for i in value:
                self._appearance_pic_list.append(i)
    @property
    def function_area_pic_list(self):
        return self._function_area_pic_list

    @function_area_pic_list.setter
    def function_area_pic_list(self, value):
        if isinstance(value, list):
            self._function_area_pic_list = list()
            for i in value:
                self._function_area_pic_list.append(i)
    @property
    def hall_pic_list(self):
        return self._hall_pic_list

    @hall_pic_list.setter
    def hall_pic_list(self, value):
        if isinstance(value, list):
            self._hall_pic_list = list()
            for i in value:
                self._hall_pic_list.append(i)
    @property
    def leisure_area_pic_list(self):
        return self._leisure_area_pic_list

    @leisure_area_pic_list.setter
    def leisure_area_pic_list(self, value):
        if isinstance(value, list):
            self._leisure_area_pic_list = list()
            for i in value:
                self._leisure_area_pic_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.appearance_pic_list:
            if isinstance(self.appearance_pic_list, list):
                for i in range(0, len(self.appearance_pic_list)):
                    element = self.appearance_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.appearance_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.appearance_pic_list, 'to_alipay_dict'):
                params['appearance_pic_list'] = self.appearance_pic_list.to_alipay_dict()
            else:
                params['appearance_pic_list'] = self.appearance_pic_list
        if self.function_area_pic_list:
            if isinstance(self.function_area_pic_list, list):
                for i in range(0, len(self.function_area_pic_list)):
                    element = self.function_area_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.function_area_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.function_area_pic_list, 'to_alipay_dict'):
                params['function_area_pic_list'] = self.function_area_pic_list.to_alipay_dict()
            else:
                params['function_area_pic_list'] = self.function_area_pic_list
        if self.hall_pic_list:
            if isinstance(self.hall_pic_list, list):
                for i in range(0, len(self.hall_pic_list)):
                    element = self.hall_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.hall_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.hall_pic_list, 'to_alipay_dict'):
                params['hall_pic_list'] = self.hall_pic_list.to_alipay_dict()
            else:
                params['hall_pic_list'] = self.hall_pic_list
        if self.leisure_area_pic_list:
            if isinstance(self.leisure_area_pic_list, list):
                for i in range(0, len(self.leisure_area_pic_list)):
                    element = self.leisure_area_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leisure_area_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.leisure_area_pic_list, 'to_alipay_dict'):
                params['leisure_area_pic_list'] = self.leisure_area_pic_list.to_alipay_dict()
            else:
                params['leisure_area_pic_list'] = self.leisure_area_pic_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApartmentPicInfo()
        if 'appearance_pic_list' in d:
            o.appearance_pic_list = d['appearance_pic_list']
        if 'function_area_pic_list' in d:
            o.function_area_pic_list = d['function_area_pic_list']
        if 'hall_pic_list' in d:
            o.hall_pic_list = d['hall_pic_list']
        if 'leisure_area_pic_list' in d:
            o.leisure_area_pic_list = d['leisure_area_pic_list']
        return o


