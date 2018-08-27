#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbCodeBindInfoVO import KbCodeBindInfoVO


class KoubeiCateringKbcodeCreateModel(object):

    def __init__(self):
        self._bind_info_list = None
        self._request_id = None
        self._stuff_template = None
        self._stuff_type = None

    @property
    def bind_info_list(self):
        return self._bind_info_list

    @bind_info_list.setter
    def bind_info_list(self, value):
        if isinstance(value, list):
            self._bind_info_list = list()
            for i in value:
                if isinstance(i, KbCodeBindInfoVO):
                    self._bind_info_list.append(i)
                else:
                    self._bind_info_list.append(KbCodeBindInfoVO.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def stuff_template(self):
        return self._stuff_template

    @stuff_template.setter
    def stuff_template(self, value):
        self._stuff_template = value
    @property
    def stuff_type(self):
        return self._stuff_type

    @stuff_type.setter
    def stuff_type(self, value):
        self._stuff_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_info_list:
            if isinstance(self.bind_info_list, list):
                for i in range(0, len(self.bind_info_list)):
                    element = self.bind_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_info_list[i] = element.to_alipay_dict()
            if hasattr(self.bind_info_list, 'to_alipay_dict'):
                params['bind_info_list'] = self.bind_info_list.to_alipay_dict()
            else:
                params['bind_info_list'] = self.bind_info_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.stuff_template:
            if hasattr(self.stuff_template, 'to_alipay_dict'):
                params['stuff_template'] = self.stuff_template.to_alipay_dict()
            else:
                params['stuff_template'] = self.stuff_template
        if self.stuff_type:
            if hasattr(self.stuff_type, 'to_alipay_dict'):
                params['stuff_type'] = self.stuff_type.to_alipay_dict()
            else:
                params['stuff_type'] = self.stuff_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringKbcodeCreateModel()
        if 'bind_info_list' in d:
            o.bind_info_list = d['bind_info_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'stuff_template' in d:
            o.stuff_template = d['stuff_template']
        if 'stuff_type' in d:
            o.stuff_type = d['stuff_type']
        return o


