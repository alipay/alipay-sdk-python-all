#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAssetVoucherTemplateInfoQuerybudgetModel(object):

    def __init__(self):
        self._is_real_time_data = None
        self._mode = None
        self._template_id_list = None

    @property
    def is_real_time_data(self):
        return self._is_real_time_data

    @is_real_time_data.setter
    def is_real_time_data(self, value):
        self._is_real_time_data = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def template_id_list(self):
        return self._template_id_list

    @template_id_list.setter
    def template_id_list(self, value):
        self._template_id_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.is_real_time_data:
            if hasattr(self.is_real_time_data, 'to_alipay_dict'):
                params['is_real_time_data'] = self.is_real_time_data.to_alipay_dict()
            else:
                params['is_real_time_data'] = self.is_real_time_data
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.template_id_list:
            if hasattr(self.template_id_list, 'to_alipay_dict'):
                params['template_id_list'] = self.template_id_list.to_alipay_dict()
            else:
                params['template_id_list'] = self.template_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetVoucherTemplateInfoQuerybudgetModel()
        if 'is_real_time_data' in d:
            o.is_real_time_data = d['is_real_time_data']
        if 'mode' in d:
            o.mode = d['mode']
        if 'template_id_list' in d:
            o.template_id_list = d['template_id_list']
        return o


