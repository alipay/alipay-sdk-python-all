#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenicExtInfo import ScenicExtInfo


class AlipayCommerceDataQrCodeApplyModel(object):

    def __init__(self):
        self._biz_type = None
        self._ext_info = None
        self._isv_pid = None
        self._outer_biz_id = None
        self._page_url = None
        self._shop_id = None
        self._source_code = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ScenicExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ScenicExtInfo.from_alipay_dict(i))
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def outer_biz_id(self):
        return self._outer_biz_id

    @outer_biz_id.setter
    def outer_biz_id(self, value):
        self._outer_biz_id = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_code(self):
        return self._source_code

    @source_code.setter
    def source_code(self, value):
        self._source_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.outer_biz_id:
            if hasattr(self.outer_biz_id, 'to_alipay_dict'):
                params['outer_biz_id'] = self.outer_biz_id.to_alipay_dict()
            else:
                params['outer_biz_id'] = self.outer_biz_id
        if self.page_url:
            if hasattr(self.page_url, 'to_alipay_dict'):
                params['page_url'] = self.page_url.to_alipay_dict()
            else:
                params['page_url'] = self.page_url
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_code:
            if hasattr(self.source_code, 'to_alipay_dict'):
                params['source_code'] = self.source_code.to_alipay_dict()
            else:
                params['source_code'] = self.source_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDataQrCodeApplyModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'outer_biz_id' in d:
            o.outer_biz_id = d['outer_biz_id']
        if 'page_url' in d:
            o.page_url = d['page_url']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_code' in d:
            o.source_code = d['source_code']
        return o


