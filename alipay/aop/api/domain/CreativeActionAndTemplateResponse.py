#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreativeTemplateResp import CreativeTemplateResp


class CreativeActionAndTemplateResponse(object):

    def __init__(self):
        self._action_type_list = None
        self._creative_template_resp = None

    @property
    def action_type_list(self):
        return self._action_type_list

    @action_type_list.setter
    def action_type_list(self, value):
        if isinstance(value, list):
            self._action_type_list = list()
            for i in value:
                self._action_type_list.append(i)
    @property
    def creative_template_resp(self):
        return self._creative_template_resp

    @creative_template_resp.setter
    def creative_template_resp(self, value):
        if isinstance(value, CreativeTemplateResp):
            self._creative_template_resp = value
        else:
            self._creative_template_resp = CreativeTemplateResp.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action_type_list:
            if isinstance(self.action_type_list, list):
                for i in range(0, len(self.action_type_list)):
                    element = self.action_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.action_type_list[i] = element.to_alipay_dict()
            if hasattr(self.action_type_list, 'to_alipay_dict'):
                params['action_type_list'] = self.action_type_list.to_alipay_dict()
            else:
                params['action_type_list'] = self.action_type_list
        if self.creative_template_resp:
            if hasattr(self.creative_template_resp, 'to_alipay_dict'):
                params['creative_template_resp'] = self.creative_template_resp.to_alipay_dict()
            else:
                params['creative_template_resp'] = self.creative_template_resp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeActionAndTemplateResponse()
        if 'action_type_list' in d:
            o.action_type_list = d['action_type_list']
        if 'creative_template_resp' in d:
            o.creative_template_resp = d['creative_template_resp']
        return o


