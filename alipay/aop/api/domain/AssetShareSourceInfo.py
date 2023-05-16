#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetShareSourceInfo(object):

    def __init__(self):
        self._share_mode = None
        self._source_id_list = None

    @property
    def share_mode(self):
        return self._share_mode

    @share_mode.setter
    def share_mode(self, value):
        self._share_mode = value
    @property
    def source_id_list(self):
        return self._source_id_list

    @source_id_list.setter
    def source_id_list(self, value):
        if isinstance(value, list):
            self._source_id_list = list()
            for i in value:
                self._source_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.share_mode:
            if hasattr(self.share_mode, 'to_alipay_dict'):
                params['share_mode'] = self.share_mode.to_alipay_dict()
            else:
                params['share_mode'] = self.share_mode
        if self.source_id_list:
            if isinstance(self.source_id_list, list):
                for i in range(0, len(self.source_id_list)):
                    element = self.source_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.source_id_list[i] = element.to_alipay_dict()
            if hasattr(self.source_id_list, 'to_alipay_dict'):
                params['source_id_list'] = self.source_id_list.to_alipay_dict()
            else:
                params['source_id_list'] = self.source_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetShareSourceInfo()
        if 'share_mode' in d:
            o.share_mode = d['share_mode']
        if 'source_id_list' in d:
            o.source_id_list = d['source_id_list']
        return o


