#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagSnInfoListRequest import TagSnInfoListRequest


class AlipayCommerceIotManufacturerSnQueryModel(object):

    def __init__(self):
        self._tag_sn_info_list_request = None

    @property
    def tag_sn_info_list_request(self):
        return self._tag_sn_info_list_request

    @tag_sn_info_list_request.setter
    def tag_sn_info_list_request(self, value):
        if isinstance(value, list):
            self._tag_sn_info_list_request = list()
            for i in value:
                if isinstance(i, TagSnInfoListRequest):
                    self._tag_sn_info_list_request.append(i)
                else:
                    self._tag_sn_info_list_request.append(TagSnInfoListRequest.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.tag_sn_info_list_request:
            if isinstance(self.tag_sn_info_list_request, list):
                for i in range(0, len(self.tag_sn_info_list_request)):
                    element = self.tag_sn_info_list_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_sn_info_list_request[i] = element.to_alipay_dict()
            if hasattr(self.tag_sn_info_list_request, 'to_alipay_dict'):
                params['tag_sn_info_list_request'] = self.tag_sn_info_list_request.to_alipay_dict()
            else:
                params['tag_sn_info_list_request'] = self.tag_sn_info_list_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotManufacturerSnQueryModel()
        if 'tag_sn_info_list_request' in d:
            o.tag_sn_info_list_request = d['tag_sn_info_list_request']
        return o


