#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeDeleteFailDetail import CreativeDeleteFailDetail


class OpenDeleteCreativeResponse(object):

    def __init__(self):
        self._creative_fail_detail_list = None
        self._creative_outer_id_success_list = None

    @property
    def creative_fail_detail_list(self):
        return self._creative_fail_detail_list

    @creative_fail_detail_list.setter
    def creative_fail_detail_list(self, value):
        if isinstance(value, list):
            self._creative_fail_detail_list = list()
            for i in value:
                if isinstance(i, CreativeDeleteFailDetail):
                    self._creative_fail_detail_list.append(i)
                else:
                    self._creative_fail_detail_list.append(CreativeDeleteFailDetail.from_alipay_dict(i))
    @property
    def creative_outer_id_success_list(self):
        return self._creative_outer_id_success_list

    @creative_outer_id_success_list.setter
    def creative_outer_id_success_list(self, value):
        if isinstance(value, list):
            self._creative_outer_id_success_list = list()
            for i in value:
                self._creative_outer_id_success_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.creative_fail_detail_list:
            if isinstance(self.creative_fail_detail_list, list):
                for i in range(0, len(self.creative_fail_detail_list)):
                    element = self.creative_fail_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_fail_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_fail_detail_list, 'to_alipay_dict'):
                params['creative_fail_detail_list'] = self.creative_fail_detail_list.to_alipay_dict()
            else:
                params['creative_fail_detail_list'] = self.creative_fail_detail_list
        if self.creative_outer_id_success_list:
            if isinstance(self.creative_outer_id_success_list, list):
                for i in range(0, len(self.creative_outer_id_success_list)):
                    element = self.creative_outer_id_success_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_outer_id_success_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_outer_id_success_list, 'to_alipay_dict'):
                params['creative_outer_id_success_list'] = self.creative_outer_id_success_list.to_alipay_dict()
            else:
                params['creative_outer_id_success_list'] = self.creative_outer_id_success_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenDeleteCreativeResponse()
        if 'creative_fail_detail_list' in d:
            o.creative_fail_detail_list = d['creative_fail_detail_list']
        if 'creative_outer_id_success_list' in d:
            o.creative_outer_id_success_list = d['creative_outer_id_success_list']
        return o


