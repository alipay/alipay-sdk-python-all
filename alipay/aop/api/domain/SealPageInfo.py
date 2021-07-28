#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SealRequestInfo import SealRequestInfo


class SealPageInfo(object):

    def __init__(self):
        self._page_index = None
        self._seal_request_info = None

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def seal_request_info(self):
        return self._seal_request_info

    @seal_request_info.setter
    def seal_request_info(self, value):
        if isinstance(value, SealRequestInfo):
            self._seal_request_info = value
        else:
            self._seal_request_info = SealRequestInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.page_index:
            if hasattr(self.page_index, 'to_alipay_dict'):
                params['page_index'] = self.page_index.to_alipay_dict()
            else:
                params['page_index'] = self.page_index
        if self.seal_request_info:
            if hasattr(self.seal_request_info, 'to_alipay_dict'):
                params['seal_request_info'] = self.seal_request_info.to_alipay_dict()
            else:
                params['seal_request_info'] = self.seal_request_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SealPageInfo()
        if 'page_index' in d:
            o.page_index = d['page_index']
        if 'seal_request_info' in d:
            o.seal_request_info = d['seal_request_info']
        return o


