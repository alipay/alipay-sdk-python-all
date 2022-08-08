#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PageInfoDTO import PageInfoDTO


class DatadigitalFincloudFinsaasDesignPageModifyModel(object):

    def __init__(self):
        self._page_info = None

    @property
    def page_info(self):
        return self._page_info

    @page_info.setter
    def page_info(self, value):
        if isinstance(value, PageInfoDTO):
            self._page_info = value
        else:
            self._page_info = PageInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.page_info:
            if hasattr(self.page_info, 'to_alipay_dict'):
                params['page_info'] = self.page_info.to_alipay_dict()
            else:
                params['page_info'] = self.page_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasDesignPageModifyModel()
        if 'page_info' in d:
            o.page_info = d['page_info']
        return o


